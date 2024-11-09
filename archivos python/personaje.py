# Importaciones
import pygame
from variables import HEIGHT_PLAYER, WIDTH_PLAYER, WIDTH, WIDTH_FRUIT, HEIGHT_FRUIT


# Controlar que no se salga de la pantalla
def limit_window(self):
    if self.shape.x < 0:
        self.shape.x = 0
    if self.shape.x + WIDTH_PLAYER > WIDTH:
        self.shape.x = WIDTH - WIDTH_PLAYER
    if self.shape.y < 0:
        self.shape.y = 0
    if self.shape.y + HEIGHT_PLAYER > 625:
        self.shape.y = 625 - HEIGHT_PLAYER


class Jugador:
    # Constructor
    def __init__(self, x, y, animaciones, animaciones_Idle,
            animaciones_Jump, animaciones_Attack):
        self.flip = False
        self.animaciones = animaciones
        self.animaciones_Idle = animaciones_Idle
        self.animaciones_Jump = animaciones_Jump
        self.animaciones_Attack = animaciones_Attack

        # Imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0

        # Aquí se almacena la hora actual (en milisegundos desde que se inició pygame)
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.image_Idle = animaciones_Idle[self.frame_index]
        self.image_Jump = animaciones_Jump[self.frame_index]
        self.image_Attack = animaciones_Attack[self.frame_index]

        # Ajustes del jugador
        self.shape = pygame.Rect(0, 0, WIDTH_PLAYER, HEIGHT_PLAYER)
        self.shape.center = (x, y)

    # Actualizar animaciones
    def update(self):
        # Ir cambiando de animación cada 100 milisegundos
        cooldown_animaciones = 100
        self.image = self.animaciones[self.frame_index]
        self.image_Idle = self.animaciones_Idle[self.frame_index]
        self.image_Jump = self.animaciones_Jump[self.frame_index]
        self.image_Attack = self.animaciones_Attack[self.frame_index]

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        # Volver a la animación 0 una vez que se ha acabado la lista
        if self.frame_index >= len(self.animaciones_Idle):
            self.frame_index = 0

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        # Volver a la animación 0 una vez que se ha acabado la lista
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        # Volver a la animación 0 una vez que se ha acabado la lista
        if self.frame_index >= len(self.animaciones_Jump):
            self.frame_index = 0

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        # Volver a la animación 0 una vez que se ha acabado la lista
        if self.frame_index >= len(self.animaciones_Attack):
            self.frame_index = 0

    # Dibujar
    def draw(self, wn, delta_x, saltar, attack):
        imagen_flip = pygame.transform.flip(self.image, self.flip, flip_y=False)
        imagen_flip2 = pygame.transform.flip(self.image_Idle, self.flip, flip_y=False)
        imagen_flip3 = pygame.transform.flip(self.image_Jump, self.flip, flip_y=False)
        imagen_flip4 = pygame.transform.flip(self.image_Attack, self.flip, flip_y=False)

        if delta_x != 0:
            wn.blit(imagen_flip, self.shape)
        elif saltar == True:
            wn.blit(imagen_flip3, self.shape)
        elif attack == True:
            wn.blit(imagen_flip4, self.shape)
        else:
            wn.blit(imagen_flip2, self.shape)

        #pygame.draw.rect(wn, (COLOR_PLAYER), self.shape, 2)
    # Mover
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
        # Función para no salirse de los límites de la pantalla
        limit_window(self)

# Definir la clase Enemy
class Enemy:
    def __init__(self, x, y, width, height, speed_x, speed_y, animaciones2, animaciones_Attack_enemy, animaciones_Death_enemy):
        self.flip = False
        self.animaciones2 = animaciones2
        self.animaciones_Attack_enemy = animaciones_Attack_enemy
        self.animaciones_Death_enemy = animaciones_Death_enemy
        # Imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        # Aquí se almacena la hora actual (en milisegundos desde que se inició pygame)
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones2[self.frame_index]
        self.image2 = animaciones_Attack_enemy[self.frame_index]
        self.image3 = animaciones_Death_enemy[self.frame_index]

        self.rect = pygame.Rect(x, y, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    # Actualizar animaciones
    def update(self):
        # Ir cambiando de animación cada 100 milisegundos
        cooldown_animaciones = 100
        self.image = self.animaciones2[self.frame_index]
        self.image2 = self.animaciones_Attack_enemy[self.frame_index]
        self.image3 = self.animaciones_Death_enemy[self.frame_index]

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            # Volver a la animación 0 una vez que se ha acabado la lista
            if self.frame_index >= len(self.animaciones2):
                self.frame_index = 0

        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            # Volver a la animación 0 una vez que se ha acabado la lista
            if self.frame_index >= len(self.animaciones_Attack_enemy):
                self.frame_index = 0
        
        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            # Volver a la animación 0 una vez que se ha acabado la lista
            if self.frame_index >= len(self.animaciones_Death_enemy):
                self.frame_index = 0

    def draw(self, wn, player, enemy, healt_enemy):
        imagen_flip = pygame.transform.flip(self.image, self.flip, flip_y=False)
        imagen_flip2 = pygame.transform.flip(self.image2, self.flip, flip_y=False)
        imagen_flip3 = pygame.transform.flip(self.image3, self.flip, flip_y=False)

        if enemy.rect.colliderect(player.shape):
            wn.blit(imagen_flip2, self.rect)
        elif healt_enemy <= 0:
            wn.blit(imagen_flip3, self.rect)
        else:
            wn.blit(imagen_flip, self.rect)

    def movimiento(self, delta_x, player, enemy):
        if enemy.rect.x < player.shape.x:
            self.flip = False
        if enemy.rect.x > player.shape.x:
            self.flip = True

# Pócima de curación
class Fruit:
    def __init__(self, x, y):
        self.fruit_img = pygame.image.load("assets/img/characters/objects/frutas/05.png")
        self.fruit = pygame.Rect(x, y, WIDTH_FRUIT, HEIGHT_FRUIT)

    def draw(self, wn):
        wn.blit(self.fruit_img, self.fruit)
        # pygame.draw.rect(wn, (COLOR_FRUIT), self.fruit)
