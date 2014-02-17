import pygame
from aplicacion.EstadoInicial import EstadoInicial
from grafico.Graficos import Graficos

class WekyBird:

    """ Clase que gestiona toda la aplicacion. Inicializa el motor pygame, los graficos y el primer estado. Contiene el bucle principal  """

    def __init__(self):
        pygame.init()
        self.graficos = Graficos()
        self.estado = EstadoInicial(self.graficos)
        # Nos permite controlar la velocidad del bucle principal
        clock = pygame.time.Clock()

        while not self.estado.done:
            eventos = pygame.event.get()
            self.estado = self.estado.step(eventos)
            pygame.display.flip()
            clock.tick(120)
        pygame.quit()