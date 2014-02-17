from fisica.Punto import Punto
class Rectangulo:

    """ Representa un rectangulo en un mundo 2D """
    def __init__(self, posicion, ancho, alto):
        """ Posicion es el punto mas cercano al eje de coordenadas, ancho la longitud en X y alto la longitud en Y """
        self.posicion, self.Ancho, self.Alto = posicion, ancho, alto

    def Punto0 (self):
        return self.posicion

    def Punto1 (self):
        return Punto(self.posicion.X + self.Ancho, self.posicion.Y)

    def Punto2 (self):
        return Punto(self.posicion.X, self.posicion.Y + self.Alto)

    def Punto3 (self):
        return Punto(self.posicion.X + self.Ancho, self.posicion.Y + self.Alto)