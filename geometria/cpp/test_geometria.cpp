#include "geometria.hpp"
#include <iostream>
#include <limits>
using namespace geometria;
#define CHECK(c) do { if (!(c)) { std::cerr<<"Fallo línea "<<__LINE__<<"\n"; return 1; } } while(0)
int main() {
CHECK(std::abs(areaPoligono({{0,0},{4,0},{4,3},{0,3}})-12)<1e-9);
CHECK(std::abs(areaPoligono({{0,3},{4,3},{4,0},{0,0}})-12)<1e-9);
CHECK(std::abs(areaPoligono({{0,0},{4,0},{0,3}})-6)<1e-9);
CHECK(std::abs(areaPoligono({{0,0},{4,0},{4,4},{2,2},{0,4}})-12)<1e-9);
CHECK(std::abs(areaPoligono({{-3,-2},{1,-2},{1,1},{-3,1}})-12)<1e-9);
CHECK(std::abs(areaPoligono({{0,0},{1,1},{2,2}})-0)<1e-9);
CHECK(std::abs(areaPoligono({{0,0},{4,0},{0,3},{0,0}})-6)<1e-9);
CHECK(std::abs(areaPoligono({{0,0},{0.5,0},{0,0.5}})-0.125)<1e-9);

for (auto p:std::vector<std::vector<Punto>>{{},{{0,0},{1,0}},{{0,0},{1,0},{NAN,1}},{{0,0},{1,0},{INFINITY,1}},{{0,0},{1e308,0},{0,1e308}}}) {
 bool fallo=false; try { areaPoligono(p); } catch(const std::exception&) { fallo=true; } CHECK(fallo);
}
CHECK(areaFirmada({{0,0},{4,0},{0,3}})==-areaFirmada({{0,3},{4,0},{0,0}}));
CHECK(areaPoligono({{1e9,-1e9},{1e9+4,-1e9},{1e9,-1e9+3}})==6);
CHECK(areaPoligono({{0,0},{8,0},{0,6}})==24);
std::cout<<"C++: todas las pruebas pasan\n";
}
