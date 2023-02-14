import pygame
from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego
def correr_juego():
    #Inicializar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    configuraciones=Configuraciones()
    """ # Carga el sonido
    sonido = pygame.mixer.Sound("sonido/fondo.wav")
    # Reproduce el sonido en un bucle
    sonido.play(loops=-1)
    sonido.set_volume(0.1) """
    # Crear pantalla y asignarle un tamaño
    pantalla=pygame.display.set_mode((configuraciones.ancho_pantalla,configuraciones.alto_pantalla))
    # Poner titulo a la pantalla
    pygame.display.set_caption("Mision vaca voladora")
    #Crea una nave
    nave=Nave(pantalla)
    #Crea un grupo para almacenar las balas
    balas=Group()
    #Iniciar el bucle principal del juego
    while True:
        #Escuchar eventos del teclado o raton
        funciones_juego.verificar_eventos(configuraciones,pantalla,nave,balas)
        nave.update()
        balas.update()
        funciones_juego.actualizar_pantalla(configuraciones,pantalla,nave,balas)

correr_juego()