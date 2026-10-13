#ifndef GEOMETRIA_H
#define GEOMETRIA_H
#include <stddef.h>
typedef struct { double x, y; } Punto;
typedef enum { GEO_OK=0, GEO_ARGUMENTO=1, GEO_DESBORDAMIENTO=2 } GeoEstado;
/* Salida solo se modifica en caso de éxito. */
GeoEstado area_firmada(const Punto *p, size_t n, double *salida);
GeoEstado area_poligono(const Punto *p, size_t n, double *salida);
#endif
