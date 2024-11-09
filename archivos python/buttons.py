import pygame
from variables import GREEN,COLOR_TEXTO

pygame.init()

# Crear botón para volver al menú de inicio
button_play = pygame.Rect(500, 450, 200, 100)
button_options = pygame.Rect(250, 450, 200, 100)
back = pygame.Rect(0, 0, 60, 30)
more_speed = pygame.Rect(595, 200, 30, 30)
less_speed = pygame.Rect(500, 200, 30, 30)
more_enemies = pygame.Rect(595, 400, 30, 30)
less_enemies = pygame.Rect(500, 400, 30, 30)
more_healt = pygame.Rect(495, 500, 30, 30)
less_healt = pygame.Rect(400, 500, 30, 30)
exit_button = pygame.Rect(350, 500, 200, 100)
# Función para dibujar el botón
# Volver a menú principal
def draw_button_back(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, back)
    font = pygame.font.Font(None, 36)
    text = font.render("<--", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=back.center)
    menu_options.blit(text, text_rect)

# Más velocidad
def draw_button_more_speed(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, more_speed)
    font = pygame.font.Font(None, 36)
    text = font.render("->", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=more_speed.center)
    menu_options.blit(text, text_rect)

# Menos velocidad
def draw_button_less_speed(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, less_speed)
    font = pygame.font.Font(None, 36)
    text = font.render("<-", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=less_speed.center)
    menu_options.blit(text, text_rect)

# Más enemigos
def draw_button_more_enemies(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, more_enemies)
    font = pygame.font.Font(None, 36)
    text = font.render("->", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=more_enemies.center)
    menu_options.blit(text, text_rect)

# Menos enemigos
def draw_button_less_enemies(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, less_enemies)
    font = pygame.font.Font(None, 36)
    text = font.render("<-", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=less_enemies.center)
    menu_options.blit(text, text_rect)

# Más vida
def draw_button_more_healt(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, more_healt)
    font = pygame.font.Font(None, 36)
    text = font.render("->", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=more_healt.center)
    menu_options.blit(text, text_rect)

# Menos vida
def draw_button_less_healt(menu_options):
    # Configurar botón
    pygame.draw.rect(menu_options, GREEN, less_healt)
    font = pygame.font.Font(None, 36)
    text = font.render("<-", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=less_healt.center)
    menu_options.blit(text, text_rect)

# Botón para empezar a jugar
def draw_button_play(menu):
    # Configurar botón
    pygame.draw.rect(menu, GREEN, button_play)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=button_play.center)
    menu.blit(text, text_rect)

# Botón de opciones
def draw_button_options(menu):
    # Configurar botón
    pygame.draw.rect(menu, GREEN, button_options)
    font = pygame.font.Font(None, 36)
    text = font.render("Options", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=button_options.center)
    menu.blit(text, text_rect)

# Botón de salir
def draw_button_exit(wn_GameOver):
    # Configurar botón
    pygame.draw.rect(wn_GameOver, GREEN, exit_button)
    font = pygame.font.Font(None, 56)
    text = font.render("Salir", True, COLOR_TEXTO)
    text_rect = text.get_rect(center=exit_button.center)
    wn_GameOver.blit(text, text_rect)

def draw_buttons(surface):
    draw_button_back(surface)
    draw_button_more_speed(surface)
    draw_button_less_speed(surface)
    draw_button_more_enemies(surface)
    draw_button_less_enemies(surface)
    draw_button_more_healt(surface)
    draw_button_less_healt(surface)