import unittest
from pathlib import Path
from ejecutar import evaluar
class PruebasDSL(unittest.TestCase):
    def test_ejemplo(self):
        self.assertEqual(evaluar(Path(__file__).with_name('ejemplo.geo').read_text()),[('parcela',12),('triangulo',.125)])
    def test_signos_y_comentarios(self):
        self.assertEqual(evaluar('// hola\npoligono p=[(-1,+0),(1,0),(0,2)]; area(p);'),[('p',2)])
    def test_errores(self):
        for texto in ('area(x);','poligono p=[(0,0),(1,1)];',
                      'poligono p=[(0,0),(1,0),(0,1)]; poligono p=[(0,0),(1,0),(0,1)];',
                      'poligono p=[(0,0),(1e999,0),(0,1)];',
                      'poligono p=[(0,0),(1,0),(0,1)]', '@'):
            with self.subTest(texto=texto), self.assertRaises(ValueError): evaluar(texto)
if __name__=='__main__': unittest.main()
