from aplicacion.EstadoTerminar import EstadoTerminar
from aplicacion.EstadoJugar import EstadoJugar
import pygame

class EstadoInicial:

    """ Primer estado del juego. Muestra el cartel de bienvenida """

    def __init__(self, grafico):
        self.graficos = grafico
        self.done = False

    def step(self, eventos):
        self.graficos.pintarGetReady()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                return EstadoTerminar()
            elif evento.type == pygame.MOUSEBUTTONUP:
                return EstadoJugar(self.graficos)
        return self