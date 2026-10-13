# Especificación DSL

Archivo normativo de sintaxis: `dsl/Geometria.g4`, ANTLR4. La sintaxis concreta es una propuesta de esta entrega, no un requisito recuperado de los puntos ausentes.

## Léxico y gramática

Se usan las palabras reservadas `poligono` y `area`, identificadores ASCII que comienzan por letra o `_`, números decimales con signo opcional y exponente opcional, separadores `= [ ] ( ) , ;`. Los comentarios `//` llegan al final de la línea; espacios y saltos se ignoran. No hay cadenas, expresiones aritméticas ni coma decimal. `NaN` e `Infinity` no son números del DSL.

```text
programa    = { declaracion | consulta } EOF
declaracion = "poligono" ID "=" "[" punto "," punto "," punto { "," punto } "]" ";"
consulta    = "area" "(" ID ")" ";"
punto       = "(" numero "," numero ")"
```

La gramática exige al menos tres puntos; consume EOF, de modo que no acepta texto residual. Ejemplos de números: `-2`, `+.5`, `4.`, `1e-3`. Los identificadores distinguen mayúsculas. Las palabras reservadas no pueden usarse como nombres.

## Semántica

El consumidor procesa sentencias secuencialmente. Una declaración guarda una lista de puntos en una tabla de símbolos. No se permiten nombres duplicados ni consulta antes de declarar. Un programa vacío es válido y no produce salida. Una declaración sin consulta no imprime nada.

Las coordenadas se convierten a `float` y la biblioteca valida finitud y desbordamiento al declarar. Por ejemplo, `1e999` cumple la forma léxica de un número, pero se rechaza semánticamente por no ser representable como valor finito. La simpleza del contorno sigue siendo una precondición del llamador; el parser no detecta intersecciones.

`area(nombre);` añade el par `(nombre, área)` a los resultados de `evaluar`. El programa de consola imprime un resultado por línea. Primero se analiza todo el programa, y después se evalúa en memoria; si hay error, la función no devuelve una lista parcial y el programa de consola no imprime resultados parciales. Los errores de sintaxis incluyen línea/columna; los semánticos incluyen el nombre cuando corresponde. Fallos de archivo se reportan por el mecanismo normal de Python.

## Generación y ejecución

La entrega incluye los archivos generados en `dsl/generated/`. No están escritos a mano. El intérprete importa `GeometriaLexer` y `GeometriaParser` y recorre los contextos de su árbol; no usa un parser de sustitución por expresiones regulares. Se verifica con generador/runtime **4.13.2**, fijados para reproducibilidad.

Desde `dsl/`:

```sh
java -jar /ruta/antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated Geometria.g4
```

Desde la raíz:

```sh
python -m pip install -r dsl/requirements.txt
python dsl/ejecutar.py dsl/ejemplo.geo
python -m unittest discover -s dsl -v
```

Las tres pruebas cubren el ejemplo de dos polígonos, signos/exponentes/comentarios y seis entradas erróneas: nombre desconocido, menos de tres puntos, nombre repetido, número no finito, falta de `;` y carácter ilegal. La gramática no necesita generar un parser en los ocho lenguajes para cumplir el alcance adoptado.
