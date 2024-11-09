import pygame
from variables import SCALA_PLAYER


def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size=(w*scale, h*scale))
    return nueva_imagen

# Correr
animaciones = []
for i in range(10):
    img = pygame.image.load(f"assets/img/characters/player/caballero/imagenes recortadas/Run_{i}.png")
    img = escalar_img(img, SCALA_PLAYER)
    animaciones.append(img)

# Quedarse quieto
animaciones_Idle = []
for i in range(10):
    img = pygame.image.load(f"assets/img/characters/player/caballero/imagenes recortadas/_Idle_{i}.png")
    img = escalar_img(img, SCALA_PLAYER)
    animaciones_Idle.append(img)

# Saltar
animaciones_Jump = []
for i in range(3):
    img = pygame.image.load(f"assets/img/characters/player/caballero/imagenes recortadas/_Jump_{i}.png")
    img = escalar_img(img, SCALA_PLAYER)
    animaciones_Jump.append(img)

animaciones_Attack = []
for i in range(10):
    img = pygame.image.load(f"assets/img/characters/player/caballero/imagenes recortadas/_Attack_{i}.png")
    img = escalar_img(img, SCALA_PLAYER)
    animaciones_Attack.append(img)