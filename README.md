# Geometría: AreaPoligono en siete grupos de lenguajes


## Organización

| Carpeta | Entregable |
|---|---|
| `c/` | Biblioteca `.h/.c`, suite con verificaciones explícitas |
| `cpp/` | Biblioteca header-only C++17 y suite |
| `python/` | Biblioteca, unittest y demostración SOLID |
| `php/` | Biblioteca PHP 8.1+ y suite sin dependencias |
| `javascript/` | Módulo ES y pruebas nativas Node 18+ |
| `java/` | Biblioteca Java y suite; JDK 21+ por `List.reversed()` |
| `go/` | Módulo Go 1.20+ y pruebas `testing` |
| `rust/` | Crate Rust 2021 y pruebas Cargo (sin dependencias) |
| `dsl/` | Gramática, parser Python generado, intérprete, ejemplo y pruebas |
| `tests/` | Ocho vectores de referencia en JSON |
| `docs/` | Contrato, fundamento matemático, SOLID y evidencia |
| `tools/` | Verificación automatizada sin instalación de herramientas |

## Inicio rápido

Desde la raíz de la entrega:

```sh
python -m unittest discover -s python -v
python python/demo_solid.py
node --test javascript/geometria.test.js
python tools/verificar.py
```

`verificar.py` ejecuta las herramientas que estén en PATH y guarda `build/verificacion.json`. Retorna error ante una suite fallida; `--estricto` también exige todas las herramientas y el runtime DSL. No interpreta ausencia de herramientas como prueba aprobada. En este entorno el compilador C/C++ instalado no arranca y tres herramientas no están presentes; consulte `docs/VERIFICACION.md`.

## Compilación y pruebas por lenguaje

Los comandos siguientes son reproducibles desde la raíz. Cree primero `build/` (`mkdir build`). En Windows use `.exe` para los ejecutables de C/C++ y ejecútelos con `./build/test_c.exe` o `./build/test_cpp.exe`; PowerShell acepta `/` en estas rutas. En Linux/macOS use los nombres mostrados.

```sh
# C11, GCC
gcc -std=c11 -Wall -Wextra -Werror -pedantic c/geometria.c c/test_geometria.c -lm -o build/test_c
./build/test_c

# C++17, G++
g++ -std=c++17 -Wall -Wextra -Werror -pedantic cpp/test_geometria.cpp -o build/test_cpp
./build/test_cpp

# Python 3.10+
python -m unittest discover -s python -v

# PHP 8.1+; los checks no dependen de zend.assertions
php php/test_geometria.php

# JavaScript, Node 18+
node --test javascript/geometria.test.js

# JDK 21+
javac -encoding UTF-8 -d build/java java/Geometria.java java/TestGeometria.java
java -cp build/java TestGeometria

# Go 1.20+, desde go/
cd go
go test ./...
cd ..

# Rust estable con edición 2021, desde rust/
cd rust
cargo test --offline
cd ..
```


## Uso de la biblioteca

Python, desde `python/`:

```python
from geometria import Punto, area_poligono
print(area_poligono([Punto(0,0), Punto(4,0), Punto(0,3)]))  # 6.0
```

Cada suite contiene ejemplos ejecutables de su propia API. Consulte [CONTRATO.md](docs/CONTRATO.md) para nombres, errores y límites. Todos los cálculos tienen tiempo O(n) y memoria auxiliar O(1), excluyendo la lista de entrada; el parser DSL sí construye un árbol y una tabla de símbolos.

## DSL ANTLR

Se incluye el parser generado con ANTLR **4.13.2**. Para usarlo solo hace falta instalar su runtime Python compatible:

```sh
python -m pip install -r dsl/requirements.txt
python dsl/ejecutar.py dsl/ejemplo.geo
python -m unittest discover -s dsl -v
```

Salida esperada: `parcela: 12` y `triangulo: 0.125`. Para regenerar el parser, descargue el JAR oficial ANTLR 4.13.2 y, **desde `dsl/`**, ejecute:

```sh
java -jar /ruta/antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated Geometria.g4
```

No se incluye el JAR ni el runtime en el paquete. La gramática y las reglas semánticas se explican en [DSL.md](docs/DSL.md). Referencias técnicas: [descarga oficial ANTLR](https://www.antlr.org/download) y [documentación del objetivo Python](https://github.com/antlr/antlr4/blob/dev/doc/python-target.md).

## Lectura de la actividad

1. [Contrato y decisiones](docs/CONTRATO.md).
2. [Fundamento y demostración matemática](docs/FUNDAMENTOS.md).
3. [Cinco principios SOLID y aceptación](docs/SOLID.md).
4. [Especificación DSL](docs/DSL.md).
5. [Verificación real y pendientes del entorno](docs/VERIFICACION.md).
6. [Trazabilidad de la imagen a los entregables](docs/TRAZABILIDAD.md).

