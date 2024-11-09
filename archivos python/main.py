# Importaciones
import pygame
from random import randint, uniform
from variables import *
from personaje import Jugador, Enemy, Fruit
from menu import menu_principal
from GameOver import game_over
from animaciones_de_player import *
from animaciones_de_enemy import *

# Inicializar pygame
pygame.init()

# Configuración ventana de juego
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El caballero")
image_background = pygame.image.load("assets/img/background/pantalla de juego/Background.png")

# Iniciar menú principal
menu_principal()

# Música
sound = pygame.mixer.Sound("assets/Music/Battle-Conflict.mp3")

# Personajes
# Player
player = Jugador(x_player, y_player, animaciones, animaciones_Idle, animaciones_Jump, animaciones_Attack)

# enemies
# Almacenar enemigos
enemies = []
for i in range(number_enemy):
    enemy = Enemy(922, 575, 80, 55, 
                uniform(SPEED_ENEMY_MIN, SPEED_ENEMY_MAX), uniform(SPEED_ENEMY_MIN, SPEED_ENEMY_MAX), 
                animaciones2, animaciones_Attack_enemy, animaciones_Death_enemy)
    enemies.append(enemy)

# Fruit
fruit = Fruit(randint(0, WIDTH), 590)

# Fuente de texto
font = pygame.font.Font(None, 36)

# Configuración de fps
clock = pygame.time.Clock()


'''# Iniciar música
sound.play()'''

# Ciclo principal
while run:

    # Controlador de FPS
    clock.tick(FPS)

    # Mover al jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = speed_player
    elif mover_izquierda == True:
        delta_x = -speed_player

    if saltar:
        if salto >= -15:
            delta_y -= (salto * abs(salto)) * 0.5
            salto -= 1

        else:
            salto = 10
            saltar = False
    
    # Bajar la vida al enemigo
    for enemy in enemies:
        if attack == True:
            if player.shape.colliderect(enemy.rect):
                healt_enemy -= 1

    player.movimiento(delta_x, delta_y)

    # Mover imagen de la pantalla
    x_relativa = x % image_background.get_rect().width
    wn.blit(image_background, (x_relativa - image_background.get_rect().width, -100))
    if x_relativa < WIDTH:
        wn.blit(image_background, (x_relativa, -100))

    if delta_x != 0:
        if delta_x < 0:
            x += 5
        elif delta_x > 0:
            x -= 5
    else:
        x == 0

    # Animaciones del jugador
    player.update()

    # Dibujar al jugador
    player.draw(wn, delta_x, saltar, attack)

    for enemy in enemies:
        # Eliminar a los enemgios cuando mueren
        if healt_enemy == 0:
            enemies.remove(enemy)

        elif healt_enemy > 0:
            # mover al enemigo hacia el jugador
            if enemy.rect.x < player.shape.x:
                enemy.rect.x += enemy.speed_x
            elif enemy.rect.x > player.shape.x:
                enemy.rect.x -= enemy.speed_x

            # Movimientos del enemigo
            enemy.movimiento(delta_x, player, enemy)

            # Animacionees del enemigo
            enemy.update()

            # Dibujar enemigosd
            enemy.draw(wn, player, enemy, healt_enemy)
            #pygame.draw.rect(wn, COLOR_ENEMY, enemy.rect)

    # Dibujar objetivo
    fruit.draw(wn)

    # Verificar si el jugador ha ganado
    if player.shape.colliderect(fruit.fruit):
        score += 1
        # Mover el objetivo a una nueva posición aleatoria
        fruit.fruit.x = randint(0, WIDTH - WIDTH_FRUIT)

    # Verificar si el jugador ha perdido
    for enemy in enemies:
        if enemy.rect.colliderect(player.shape):
            healt_player -= 0.5
            if healt_player == 0:
                run = False
    
    # Hacer que la vida no baje del 0
    if healt_player < 0:
        healt_player == 0

    # Mostrar vida del jugador en la pantalla
    text = font.render(f"Vida: {healt_player}", True, COLOR_TEXTO)
    wn.blit(text, (200, 10))
        
    # Mostrar puntuación en la pantalla
    text = font.render(f"Puntuación: {score}", True, COLOR_TEXTO)
    wn.blit(text, (10, 10))

    # Cerrar el programa cuando se pulsa la X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sound.stop()
            run = False

        # Conectar teclas al movimiento del jugador
        # Tecla pulsada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_SPACE:
                saltar = True
            if event.key == pygame.K_s:
                rodar = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Botón izquierdo
                attack = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Botón izquierdo
                attack = False

        # Tecla no pulsada
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_s:
                rodar = False


    # Actualizar la pantalla automaticamente
    pygame.display.update()

'''# Detener sonido
sound.stop()'''

# Iniciar pantalla de Game Over
game_over