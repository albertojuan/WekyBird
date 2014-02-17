import pygame
from logica.Jugador import Jugador

class JugadorGrafico:

    """ Clase encargada de representar graficamente al jugador """
    def __init__(self, jugadorLogico, graficos):
        self.jugadorLogico = jugadorLogico
        self.graficos = graficos
        self.rotacion = 0

    def pintar(self):
        if not self.jugadorLogico.tocaTierra or not self.jugadorLogico.muerto: #Rotamos el sprite del jugador para que mira hacia abajo cuando esta cayendo.
            self.rotacion = self.jugadorLogico.velocidadY * 30 / Jugador.IMPULSO
        jugadorRotado = pygame.transform.rotate(self.graficos.JUGADOR, self.rotacion)

        # Pintamos el sprite y lo ajustamos para que coincida que la forma geometrica que lo representa en la logica del juego
        self.graficos.screen.blit(jugadorRotado, (self.jugadorLogico.geometria.Centro.X - self.jugadorLogico.geometria.Radio - 15, self.jugadorLogico.geometria.Centro.Y - self.jugadorLogico.geometria.Radio -15))
        #pygame.draw.circle(self.grafico.screen, Graficos.RED,[self.jugadorLogico.geometria.Centro.X,int(self.jugadorLogico.geometria.Centro.Y)], self.jugadorLogico.geometria.Radio)
