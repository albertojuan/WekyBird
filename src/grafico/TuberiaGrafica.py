import pygame

class TuberiaGrafica:

    """ Representacion grafica del obstaculo que el jugador ha de tratar de esquivar. """
    def __init__(self, tuberiaLogica, graficos):
        self.tuberiaLogica = tuberiaLogica
        self.graficos = graficos

    def pintar(self):
        pygame.draw.rect(self.graficos.screen, self.graficos.GREEN, pygame.Rect(self.tuberiaLogica.geometria.posicion.X, self.tuberiaLogica.geometria.posicion.Y, self.tuberiaLogica.geometria.Ancho, self.tuberiaLogica.geometria.Alto))

        # Segun si la tuberia esta arriba o abajo de la pantalla la representamos de una forma u otra
        if self.tuberiaLogica.geometria.posicion.Y > 0:
            self.graficos.screen.blit(self.graficos.TUBERIA, (self.tuberiaLogica.geometria.posicion.X - 6, self.tuberiaLogica.geometria.posicion.Y))
        else:
            self.graficos.screen.blit(pygame.transform.flip(self.graficos.TUBERIA, False, True), (self.tuberiaLogica.geometria.posicion.X - 6, self.tuberiaLogica.geometria.posicion.Y - 300 + self.tuberiaLogica.geometria.Alto))
