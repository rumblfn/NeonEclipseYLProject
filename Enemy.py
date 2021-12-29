import pygame
from random import randrange
# from map_preparation_settings import level1_map


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_settings, map):
        super().__init__()
        self.block_moving = False
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.dif = 0
        self.map = map
        self.map_w = len(self.map[0])
        self.map_h = len(self.map)
        self.name = enemy_settings['name']
        self.power = enemy_settings['attack power']
        self.maxHp = enemy_settings['maxHp']
        self.hp = enemy_settings['maxHp']
        self.started_pos = self.pos_change(self.map, self.map_w, self.map_h)

        re_size = (HEIGHT / len(map)) / 64
        self.width = round(enemy_settings['width'] * re_size) - 1
        self.height = round(enemy_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        self.image.blit(pygame.transform.scale(enemy_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def pos_change(self, current_map, widht, height):
        new_pos = randrange(0, widht), randrange(0, height)
        while self.pos_wrong(new_pos, current_map):
            new_pos = randrange(0, widht), randrange(0, height)
        return new_pos

    def pos_wrong(self, pos, map):
        if map[pos[0]][pos[1]] == 'X':
            return True
        return False

    def poser(self):
        self.pos_change(self.map, self.map_w, self.map_h)

    def update(self, shift):
        self.dif += shift[0]
        self.rect.x += shift[0]
        self.rect.y += shift[1]
