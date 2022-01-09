import pygame
import time
from random import randint
from CBullet import Bullet
from map_preparation_settings import level1_map


class Enemy(pygame.sprite.Sprite):
    def __init__(self, lev):
        super().__init__()
        self.block_moving = False
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.map = level1_map
        self.map_w = 134
        self.map_h = 17
        self.CURRENT_SPRITE = 0
        self.name = 'Bat'
        self.side = 'r'
        self.animations = {
            'r': ['C:/Users/Артём/PycharmProjects/NeonEclipseYLProject/Sfiles/static/Bat/Right/', 4],
            'l': ['C:/Users/Артём/PycharmProjects/NeonEclipseYLProject/Sfiles/static/Bat/Left/', 4],
        }
        self.power = 30
        self.maxHp = 100
        self.hp = 100
        self.pos = 0, 0
        self.player_pos = lev.player_sprite.rect

        re_size = (HEIGHT / len(self.map)) / 64
        self.width = round(32 * re_size) - 1
        self.height = round(32 * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        self.rect = self.image.get_rect(topleft=self.pos)

        tile_size = HEIGHT // len(self.map)

        self.bullets = pygame.sprite.Group()
        self.poser()
        self.shoot()

        self.pix_pos = self.pos[0] * tile_size, self.pos[1] * tile_size

        self.images = dict()
        for el in self.animations.keys():
            self.images[el] = []
            src = self.animations[el][0]
            number_of_last_image = self.animations[el][1]
            for i in range(1, number_of_last_image + 1):
                image = pygame.transform.scale(
                    pygame.image.load(f'{src}{i}.png').convert_alpha(),
                    (self.width, self.height))
                self.images[el].append(image)

    def pos_change(self, current_map, widht, height):
        new_pos = 2, 22
        #pos_incor = self.pos_wrong(new_pos, current_map)
        # while pos_incor:
        #     new_pos = randint(0, 16), randint(0, widht - 1)
        #     pos_incor = self.pos_wrong(new_pos, current_map)
        if self.player_pos[0] < new_pos[0]:
            self.side = 'l'
        else:
            self.side = 'r'
        return new_pos

    # def pos_wrong(self, pos, map1):
    #     print(map1[pos[0]][pos[1]])
    #     if map1[pos[0]][pos[1]] == ' ':
    #         return False
    #     if map1[pos[0]][pos[1]] == 'X':
    #         return True
    #     return False

    def poser(self):
        while self.hp > 0:
            self.CURRENT_SPRITE += 0.25
            if self.CURRENT_SPRITE >= 4:
                self.CURRENT_SPRITE = 0
            self.pos = self.pos_change(self.map, self.map_w, self.map_h)
            self.hp -= 50
            # self.image.blit(self.images[self.side][int(self.CURRENT_SPRITE)], (0, 0))
            time.sleep(2)
            self.poser()

    def create_bullet(self):
        return Bullet(self.pix_pos, self.player_pos)

    def shoot(self):
        while self.hp > 0:
            self.bullets.add(self.create_bullet())
            self.hp -= 50
            time.sleep(2)
            self.shoot()

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]