"""Aceptación ejecutable de las decisiones SOLID explicadas en docs/SOLID.md."""
from geometria import Punto, validar, area_firmada, Cordon, Abanico, ServicioArea

def main():
    puntos = [Punto(0,0), Punto(4,0), Punto(4,4), Punto(2,2), Punto(0,4)]
    validar(puntos)
    assert area_firmada(puntos) == 12
    print('SRP: validación y cálculo pueden usarse sin lectura ni impresión.')
    for estrategia in (Cordon(), Abanico()):
        assert ServicioArea(estrategia).ejecutar(puntos) == 12
    print('OCP: Abanico amplía el cálculo sin cambiar ServicioArea.')
    for estrategia in (Cordon(), Abanico()):
        assert estrategia.calcular(puntos[::-1]) == 12
        try:
            estrategia.calcular(puntos[:2])
        except ValueError:
            pass
        else:
            raise AssertionError('Contrato de error incumplido')
    print('LSP: ambas estrategias conservan resultados y precondiciones.')
    class SoloCalculo:
        def calcular(self, puntos):
            return Cordon().calcular(puntos)
    assert ServicioArea(SoloCalculo()).ejecutar(puntos) == 12
    print('ISP: el cliente solo necesita calcular; no necesita imprimir ni guardar.')
    class Doble:
        def calcular(self, puntos):
            return 42.0
    assert ServicioArea(Doble()).ejecutar(puntos) == 42
    print('DIP: el servicio recibe su dependencia y admite un doble para aislarlo.')

if __name__ == '__main__':
    main()
