import pygame
import os

from grafico.SueloGrafico import SueloGrafico
from grafico.JugadorGrafico import JugadorGrafico
from grafico.TuberiaGrafica import TuberiaGrafica



class Graficos:

    """ Clase que mediante el uso del motor pygame se ocupa del renderizado del juego"""
    # Definimos algunos colores como constantes
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)

    # Cargamos las imagenes del juego
    JUGADOR = pygame.image.load(os.path.join('data', 'wekky.png'))
    TUBERIA = pygame.image.load(os.path.join('data', 'tuberia.png'))
    FONDO = pygame.image.load(os.path.join('data', 'fondo.png'))
    SUELO = pygame.image.load(os.path.join('data', 'suelo.png'))
    GETREADY = pygame.image.load(os.path.join('data', 'getready.png'))
    PAUSE = pygame.image.load(os.path.join('data', 'pause.png'))
    GAMEOVER = pygame.image.load(os.path.join('data', 'gameover.png'))

    def __init__(self):
        self.size = (1000, 500)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(Graficos.BLACK)
        pygame.display.set_caption("Weky Bird")
        self.jugadorGrafico = None
        self.tuberiasGraficas = None
        self.puntuacion = 0
        self.partida = None
        self.suelos = [ SueloGrafico(self, 0), SueloGrafico(self, 1204) ]

    def cargar_partida(self, partida):
        """ Metodo para reiniciar los objetos graficos que dependen del estado de la partida """
        self.jugadorGrafico = JugadorGrafico(partida.jugador, self)
        self.partida = partida
        self.suelos = [ SueloGrafico(self, 0), SueloGrafico(self, 1204) ]
        # Seleccionamos todas las tuberias que sean visibles
        self.tuberiasGraficas = [TuberiaGrafica(x, self) for x in self.partida.tuberias if x.geometria.posicion.X > -200]

    def pintar(self):
        """ Renderiza los graficos. Delega la responsabilidad de pintarse al resto de objetos graficos contenidos en la clase """

        if self.partida: # Si hay una partida en ejecucion hay que pintar tuberias, seleccionamos las que esten visibles
            self.tuberiasGraficas = [TuberiaGrafica(x, self) for x in self.partida.tuberias if x.geometria.posicion.X > -200]

        self.screen.fill(Graficos.BLACK)
        self.screen.blit(Graficos.FONDO, (0,0))

        if self.tuberiasGraficas:
            for tuberiaGrafica in self.tuberiasGraficas:
                tuberiaGrafica.pintar()

        if self.suelos: #Para crear una animacion infinita de suelo moviendose utilizamos dos imagenes de suelo que desplazamos por la pantalla
            for suelo in self.suelos:
                suelo.pintar(not self.partida or self.partida.jugador.muerto)

        if self.jugadorGrafico:
            self.jugadorGrafico.pintar()

        self.pintarPuntuacion()

    def pintarGetReady(self):
        self.screen.blit(self.GETREADY, [325,200])

    def pintarPause(self):
        self.screen.blit(self.PAUSE, [400,150])

    def pintarGameOver(self):
        self.screen.blit(self.GAMEOVER, [325,200])

    def pintarPuntuacion(self):
        self.font = pygame.font.Font(None, 25)
        text = self.font.render("Puntos: " + str(self.puntuacion),True, Graficos.WHITE)
        self.screen.blit(text, [800,50])