import pygame
from aplicacion.EstadoTerminar import EstadoTerminar
from aplicacion.EstadoJugar import EstadoJugar


class EstadoPause:

    """ Estado que para la logica y el pintado de graficos hasta que se pulse una tecla o se haga click """

    def __init__(self, grafico, partida):
        self.done = False
        self.graficos = grafico
        self.graficos.pintarPause()
        self.partida = partida

    def step(self, eventos):
        for evento in eventos: # User did something
            if evento.type == pygame.QUIT: # If user clicked close
                return EstadoTerminar() # Flag that we are done so we exit this loop
            elif evento.type == pygame.MOUSEBUTTONUP or evento.type == pygame.KEYUP:
                return EstadoJugar(self.graficos, self.partida)
        return self
