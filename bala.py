import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Sirve para manejar las balas disparadas desde la nave"""
    def __init__(self,configuraciones,pantalla,nave):
        super(Bala,self).__init__()
        self.pantalla=pantalla

        #Crea una bala rect en (0,0) y luego establece la posicion correcta
        self.rect=pygame.Rect(0,0,configuraciones.ancho_bala,configuraciones.alto_bala)
        self.rect.centery=nave.rect.centery
        self.rect.right=nave.rect.right

        #Almacena la posicion de la bala
        self.x=float(self.rect.x)
        self.color=configuraciones.color_bala
        self.velocidad_bala=configuraciones.velocidad_bala
    def update(self):
        """ ""Mueve la bala hacia la derecha de la pantalla"" """
        #Actualiza la posicion de la bala
        self.x+=self.velocidad_bala
        #Actualiza la posicion del rect
        self.rect.x=self.x
    def dibujar_bala(self):
        """ Dibuja la bala en la pantalla """
        pygame.draw.rect(self.pantalla,self.color,self.rect)

