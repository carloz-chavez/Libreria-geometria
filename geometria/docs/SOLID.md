# Fundamentación y aceptación SOLID

Los cinco principios orientan la organización y las dependencias; no son propiedades de la fórmula geométrica. La demostración se concentra en `python/geometria.py` para poder observar cada decisión en código ejecutable. El resto de las bibliotecas conserva la API matemática común sin introducir jerarquías artificiales.

## S: responsabilidad única (SRP)

Una responsabilidad agrupa decisiones que cambian por una misma causa. En este proyecto, `validar` controla la política de entrada; `area_firmada` recorre el contorno; `area_poligono` convierte al valor absoluto; `ServicioArea` delega; el consumidor DSL interpreta nombres y `demo_solid.py` presenta resultados. La biblioteca no depende de consola, archivos ni ANTLR. Si cambia la sintaxis del DSL, el cálculo no cambia.

La separación se puede observar ejecutando `validar(puntos)` y `area_firmada(puntos)` sin ninguna entrada/salida. El hecho de que una función llame a la validación no le añade la responsabilidad de interpretar archivos. Un contraejemplo sería leer un archivo, interpretar su formato, calcular y enviar un correo dentro de `area_poligono`.

## O: abierto/cerrado (OCP)

Se define un punto de extensión concreto: la estrategia de cálculo que recibe el servicio. `Cordon.calcular` usa la suma de aristas; `Abanico.calcular` usa triángulos firmados. Se añade la segunda clase sin cambiar `ServicioArea.ejecutar` ni agregar un `if` por cada motor.

```python
ServicioArea(Cordon()).ejecutar(puntos)
ServicioArea(Abanico()).ejecutar(puntos)
```

Esta apertura tiene un alcance: nuevas estrategias que respeten `CalculadorArea`. Una nueva entrada con agujeros requeriría reconsiderar el contrato; OCP no prohíbe corregir requisitos o defectos.

## L: sustitución de Liskov (LSP)

Una implementación sustituible conserva el contrato observable: acepta polígonos simples cóncavos o convexos con al menos tres puntos finitos, devuelve área no negativa independiente del sentido del recorrido y rechaza cardinalidad insuficiente o resultados no finitos con `ValueError`. Ninguna estrategia impone convexidad adicional, modifica puntos ni devuelve área firmada como resultado final.

`test_casos_y_sustitucion` ejecuta los ocho vectores a través de `ServicioArea` con ambos motores, y `test_invalidos` comprueba las mismas excepciones. `demo_solid.py` verifica orientación y rechazo de dos puntos con ambos. Las pruebas son evidencia de sustitución en esos casos, no una prueba universal para todos los números flotantes; la identidad algebraica del documento matemático justifica la equivalencia ideal. En extremos de precisión puede haber redondeos distintos.

Un motor que solo acepte polígonos convexos o sume valores absolutos por triángulo violaría este contrato. El doble que devuelve 42 se usa exclusivamente para probar la delegación, no se presenta como un motor geométrico válido según LSP.

## I: segregación de interfaces (ISP)

`CalculadorArea` es un `Protocol` con el único método que usa el servicio: `calcular`. No obliga al calculador a exportar JSON, dibujar, imprimir ni guardar. `SoloCalculo` en la demostración satisface la necesidad del cliente con ese único método. En Python el protocolo declara una forma para herramientas de tipado; no realiza validación dinámica automática.

No hace falta inventar interfaces de persistencia no utilizadas. Si se incorporara un exportador, tendría su propio contrato. Un contraejemplo sería exigir `guardar`, `imprimir` y `calcular` en una sola interfaz para clientes que solo necesitan el área.

## D: inversión de dependencias (DIP)

La política de servicio declara dependencia sobre `CalculadorArea`; recibe una instancia por constructor. Las estrategias cumplen ese protocolo por su estructura. La composición concreta ocurre fuera del servicio. `ServicioArea` no crea `Cordon` internamente ni conoce ANTLR.

`test_inyeccion_sin_herencia` y el último paso de la demostración inyectan un doble para verificar la delegación independientemente de la fórmula. Inyección es el mecanismo empleado; el principio es que la política se expresa contra la abstracción que necesita, sin dependencia fija sobre un motor concreto.

## Aceptación ejecutable y trazabilidad

Desde la raíz:

```sh
python python/demo_solid.py
python -m unittest discover -s python -v
```

| Principio | Subrutina o interfaz observable | Evidencia |
|---|---|---|
| SRP | `validar`, `area_firmada`, `area_poligono` | Primer paso del demo; cálculo aislado de DSL/consola |
| OCP | `Abanico.calcular`, `ServicioArea.ejecutar` | Dos motores sin modificar servicio |
| LSP | `Cordon.calcular`, `Abanico.calcular` | Batería contractual y errores con ambos motores |
| ISP | `CalculadorArea.calcular` | Objeto `SoloCalculo` sin métodos de presentación |
| DIP | `ServicioArea.__init__` | Doble inyectado; servicio delega |

La explicación usa formulaciones propias. Referencias primarias para ampliar: [Robert C. Martin, Design Principles and Design Patterns](https://objectmentor.com/resources/articles/Principles_and_Patterns.pdf) (OCP, LSP, ISP y DIP) y [The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) (SRP). Los ejemplos y criterios de aceptación aquí son decisiones del proyecto.
