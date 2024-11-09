import pygame
from variables import COLOR_TEXTO, WIDTH, HEIGHT, FPS
from buttons import *

pygame.init()

# Fuente de texto
font_menu_options = pygame.font.Font(None, 60)

# Configuración pantalla
menu_options = pygame.display.set_mode((WIDTH, HEIGHT))
image_background = pygame.image.load("assets/img/background/pantalla de juego/Background.png")
pygame.display.set_caption("Menu principal")

# FPS
clock = pygame.time.Clock()


def menu_opciones(run_menu_options, speed_player, number_enemy, healt_player):
    while run_menu_options:
        speed_player = speed_player
        number_enemy = number_enemy
        healt_player = healt_player
        # Controlar FPS
        clock.tick(FPS)

        # imagen del fondo del menú
        menu_options.blit(image_background, (0, -100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu_options = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    run_menu_options = False
                elif more_speed.collidepoint(event.pos):
                    speed_player = min(speed_player + 1, 16)
                elif less_speed.collidepoint(event.pos):
                    speed_player = max(speed_player - 1, 1)
                elif more_enemies.collidepoint(event.pos):
                    number_enemy = min(number_enemy + 1, 16)
                elif less_enemies.collidepoint(event.pos):
                    number_enemy = max(number_enemy - 1, 1)
                elif more_healt.collidepoint(event.pos):
                    healt_player = min(healt_player + 1, 20)
                elif less_healt.collidepoint(event.pos):
                    healt_player = max(healt_player - 1, 1)

        draw_buttons(menu_options)

        text = font_menu_options.render("Opciones", True, COLOR_TEXTO)
        menu_options.blit(text, (500, 15))

        text = font_menu_options.render("Velocidad del jugador:", True, COLOR_TEXTO)
        menu_options.blit(text, (48, 195))
        text = font_menu_options.render(f"{speed_player}", True, COLOR_TEXTO)
        menu_options.blit(text, (545, 200))

        text = font_menu_options.render("Número de enemigos:", True, COLOR_TEXTO)
        menu_options.blit(text, (48, 395))
        text = font_menu_options.render(f"{number_enemy}", True, COLOR_TEXTO)
        menu_options.blit(text, (545, 400))

        text = font_menu_options.render("Vida del jugador:", True, COLOR_TEXTO)
        menu_options.blit(text, (48, 495))
        text = font_menu_options.render(f"{healt_player}", True, COLOR_TEXTO)
        menu_options.blit(text, (442, 500))

        pygame.display.update()
