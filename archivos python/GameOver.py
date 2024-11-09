# Importaciones
import pygame
from variables import WIDTH,HEIGHT,FPS,ORANGE
from buttons import draw_button_exit,exit_button

# inicializar pygame
pygame.init()

# Configuración de la pantalla de Game Over
wn_GameOver = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fin del juego")

# Guardar la imagen en una variable
GameOver_image = pygame.image.load("assets/img/background/Game Over/game_over.png")

# Configuración de fps
clock = pygame.time.Clock()

def game_over():
    run_game_over = True
    # Ciclo principal
    while run_game_over:
        # Controlar FPS
        clock.tick(FPS)

        # Cerrar el programa cuando se pulsa la X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game_over = False
            # Volver a menu de inicio
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    run_game_over = False

        # Color de la ventana
        wn_GameOver.fill(ORANGE)

        # Implementar imagen
        wn_GameOver.blit(GameOver_image, (50, 100))

        # Dibujar botón de salir
        draw_button_exit(wn_GameOver)

        # Actualizar pantalla automaticamente
        pygame.display.update()