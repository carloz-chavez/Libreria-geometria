# Verificación realizada — 13 de octubre de 2026

Entorno Windows del usuario. Se ejecutaron los comandos y pruebas locales; no se presentan compilaciones no realizadas como aprobadas.

| Entregable | Herramienta real | Resultado |
|---|---|---|
| Python | Python 3.12.14 | 4 pruebas unittest aprobadas, con subcasos para los ocho vectores y ambos motores |
| SOLID | Python 3.12.14 | Demostración de los cinco principios ejecutada, todas sus comprobaciones aprobadas |
| JavaScript | Node v24.18.0 | 10 pruebas `node:test` aprobadas |
| Java | Temurin JDK 21.0.12.1 | Compilación aprobada; suite ejecutada con salida exitosa |
| ANTLR | Generador 4.13.2, Java 21 | Gramática procesada sin errores; lexer/parser Python generados |
| DSL | Runtime Python ANTLR 4.13.2 | 3 pruebas unittest aprobadas; ejemplo ejecutado: 12 y 0.125 |
| C | GCC encontrado en `C:\MinGW\bin` | No se pudo arrancar el compilador: WinError 623, conflicto de reasignación de DLL |
| C++ | G++ encontrado en `C:\MinGW\bin` | Misma limitación; no se compiló ni ejecutó la suite |
| PHP | No encontrado en PATH ni en ruta común examinada | Código y suite entregados; no ejecutados |
| Go | No encontrado en PATH ni en ruta común examinada | Código y suite entregados; no ejecutados |
| Rust | Cargo no encontrado en PATH ni en ruta común examinada | Código y suite entregados; no ejecutados |

El fallo de C/C++ sucede antes de que el compilador analice los fuentes. No demuestra un defecto del programa ni permite afirmar que compile. Hace falta ejecutar esas suites con una instalación funcional de GCC/G++ y las otras tres con sus herramientas.

## Evidencia y reproducción

`docs/evidencias/verificacion.json` conserva comandos, códigos de salida, resultados y errores de la ejecución de `tools/verificar.py`. El marcador `FALLA` de C/C++ registra el intento fallido de verificación por entorno. El ejecutor termina con código 1 porque no pudo aprobar todas las suites disponibles; las tres herramientas ausentes se marcan `NO_DISPONIBLE`. Un código global no reemplaza la lectura por lenguaje.

El generador se invocó con:

```sh
java -jar work/antlr-4.13.2-complete.jar -Dlanguage=Python3 -o outputs/geometria/dsl/generated outputs/geometria/dsl/Geometria.g4
```

Terminó con código 0. El runtime se instaló en una carpeta de trabajo aislada, sin cambiar la instalación Python del usuario. Para reproducir en otro equipo use el README, que emplea rutas relativas de la entrega e instalación del runtime en su entorno elegido. El ejemplo DSL produjo:

```text
parcela: 12
triangulo: 0.125
```

Las pruebas cubren área conocida, orientación, concavidad, negativos, degeneración, cierre repetido, decimales, cardinalidad, NaN, infinito, desbordamiento, traslación y escala. No se verificó soporte para agujeros, contornos cruzados ni geometría geográfica porque están fuera del contrato asumido.

## Integridad de la entrega

El ZIP contiene fuentes, pruebas, parser generado, documentación y la imagen de referencia. Excluye compilados, cachés, runtime y JAR descargados. `MANIFEST.sha256` enumera las huellas SHA-256 de sus archivos (excepto el propio manifiesto). La integridad del ZIP y la correspondencia de sus entradas con el manifiesto se comprobaron al empaquetar.
