import pygame
from variables import SCALA_ENEMY

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size=(w*scale, h*scale))
    return nueva_imagen

animaciones2 = []

for i in range(6):
    img = pygame.image.load(f"assets/img/characters/enemies/movimientos separados/correr/NightBorne_Run_{i}.png")
    img = escalar_img(img, SCALA_ENEMY)
    animaciones2.append(img)

animaciones_Attack_enemy = []

for i_ataque in range(7):
    img = pygame.image.load(f"assets/img/characters/enemies/movimientos separados/ataque/NightBorne_Attack_{i_ataque}.png")
    img = escalar_img(img, SCALA_ENEMY)
    animaciones_Attack_enemy.append(img)

animaciones_Death_enemy = []

for i in range(22):
    img = pygame.image.load(f"assets/img/characters/enemies/movimientos separados/muerte/NightBorne_Death_{i}.png")
    img = escalar_img(img, SCALA_ENEMY)
    animaciones_Death_enemy.append(img)
