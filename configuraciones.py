class Configuraciones():
    """Sirve para almacenar todas las configuraciones del juego"""
    def __init__(self):
        """Inicializa las configuraciones del juego"""
        import pygame
        self.ancho_pantalla=pygame.display.Info().current_w
        self.alto_pantalla=pygame.display.Info().current_h-80
        self.color_fondo=(0,0,0)

        import random
        self.WHITE=(255,255,255)
        #Posicion al azar de estrellas de fondo
        self.coor_list=[]
        for i in range(60):
            x=random.randint(0,self.ancho_pantalla)
            y=random.randint(0,self.alto_pantalla)
            self.coor_list.append([x,y])

        #Configuraciones de balas
        self.velocidad_bala=10
        self.ancho_bala=30
        self.alto_bala=6
        self.color_bala=198, 142, 255
        