# Relación entre imagen y entregables

| Texto visible | Desarrollo |
|---|---|
| 3. Implementación: C/C++, Python, PHP, Javascript, Java, Go, Rust | Bibliotecas y suites en sus ocho carpetas (C y C++ separados) |
| 4. Especificación DSL (ANTLR-Gramática g4) | `dsl/Geometria.g4`, documentación semántica, parser generado y consumidor Python |
| 4. Pruebas Unitarias | Suites en cada lenguaje, vectores comunes y script de verificación |
| 5. Implementar la librería “geometria” | APIs reutilizables con contrato de `AreaPoligono` |
| 5. Prueba de aceptación: Principios SOLID / Fundamentación Teórica | `docs/SOLID.md` y `docs/FUNDAMENTOS.md` |
| Demostración: subrutinas implementadas en Algoritmo AreaPoligono | `validar`, `area_firmada`, `area_poligono`, estrategias y servicio en Python; demo y pruebas |
| Nota de devolver soluciones a una dirección de correo | Paquete local preparado; no se ha enviado correo |

La imagen está copiada en `actividad.png`. El contenido de los puntos 1 y 2 es desconocido. El contrato de geometría plana, los nombres de API, el comportamiento de errores, el formato DSL, las versiones elegidas y la estrategia concreta de SOLID son supuestos explícitos en el README. Se pueden revisar al obtener la parte faltante, sin atribuirlos a la imagen.
