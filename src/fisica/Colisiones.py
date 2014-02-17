import math
from fisica.Punto import Punto


class Colisiones:

    """ Calcula algunas colisiones basicas entre objetos 2D """

    def _init_(self, mundo):
        self.Mundo = mundo

    def ColisionCirculoRectangulo(self, circulo, rectangulo):
        """ Comprueba si un circulo colisiona con un rectangulo. No funciona con rectangulos rotados."""
        return self.CirculoEnRectangulo(circulo, rectangulo) or \
            self.PuntoEnCirculo(rectangulo.Punto0(), circulo) or \
            self.PuntoEnCirculo(rectangulo.Punto1(), circulo) or \
            self.PuntoEnCirculo(rectangulo.Punto2(), circulo) or \
            self.PuntoEnCirculo(rectangulo.Punto3(), circulo) or \
            self.PuntoEnRectangulo(Punto(circulo.Centro.X + circulo.Radio, circulo.Centro.Y), rectangulo ) or \
            self.PuntoEnRectangulo(Punto(circulo.Centro.X, circulo.Centro.Y + circulo.Radio), rectangulo ) or \
            self.PuntoEnRectangulo(Punto(circulo.Centro.X - circulo.Radio, circulo.Centro.Y), rectangulo ) or \
            self.PuntoEnRectangulo(Punto(circulo.Centro.X, circulo.Centro.Y - circulo.Radio), rectangulo )

    def CirculoEnRectangulo(self, circulo, rectangulo):
        """ Determina si el centro de un circulo esta dentro de un rectangulo. No funciona con rectangulos rotados."""
        return self.PuntoEnRectangulo(circulo.Centro, rectangulo)

    def PuntoEnRectangulo(self, punto, rectangulo):
        """ Determina si un punto esta dentro de un rectangulo. No funciona con rectangulos rotados"""
        return punto.X >= rectangulo.posicion.X and punto.X <= rectangulo.posicion.X + rectangulo.Ancho and punto.Y >= rectangulo.posicion.Y and punto.Y <= rectangulo.posicion.Y + rectangulo.Alto

    def PuntoEnCirculo (self, punto, circulo):
        """ Determina si un punto esta dentro de un circulo """
        return self.Distancia (punto, circulo.Centro) < circulo.Radio

    def Distancia(self, punto1, punto2):
        """ Calcula la distancia entre dos puntos en un espacio 2D"""
        r1, r2 = punto2.X - punto1.X, punto2.Y - punto1.Y
        p1, p2 = r1**2, r2**2
        return math.sqrt(p1+p2)