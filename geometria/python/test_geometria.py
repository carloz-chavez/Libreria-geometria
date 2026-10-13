import json
import unittest
from pathlib import Path
from geometria import Punto, area_poligono, area_firmada, Cordon, Abanico, ServicioArea

CASOS = json.loads((Path(__file__).resolve().parents[1]/"tests/casos.json").read_text())
class PruebasArea(unittest.TestCase):
    def test_casos_y_sustitucion(self):
        for caso in CASOS:
            puntos = [Punto(*p) for p in caso["puntos"]]
            for motor in (Cordon(), Abanico()):
                with self.subTest(caso=caso["nombre"], motor=type(motor).__name__):
                    self.assertAlmostEqual(ServicioArea(motor).ejecutar(puntos),caso["area"])
    def test_invalidos(self):
        for motor in (Cordon(), Abanico()):
            for puntos in ([], [Punto(0,0)]*2, [Punto(0,0),Punto(1,0),Punto(float('nan'),1)],
                           [Punto(0,0),Punto(1,0),Punto(1,float('inf'))],
                           [Punto(0,0),Punto(1e308,0),Punto(0,1e308)]):
                with self.assertRaises(ValueError): motor.calcular(puntos)
    def test_orientacion_traslacion_escala(self):
        p=[Punto(0,0),Punto(4,0),Punto(0,3)]
        self.assertEqual(area_firmada(p),-area_firmada(p[::-1]))
        self.assertEqual(area_poligono([Punto(q.x+1e9,q.y-1e9) for q in p]),6)
        self.assertEqual(area_poligono([Punto(q.x*2,q.y*2) for q in p]),24)
    def test_inyeccion_sin_herencia(self):
        class Doble:
            def calcular(self, puntos): return 42.0
        self.assertEqual(ServicioArea(Doble()).ejecutar([]),42)

if __name__ == '__main__': unittest.main()
