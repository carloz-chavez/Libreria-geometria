# Contrato de AreaPoligono

## Entrada

Una secuencia de al menos tres puntos con coordenadas reales finitas representables en doble precisión. Los puntos se entregan en orden consecutivo del contorno, horario o antihorario. Se cierra el recorrido internamente conectando el último punto con el primero. También se acepta un último punto repetido igual al primero.

El llamador garantiza que el polígono sea simple y sin agujeros. La implementación **no comprueba intersecciones ni ordena vértices**. La secuencia de puntos colineales se acepta como caso degenerado con área cero; no se exige que todos los puntos sean distintos. Estas decisiones son supuestos de diseño porque los puntos 1 y 2 faltan.

La entrada no se modifica. En C el llamador debe proporcionar un arreglo válido de `n` elementos y memoria de salida independiente de ese arreglo. Las APIs tipadas esperan los tipos declarados; en Python no se promete convertir cadenas ni objetos arbitrarios a puntos.

## Salida y errores

El área es no negativa y está expresada en unidades cuadradas. La subrutina auxiliar de área firmada devuelve valor positivo con recorrido antihorario y negativo con recorrido horario en un plano cartesiano convencional. Invertir un contorno degenerado mantiene cero.

| Lenguaje | Área absoluta / firmada | Error de entrada o rango |
|---|---|---|
| C | `area_poligono` / `area_firmada` | `GEO_ARGUMENTO`, `GEO_DESBORDAMIENTO`; salida solo escrita con `GEO_OK` |
| C++ | `geometria::areaPoligono` / `areaFirmada` | `invalid_argument`, `overflow_error` |
| Python | `area_poligono` / `area_firmada` | `ValueError` |
| PHP | `Geometria\\areaPoligono` / `areaFirmada` | `InvalidArgumentException`, `OverflowException` |
| JavaScript | `areaPoligono` / `areaFirmada` | `RangeError` o `TypeError` |
| Java | `Geometria.areaPoligono` / `areaFirmada` | `IllegalArgumentException`, `ArithmeticException` |
| Go | `AreaPoligono` / `AreaFirmada` | `(0,error)`; éxito `(area,nil)` |
| Rust | `area_poligono` / `area_firmada` | `Result<f64, ErrorArea>` |

Se rechazan menos de tres puntos, NaN e infinito. Los productos o sumas que terminan en un resultado no finito producen error de desbordamiento. No se detecta subdesbordamiento a cero ni toda pérdida de precisión finita.

## Límites numéricos y geométricos

Se traduce cada coordenada restando el primer vértice para reducir cancelación con desplazamientos grandes. Esto no recupera bits ya perdidos al representar las coordenadas ni sustituye predicados geométricos exactos. Las comparaciones generales de pruebas usan tolerancia absoluta `1e-9` en los casos de escala pequeña provistos; no es una tolerancia universal para cualquier magnitud.

Un contorno cruzado puede producir cero aun encerrando regiones visibles: el resultado del cordón sería área algebraica, fuera del contrato de área geométrica elegido. Para agujeros habría que sumar contornos con orientación definida y diseñar otra API. Coordenadas geográficas longitud/latitud necesitarían proyección o geometría esférica: no están cubiertas.

## Casos de referencia

`tests/casos.json` documenta ocho ejemplos: rectángulo (4×3, área 12), orden inverso (12), triángulo (6), cóncavo (12), coordenadas negativas (12), colineal (0), cierre explícito (6) y fraccionario (0.125). Las suites C/C++, Java, PHP, Go y Rust contienen esos mismos vectores como literales para evitar dependencias JSON; Python y JavaScript leen directamente el archivo.

Cada lenguaje también comprueba entradas inválidas, NaN, infinito, desbordamiento, inversión de orientación, traslación y escalado. El área de un polígono escalado por factor k debe multiplicarse por k².
