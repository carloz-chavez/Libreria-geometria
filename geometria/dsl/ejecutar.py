"""Consumidor del parser ANTLR4 generado para Python. Requiere runtime 4.13.2."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'python'))
sys.path.insert(0,str(Path(__file__).resolve().parent/'generated'))
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from GeometriaLexer import GeometriaLexer
from GeometriaParser import GeometriaParser
from geometria import Punto, area_poligono

class ErrorSintaxis(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Línea {line}:{column}: {msg}")

def evaluar(texto):
    lexer=GeometriaLexer(InputStream(texto))
    lexer.removeErrorListeners(); lexer.addErrorListener(ErrorSintaxis())
    parser=GeometriaParser(CommonTokenStream(lexer))
    parser.removeErrorListeners(); parser.addErrorListener(ErrorSintaxis())
    arbol=parser.programa()
    simbolos={}; resultados=[]
    for s in arbol.sentencia():
        d=s.declaracion()
        if d:
            nombre=d.ID().getText()
            if nombre in simbolos: raise ValueError(f"Polígono duplicado: {nombre}")
            puntos=[Punto(*(float(n.getText()) for n in p.numero())) for p in d.punto()]
            area_poligono(puntos) # Verificar finitud, cardinalidad y desbordamiento.
            simbolos[nombre]=puntos
        else:
            nombre=s.consulta().ID().getText()
            if nombre not in simbolos: raise ValueError(f"Polígono no definido: {nombre}")
            resultados.append((nombre,area_poligono(simbolos[nombre])))
    return resultados

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Uso: python ejecutar.py archivo.geo')
    try:
        for nombre, area in evaluar(Path(sys.argv[1]).read_text(encoding='utf-8')):
            print(f'{nombre}: {area:g}')
    except ValueError as error: raise SystemExit(str(error))
