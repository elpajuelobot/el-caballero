# Importaciones
import pygame
from variables import HEIGHT,WIDTH,FPS,healt_player,number_enemy,speed_player,run_menu_options
from menu_opciones import menu_opciones
from buttons import *

# Inicializar pygame
pygame.init()

# Variable para guardar el sonido
sound = pygame.mixer.Sound("assets/Music/Battle-Conflict_intro.ogg")

# Configuración de fps
clock = pygame.time.Clock()

# Fuenta del texto del menú
font_menu = pygame.font.Font(None, 36)

# Texto de bienvenida
text_welcome = pygame.image.load("assets/img/background/menu principal/welcome.jpg")

# Imagen de fondo
image_background = pygame.image.load("assets/img/background/pantalla de juego/Background.png")

# Cofiguración del menú
menu = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu principal")
def menu_principal():
    # Variables
    run_menu = True
    GREEN = 0, 255, 0
    COLOR_TEXTO = 255, 0, 205
    # Menú principal
    while run_menu:
        '''# Iniciar música
        sound.play()'''

        # Controlador de FPS
        clock.tick(FPS)

        # imagen del fondo del menú
        menu.blit(image_background, (0, -100))

        # Cerrar el programa cuando se pulsa la X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                '''# Parar música
                sound.stop()'''
                run_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    '''# Parar música
                    sound.stop()'''
                    run_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_options.collidepoint(event.pos):
                    menu_opciones(run_menu_options, speed_player, number_enemy, healt_player)

        # Dibujar botones
        draw_button_play(menu)
        draw_button_options(menu)

        # Mostrar mensaje de bienvenida
        menu.blit(text_welcome, (80, -185))

        # Actualizar la pantalla automaticamente
        pygame.display.update()