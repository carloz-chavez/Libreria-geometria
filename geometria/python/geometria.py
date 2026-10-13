"""Área euclídea de polígonos simples; coordenadas finitas, contorno ordenado."""
from dataclasses import dataclass
from math import isfinite
from typing import Protocol, Sequence

@dataclass(frozen=True)
class Punto:
    x: float
    y: float

def validar(puntos: Sequence[Punto]) -> None:
    if len(puntos) < 3:
        raise ValueError("Se requieren al menos tres puntos")
    if any(not isfinite(p.x) or not isfinite(p.y) for p in puntos):
        raise ValueError("Las coordenadas deben ser finitas")

def area_firmada(puntos: Sequence[Punto]) -> float:
    validar(puntos)
    # Trasladar al primer vértice reduce cancelación con grandes desplazamientos.
    origen = puntos[0]
    suma = 0.0
    for i, p in enumerate(puntos):
        q = puntos[(i + 1) % len(puntos)]
        suma += (p.x-origen.x)*(q.y-origen.y)-(q.x-origen.x)*(p.y-origen.y)
    resultado = suma / 2.0
    if not isfinite(resultado):
        raise ValueError("Desbordamiento numérico")
    return resultado

def area_poligono(puntos: Sequence[Punto]) -> float:
    return abs(area_firmada(puntos))

# Interfaces de un único método: el cliente depende del cálculo, no de la técnica.
class CalculadorArea(Protocol):
    def calcular(self, puntos: Sequence[Punto]) -> float: ...

class Cordon:
    def calcular(self, puntos: Sequence[Punto]) -> float:
        return area_poligono(puntos)

class Abanico:
    """Suma firmada de triángulos: también funciona para polígonos cóncavos simples."""
    def calcular(self, puntos: Sequence[Punto]) -> float:
        validar(puntos)
        o = puntos[0]
        total = 0.0
        for i in range(1, len(puntos)-1):
            a, b = puntos[i], puntos[i+1]
            total += (a.x-o.x)*(b.y-o.y)-(b.x-o.x)*(a.y-o.y)
        resultado = abs(total / 2.0)
        if not isfinite(resultado):
            raise ValueError("Desbordamiento numérico")
        return resultado

class ServicioArea:
    def __init__(self, calculador: CalculadorArea):
        self.calculador = calculador
    def ejecutar(self, puntos: Sequence[Punto]) -> float:
        return self.calculador.calcular(puntos)
