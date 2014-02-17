import random
from logica.Jugador import  Jugador
from logica.Tuberia import Tuberia
from fisica.Rectangulo import Rectangulo
from fisica.Punto import Punto


class Partida:

    """ Clase encargada de controlar una partida, creando y moviendo el jugador y las tuberias. Ademas de determinar cuando el jugador ha perdido por haber chocada o cuantos puntos lleva. """

    def __init__(self):
        self.puntos = 0
        self.terminada = False
        self.jugador = Jugador()
        self.tuberias = self.generarParTuberia()



    def generarParTuberia(self):
        """ Genera aleatoriamente una pareja de tuberias, una superior y otra inferior"""
        aleatorio = random.randint(1,3)
        if aleatorio == 1:
            return [Tuberia(Rectangulo(Punto(1000,0), 100, 50)), Tuberia(Rectangulo(Punto(1000,200), 100, 300))]
        elif aleatorio == 2:
            return [Tuberia(Rectangulo(Punto(1000,0), 100, 175)), Tuberia(Rectangulo(Punto(1000,325), 100, 175))]
        else:
            return [Tuberia(Rectangulo(Punto(1000,0), 100, 250)), Tuberia(Rectangulo(Punto(1000,400), 100, 100))]


    def step(self, impulso):

        """ Paso logico del juego que se produce en cada iteracion del bucle principal. Delega en el resto de objetos logicos de 'Partida' sus movimientos """

        # Los puntos son el total de pares de tuberias que el jugador a sobrepasado
        self.puntos = int (len ([x for x in self.tuberias if x.geometria.posicion.X < self.jugador.geometria.Centro.X]) / 2)

        if not self.jugador.muerto: #Si el jugador no ha muerto ejecutamos la logica normal (impulsos, tuberias, colisiones, etc)
            if impulso:
                self.jugador.impulsar()
            self.jugador.aplicar_gravedad()
            self.jugador.mover()
            for tuberia in self.tuberias:
                tuberia.mover()

            for tuberia in self.tuberias:
                if self.jugador.colisiona(tuberia):
                    self.jugador.muerto = True
                    break

            if self.tuberias[-1].geometria.posicion.X < 700:
                self.tuberias += self.generarParTuberia()

        else: #Si el jugador ha muerto paramos toda la logica y solo aplicamos la gravedad para que caiga al suelo y una vez en el suelo terminamos la partida
            self.jugador.aplicar_gravedad()
            self.jugador.mover()
            if self.jugador.tocaTierra:
                self.terminada = True