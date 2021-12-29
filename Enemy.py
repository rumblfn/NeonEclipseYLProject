import pygame
from random import randrange
# from map_preparation_settings import level1_map


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_settings, map):
        super().__init__()
        self.block_moving = False
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.map = map
        self.map_w = len(self.map[0])
        self.map_h = len(self.map)
        self.name = enemy_settings['name']
        self.power = enemy_settings['attack power']
        self.maxHp = enemy_settings['maxHp']
        self.hp = enemy_settings['maxHp']
        self.started_pos = self.pos_change(self.map, self.map_w, self.map_h)

        self.K_x = False

        re_size = (HEIGHT / len(map)) / 64
        self.width = round(enemy_settings['width'] * re_size) - 1
        self.height = round(enemy_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        self.image.blit(pygame.transform.scale(enemy_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        # self.direction = pygame.math.Vector2(0, 0)
        # self.control_speed = round(9 * WIDTH / 1440)
        # self.speed = round(9 * WIDTH / 1440)
        self.gravity = 0.7 * HEIGHT / 900
        # self.jump_speed = -16 * HEIGHT / 900
        # self.jump_bool = True

        self.server_player = None

    def pos_change(self, current_map, widht, height):
        new_pos = randrange(0, widht), randrange(0, height)
        while self.pos_wrong(new_pos, current_map):
            new_pos = randrange(0, widht), randrange(0, height)
        return new_pos

    def pos_wrong(self, pos, map):
        if map[pos[0]][pos[1]] == 'X':
            return True
        return False

    # def apply_gravity(self):
    #     self.direction.y += self.gravity
    #     self.rect.y += self.direction.y
    #
    # def jump(self):
    #     self.jump_bool = False
    #     self.direction.y = self.jump_speed

    def update(self):
        if not self.block_moving:
            self.get_input()

    def initialize_server_player(self, server_player):
        self.server_player = server_player