from fisica.Circulo import Circulo
from fisica.Colisiones import  Colisiones
from fisica.Punto import Punto

class Jugador:

    """ Persona principal que va esquivando los obstaculos"""

    IMPULSO = -4 # Velocidad del personaje en el eje que se le aplica cuando hacemos que se impulse
    GRAVEDAD_Y = 0.15 # Incremento constante de la gravedad que va sufriendo el personaje
    VY_MAX = 8 # Cuando la gravedad hace que la velocidad de caida sea mayor a VY_MAX deja de incrementarse


    def __init__(self):
        self.muerto = False
        self.velocidadY = Jugador.IMPULSO

        self.geometria = Circulo(Punto(100,200), 30) # Se asigna el objeto fisico circulo al jugador para conocer su posicion y calcular sus colisiones
        self.motorColisiones = Colisiones()
        self.tocaTierra = False

    def impulsar(self):
        self.velocidadY = Jugador.IMPULSO

    def aplicar_gravedad(self):
        if self.velocidadY < Jugador.VY_MAX:
            self.velocidadY += Jugador.GRAVEDAD_Y

    def mover(self):

        self.geometria.Centro.Y += self.velocidadY
        if self.geometria.Centro.Y + self.geometria.Radio > 450: #Si el jugador esta a esta altura ha chocado contra el suelo
            self.velocidadY = 0
            self.geometria.Centro.Y = 450 - self.geometria.Radio
            self.tocaTierra = True
            self.muerto = True
        else:
            self.tocaTierra = False


        if self.geometria.Centro.Y - self.geometria.Radio < 0:
            self.velocidadY = 0
            self.geometria.Centro.Y = self.geometria.Radio


    def colisiona(self, tuberia):
        return self.motorColisiones.ColisionCirculoRectangulo(self.geometria, tuberia.geometria)