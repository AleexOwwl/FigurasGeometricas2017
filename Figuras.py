# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Figuras:

    def circulo(self, radio):

        try:
            if radio <= 0:
                return 'No se aceptan 0s'

            else:
                pi = 3.1416
                radio = int(radio)
                area = pi * (radio**2)
                area = round(area, 2)
                return area

        except:
            return 'Dato Incorrecto'

    def triangulo(self, base, altura):

        try:

            if altura <= 0 or base <= 0:
                return 'No se aceptan 0s'

            else:
                base = int(base)
                altura = int(altura)
                area = (base * altura) / 2
                return area

        except:
            return 'Dato Incorrecto'

    def cuadrado(self, lado):

        try:

            if lado <= 0:
                return 'No se aceptan 0s'

            else:
                lado = int(lado)
                return lado * lado

        except:
            return 'Dato Incorrecto'

    def trapecio(self, baseMay, baseMen, altura):

        try:

            if baseMay <= 0 or baseMen <= 0 or altura <= 0:
                return 'No se aceptan 0s'

            else:
                baseMay = int(baseMay)
                baseMen = int(baseMen)
                altura = int(altura)
                area = (baseMay + baseMen) / 2 * altura
                return area

        except:
            return 'Dato Incorrecto'
