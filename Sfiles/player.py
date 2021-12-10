import pygame
from map_preparation_settings import tile_size
from map_preparation_settings import level1_map

player1Preview = pygame.image.load('static/charackter64x64Preview.png')
player2Paladin = pygame.image.load('static/paladin27x78.png')
player3Sniper = pygame.image.load('static/sniper37x75.png')
playerImages = {
    'Hero1': player1Preview,
    'Hero2': player3Sniper,
    'Hero3': player2Paladin,
}


class Player_map_preparation(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(level1_map)
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.blit(pygame.transform.scale(playerImages['Hero1'], (tile_size, tile_size)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 8
        self.ready = True  # None
        self.name = 'Hero1'
        self.attack_power = None
        self.maxHp = None
        self.attackE = None
        self.attackQ = None
        self.simpleAttack = None

    def draw(self, win):
        win.blit(playerImages[self.name], self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        # if keys[pygame.K_UP]:
        #     self.y -= self.vel
        #
        # if keys[pygame.K_DOWN]:
        #     self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
