

class SueloGrafico:

    """ Mediante 2 imagenes de suelo se crea un bucle infinito de suelo moviendose """

    VELOCIDAD_X = -2
    def __init__(self, graficos, posicionX = 0):
        self.graficos = graficos
        self.posicionX = posicionX
        self.posicionY = 450


    def pintar(self, parar):
        if not parar: # En algunos momentos como cuando el jugador esta muerto o el juego en pausa paramos la animacion del suelo
            self.posicionX += SueloGrafico.VELOCIDAD_X
        if self.posicionX <= -1200: # Cuando el suelo deja de verse por el lado izquierdo de la pantalla vuelve a empezar a entrar por la derecha
            self.posicionX = 1200
        self.graficos.screen.blit(self.graficos.SUELO, (self.posicionX , self.posicionY))