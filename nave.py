import pygame
velocidad=5
class Nave():
    """Sirve para gestionar el comportamiento de la nave"""
    def __init__(self, pantalla):
        """Inicializa la nave y establece su posicion de partida"""
        self.pantalla=pantalla
        #Carga la imagen de la nave y obtiene su rect(rectangulo)
        self.imagen=pygame.image.load("imagenes/nave.png")
        self.rect=self.imagen.get_rect()
        self.pantalla_rect=pantalla.get_rect()

        #Empieza cada nueva nave en la parte inferior de la pantalla
        self.rect.centery=self.pantalla_rect.centery
        self.rect.left=self.pantalla_rect.left
        #Bandera de movimiento
        self.movimiento_derecha=False
        self.movimiento_izquierda=False
        self.movimiento_arriba=False
        self.movimiento_abajo=False
    def update(self):
        """ Actualiza la posicion de la nave segun la bandera de movimiento """
        if self.movimiento_derecha and self.rect.right< self.pantalla_rect.right:
            self.rect.centerx+=velocidad
        if self.movimiento_izquierda and self.rect.left>0:
            self.rect.centerx-=velocidad
        if self.movimiento_arriba and self.rect.top>0:
            self.rect.centery-=velocidad
        if self.movimiento_abajo and self.rect.bottom<self.pantalla_rect.bottom:# and self.rect.bottom<self.pantalla_rect.bottom
            self.rect.centery+=velocidad

    def blitme(self):
        """ Dibuja la nave en su ubicacion actual """
        self.pantalla.blit(self.imagen,self.rect)
        