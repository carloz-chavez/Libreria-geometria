#include "geometria.h"
#include <math.h>
#include <stdio.h>
#define CHECK(c) do { if (!(c)) { fprintf(stderr,"Fallo línea %d\n",__LINE__); return 1; } } while(0)
int main(void) { double a=0,b=0;
Punto p0[]={{0,0},{4,0},{4,3},{0,3}}; CHECK(area_poligono(p0,4,&a)==GEO_OK && fabs(a-12)<1e-9);
Punto p1[]={{0,3},{4,3},{4,0},{0,0}}; CHECK(area_poligono(p1,4,&a)==GEO_OK && fabs(a-12)<1e-9);
Punto p2[]={{0,0},{4,0},{0,3}}; CHECK(area_poligono(p2,3,&a)==GEO_OK && fabs(a-6)<1e-9);
Punto p3[]={{0,0},{4,0},{4,4},{2,2},{0,4}}; CHECK(area_poligono(p3,5,&a)==GEO_OK && fabs(a-12)<1e-9);
Punto p4[]={{-3,-2},{1,-2},{1,1},{-3,1}}; CHECK(area_poligono(p4,4,&a)==GEO_OK && fabs(a-12)<1e-9);
Punto p5[]={{0,0},{1,1},{2,2}}; CHECK(area_poligono(p5,3,&a)==GEO_OK && fabs(a-0)<1e-9);
Punto p6[]={{0,0},{4,0},{0,3},{0,0}}; CHECK(area_poligono(p6,4,&a)==GEO_OK && fabs(a-6)<1e-9);
Punto p7[]={{0,0},{0.5,0},{0,0.5}}; CHECK(area_poligono(p7,3,&a)==GEO_OK && fabs(a-0.125)<1e-9);

Punto invalidos[]={{0,0},{1,0},{NAN,1}};
CHECK(area_poligono(invalidos,3,&a)==GEO_ARGUMENTO);
invalidos[2].x=INFINITY; CHECK(area_poligono(invalidos,3,&a)==GEO_ARGUMENTO);
CHECK(area_poligono(p0,2,&a)==GEO_ARGUMENTO);
CHECK(area_poligono(NULL,3,&a)==GEO_ARGUMENTO);
CHECK(area_poligono(p0,4,NULL)==GEO_ARGUMENTO);
Punto enorme[]={{0,0},{1e308,0},{0,1e308}};
a=99; CHECK(area_poligono(enorme,3,&a)==GEO_DESBORDAMIENTO && a==99);
CHECK(area_firmada(p0,4,&a)==GEO_OK && area_firmada(p1,4,&b)==GEO_OK && a==-b);
Punto trasladado[]={{1e9,-1e9},{1e9+4,-1e9},{1e9,-1e9+3}};
CHECK(area_poligono(trasladado,3,&a)==GEO_OK && a==6);
Punto escalado[]={{0,0},{8,0},{0,6}};
CHECK(area_poligono(escalado,3,&a)==GEO_OK && a==24);
puts("C: todas las pruebas pasan"); return 0;
}
