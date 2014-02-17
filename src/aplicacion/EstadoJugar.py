from logica.Partida import Partida
import pygame

class EstadoJugar:

    ''' Estado que inicializa y gestiona la partida. En este estado estaremos esquivando tuberias.'''

    def __init__(self, grafico,  partida = None):
        self.done = False
        self.graficos = grafico
        self.partida = partida
        if not self.partida:
            self.partida = Partida()
            self.graficos.cargar_partida(self.partida)


    def step(self, eventos):
        self.graficos.pintar()
        self.graficos.puntuacion = self.partida.puntos
        evento_impulso = False

        for evento in eventos:
            if evento.type == pygame.QUIT:
                from aplicacion.EstadoTerminar import EstadoTerminar
                return EstadoTerminar()
            elif evento.type == pygame.MOUSEBUTTONUP:
                evento_impulso = True
            elif evento.type == pygame.KEYUP:
                from aplicacion.EstadoPause import EstadoPause
                return EstadoPause(self.graficos, self.partida)

        self.partida.step(evento_impulso)

        if not self.partida.terminada:
            return self
        else: #Si la logica nos dice que la partida ha terminado es que hemos perdido y pasamos a un nuevo estado
            from aplicacion.EstadoMuerto import EstadoMuerto
            return EstadoMuerto(self.graficos)