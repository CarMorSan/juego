import sys, pygame
from bala import Bala
#Controlar los fps
clock=pygame.time.Clock()
def verificar_eventos_keydown(event,configuraciones,pantalla, nave, balas):
    """Responder a las pulsasiones de teclas"""
    if event.key==pygame.K_d:
        nave.movimiento_derecha=True
    elif event.key==pygame.K_a:
        nave.movimiento_izquierda=True
    elif event.key==pygame.K_w:
        nave.movimiento_arriba=True
    elif event.key==pygame.K_s:
        nave.movimiento_abajo=True
    elif event.key==pygame.K_SPACE:
        #Crea una nueva balaa y la agrega al grupo de balas
        nueva_bala=Bala(configuraciones,pantalla,nave)
        balas.add(nueva_bala)
        
        
def verificar_eventos_keyup(event,nave):
    if event.key==pygame.K_d:
        nave.movimiento_derecha=False
    elif event.key==pygame.K_a:
        nave.movimiento_izquierda=False
    elif event.key==pygame.K_w:
        nave.movimiento_arriba=False
    elif event.key==pygame.K_s:
        nave.movimiento_abajo=False

def verificar_eventos(configuraciones,pantalla,nave,balas):
    """ Responde a las pulsasiones de teclas y los eventos del raton """
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:# Evento de tecla presionada
            verificar_eventos_keydown(event,configuraciones,pantalla,nave,balas)
        elif event.type==pygame.KEYUP:# Evento de tecla soltada
            verificar_eventos_keyup(event,nave)

def fondo_estrellado(configuraciones,pantalla):
    """ Dibuja un cielo estrellado con posiciones al azar"""
    for coord in configuraciones.coor_list:
        x=coord[0]
        y=coord[1]
        pygame.draw.circle(pantalla,configuraciones.WHITE,(x,y),2)
        
        coord[0]-=1
        if coord[0]<0:
             coord[0]=configuraciones.ancho_pantalla

def actualizar_pantalla(configuraciones,pantalla,nave,balas):
    """ Actualiza las imagenes en la pantalla y pasa a la nueva pantalla """
    # Volver a dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(configuraciones.color_fondo)
    #Dibujar estrellas despues del fondo
    fondo_estrellado(configuraciones,pantalla)
    #Vuelve a dibujar todas las balas detras de la nave
    for bala in balas.sprites():
        bala.dibujar_bala()
    nave.blitme()
    #Hacer visible la pantalla dibujada mas reciente
    pygame.display.flip()
    clock.tick(60)