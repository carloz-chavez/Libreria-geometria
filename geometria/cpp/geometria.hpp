#ifndef GEOMETRIA_HPP
#define GEOMETRIA_HPP
#include <vector>
#include <cmath>
#include <stdexcept>
namespace geometria {
struct Punto { double x, y; };
inline double areaFirmada(const std::vector<Punto>& p) {
    if (p.size()<3) throw std::invalid_argument("Se requieren tres puntos");
    for (const auto& q:p) if (!std::isfinite(q.x)||!std::isfinite(q.y))
        throw std::invalid_argument("Coordenadas no finitas");
    double suma=0;
    for (std::size_t i=0;i<p.size();++i) {
        const auto& a=p[i]; const auto& b=p[(i+1)%p.size()];
        suma+=(a.x-p[0].x)*(b.y-p[0].y)-(b.x-p[0].x)*(a.y-p[0].y);
    }
    double resultado=suma/2;
    if (!std::isfinite(resultado)) throw std::overflow_error("Desbordamiento numérico");
    return resultado;
}
inline double areaPoligono(const std::vector<Punto>& p) { return std::abs(areaFirmada(p)); }
}
#endif
