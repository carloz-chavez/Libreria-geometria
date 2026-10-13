"""Ejecuta cada suite disponible y guarda evidencia; no instala herramientas."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
BUILD.mkdir(exist_ok=True)
EXE = '.exe' if os.name == 'nt' else ''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--estricto', action='store_true', help='Falla también si falta alguna herramienta')
    args = parser.parse_args()
    suites = [
        ('Python', [], [[sys.executable, '-m', 'unittest', 'discover', '-s', 'python', '-v']]),
        ('SOLID', [], [[sys.executable, 'python/demo_solid.py']]),
        ('JavaScript', ['node'], [['node', '--test', 'javascript/geometria.test.js']]),
        ('C', ['gcc'], [['gcc','-std=c11','-Wall','-Wextra','-Werror','-pedantic','c/geometria.c','c/test_geometria.c','-lm','-o',str(BUILD/('test_c'+EXE))],[str(BUILD/('test_c'+EXE))]]),
        ('C++', ['g++'], [['g++','-std=c++17','-Wall','-Wextra','-Werror','-pedantic','cpp/test_geometria.cpp','-o',str(BUILD/('test_cpp'+EXE))],[str(BUILD/('test_cpp'+EXE))]]),
        ('Java', ['javac','java'], [['javac','-encoding','UTF-8','-d',str(BUILD/'java'),'java/Geometria.java','java/TestGeometria.java'],['java','-cp',str(BUILD/'java'),'TestGeometria']]),
        ('PHP', ['php'], [['php','php/test_geometria.php']]),
        ('Go', ['go'], [['go','test','./...']]),
        ('Rust', ['cargo'], [['cargo','test','--offline']]),
        ('DSL', [], [[sys.executable,'-m','unittest','discover','-s','dsl','-v']]),
    ]
    resultados=[]
    for nombre, herramientas, comandos in suites:
        faltantes = [x for x in herramientas if not shutil.which(x)]
        if nombre == 'DSL' and not importlib.util.find_spec('antlr4'):
            faltantes.append('antlr4-python3-runtime')
        if nombre == 'DSL' and not (ROOT/'dsl/generated/GeometriaParser.py').exists():
            faltantes.append('parser generado')
        r = {'suite': nombre, 'estado':'NO_DISPONIBLE' if faltantes else 'PASA', 'faltantes':faltantes, 'pasos':[]}
        if not faltantes:
            cwd = ROOT / nombre.lower() if nombre in ('Go','Rust') else ROOT
            for comando in comandos:
                try:
                    entorno = dict(os.environ, PYTHONIOENCODING='utf-8')
                    p=subprocess.run(comando,cwd=cwd,env=entorno,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
                    r['pasos'].append({'comando':comando,'codigo':p.returncode,'salida':p.stdout+p.stderr})
                    if p.returncode:
                        r['estado']='FALLA'; break
                except (OSError,subprocess.TimeoutExpired) as e:
                    r['estado']='FALLA'
                    r['pasos'].append({'comando':comando,'error':str(e)})
                    break
        resultados.append(r)
        print(f"{nombre}: {r['estado']}" + (f" ({', '.join(faltantes)})" if faltantes else ''))
    destino=BUILD/'verificacion.json'
    destino.write_text(json.dumps(resultados,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Evidencia: {destino}')
    return int(any(r['estado']=='FALLA' or (args.estricto and r['estado']!='PASA') for r in resultados))

if __name__=='__main__':
    raise SystemExit(main())
