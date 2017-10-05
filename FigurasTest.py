# !/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from figuras import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figura = Figuras()

# Pruebas con cuadrados
    def test_area_cuadrado_lado_5(self):
        resultado = self.figura.cuadrado(5)
        self.assertEquals(25, resultado)

    def test_area_cuadrado_lado_8(self):
        resultado = self.figura.cuadrado(8)
        self.assertEquals(64, resultado)

    def test_area_cuadrado_lado_0(self):
        resultado = self.figura.cuadrado(0)
        self.assertEquals('No se aceptan 0s', resultado)

    def test_area_cuadrado_lado_X(self):
        resultado = self.figura.cuadrado('x')
        self.assertEquals('Dato Incorrecto', resultado)

# Pruebas con circulos
    def test_area_circulo_radio_3(self):
        resultado = self.figura.circulo(3)
        self.assertEquals(28.27, resultado)

    def test_area_circulo_radio_5(self):
        resultado = self.figura.circulo(5)
        self.assertEquals(78.54, resultado)

    def test_area_circulo_radio_0(self):
        resultado = self.figura.circulo(0)
        self.assertEquals('No se aceptan 0s', resultado)

    def test_area_circulo_radio_x(self):
        resultado = self.figura.circulo('x')
        self.assertEquals('Dato Incorrecto', resultado)

# Pruebas con triangulo
    def test_area_triangulo_base_4_altura_5(self):
        resultado = self.figura.triangulo(4, 5)
        self.assertEquals(10, resultado)

    def test_area_triangulo_base_4_altura_8(self):
        resultado = self.figura.triangulo(4, 8)
        self.assertEquals(16, resultado)

    def test_area_triangulo_base_4_altura_0(self):
        resultado = self.figura.triangulo(4, 0)
        self.assertEquals('No se aceptan 0s', resultado)

    def test_area_triangulo_base_4_altura_x(self):
        resultado = self.figura.triangulo(4, 'x')
        self.assertEquals('Dato Incorrecto', resultado)

# Pruebas con trapecio
    def test_area_trapecio_baseMayor_6_baseMenor_4_altura_4(self):
        resultado = self.figura.trapecio(6, 4, 4)
        self.assertEquals(20, resultado)

    def test_area_trapecio_baseMayor_6_baseMenor_4_altura_8(self):
        resultado = self.figura.trapecio(6, 4, 8)
        self.assertEquals(40, resultado)

    def test_area_trapecio_baseMayor_6_baseMenor_4_altura_0(self):
        resultado = self.figura.trapecio(6, 4, 0)
        self.assertEquals('No se aceptan 0s', resultado)

    def test_area_trapecio_baseMayor_6_baseMenor_4_altura_x(self):
        resultado = self.figura.trapecio(6, 4, 'x')
        self.assertEquals('Dato Incorrecto', resultado)


if __name__ == '__main__':
    unittest.main()
