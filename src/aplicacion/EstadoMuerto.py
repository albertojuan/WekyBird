from aplicacion.EstadoTerminar import EstadoTerminar
from aplicacion.EstadoJugar import EstadoJugar
import pygame


class EstadoMuerto:

    ''' Estado a la espera de que el jugador quiera iniciar una nueva partida despues de haber perdido.'''

    def __init__(self, grafico):
        self.done = False
        self.graficos = grafico
        self.graficos.pintarGameOver()

    def step(self, eventos):
        for evento in eventos: # User did something
            if evento.type == pygame.QUIT: # If user clicked close
                return EstadoTerminar() # Flag that we are done so we exit this loop
            elif evento.type == pygame.MOUSEBUTTONUP:
                return EstadoJugar(self.graficos)

        return self