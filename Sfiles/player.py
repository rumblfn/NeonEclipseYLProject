import pygame
from pygame.constants import *

try:
    from CBullet import Bullet
    player1Preview = pygame.image.load('static/charackter64x64Preview.png').convert_alpha()
    player2Paladin = pygame.image.load('static/paladin27x78.png').convert_alpha()
    player3Sniper = pygame.image.load('static/sniper37x75.png').convert_alpha()
    playerImages = {
        'Hero1': player1Preview,
        'Hero2': player3Sniper,
        'Hero3': player2Paladin,
    }
except:
    print('game not started')


class Player_map_preparation(pygame.sprite.Sprite):
    def __init__(self, pos, player_settings):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = player_settings['name']
        self.power = player_settings['attack power']
        self.maxHp = player_settings['maxHp']
        self.started_pos = pos

        self.K_x = False
        self.current_sprite = 0

        from map_preparation_settings import level1_map

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(player_settings['width'] * re_size) - 1
        self.height = round(player_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # self.image.fill((255, 255, 255, 0))
        self.images = False
        if player_settings['animations'] is None:
            self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        else:
            self.images = {}
            for el in player_settings['animations'].keys():
                self.images[el] = []
                for i in range(1, 15):
                    image = pygame.transform.scale(pygame.image.load(f'{player_settings["animations"][el]}{i}.png').convert_alpha(), (self.width, self.height))
                    self.images[el].append(image)
            self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        print(self.images)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(7 * WIDTH / 1440)
        self.speed = round(7 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True

        self.shoot_bool = 1

    def get_input(self):
        self.current_sprite += 0.25
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if keys[pygame.K_d]:
            self.direction.x = 1
            if self.images:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
        elif keys[pygame.K_a]:
            self.direction.x = -1
            if self.images:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['left_walk'][int(self.current_sprite)], (0, 0))
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if not self.direction.y:
            self.jump_bool = True

        if self.current_sprite >= 13:
            self.current_sprite = 0

    def create_bullet(self):
        self.shoot_bool = 0
        return Bullet((self.rect.centerx + 10, self.rect.centery - self.height / 4))

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        self.shoot_bool += 0.1
        self.get_input()


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ready = None  # True
