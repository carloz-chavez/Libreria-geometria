#include "geometria.h"
#include <math.h>
GeoEstado area_firmada(const Punto *p, size_t n, double *salida) {
    if (!p || !salida || n < 3) return GEO_ARGUMENTO;
    for (size_t i=0; i<n; ++i)
        if (!isfinite(p[i].x) || !isfinite(p[i].y)) return GEO_ARGUMENTO;
    double suma=0;
    for (size_t i=0; i<n; ++i) {
        size_t j=(i+1)%n;
        suma+=(p[i].x-p[0].x)*(p[j].y-p[0].y)-(p[j].x-p[0].x)*(p[i].y-p[0].y);
    }
    double resultado=suma/2;
    if (!isfinite(resultado)) return GEO_DESBORDAMIENTO;
    *salida=resultado;
    return GEO_OK;
}
GeoEstado area_poligono(const Punto *p, size_t n, double *salida) {
    double resultado;
    if (!salida) return GEO_ARGUMENTO;
    GeoEstado estado=area_firmada(p,n,&resultado);
    if (estado==GEO_OK) *salida=fabs(resultado);
    return estado;
}
