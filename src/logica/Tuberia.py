class Tuberia:

    """ Representacion logica de una tuberia. Obstaculo que el usuario ha de evitar."""

    def __init__(self, geometria):
        self.geometria = geometria
        self.velocidadX = -2

    def mover(self):
        """ Las tuberias se mueven con velocidad constante izquierda a derecha de la pantalla """
        self.geometria.posicion.X += self.velocidadX