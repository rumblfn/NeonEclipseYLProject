import pygame
import random
from map_preparation_settings import level1_map

# block1 = pygame.image.load('static/Bg.png')
# block2 = pygame.image.load('static/Bg1.png')
# block3 = pygame.image.load('static/Bg1-1.png')
h = pygame.display.Info().current_h
res = h // len(level1_map)
portal_res = round((109 / 900) * h)
blockLeft = pygame.transform.scale(pygame.image.load('static/blockLeft.png'), (res, res))
blockTop = pygame.transform.scale(pygame.image.load('static/blockTop.png'), (res, res))
blockRight = pygame.transform.scale(pygame.image.load('static/blockRight.png'), (res, res))
blockBottom = pygame.transform.scale(pygame.image.load('static/blockBottom.png'), (res, res))
blockLeftTop = pygame.transform.scale(pygame.image.load('static/blockLeftRight.png'), (res, res))
blockTopRight = pygame.transform.scale(pygame.image.load('static/blockTopRight.png'), (res, res))
blockRightBottom = pygame.transform.scale(pygame.image.load('static/blockRightBottom.png'), (res, res))
blockBottomLeft = pygame.transform.scale(pygame.image.load('static/blockLeftBottom.png'), (res, res))
block = pygame.transform.scale(pygame.image.load('static/block.png'), (res, res))
windowBlock1 = pygame.transform.scale(pygame.image.load('static/WindowBlock.png'), (res, res))
windowBlock2 = pygame.transform.scale(pygame.image.load('static/WindowBlock2.png'), (res, res))
windowBlock3 = pygame.transform.scale(pygame.image.load('static/WindowBlock3.png'), (res, res))
windowBlock4 = pygame.transform.scale(pygame.image.load('static/WindowBlock4.png'), (res, res))
windowBlock5 = pygame.transform.scale(pygame.image.load('static/WindowBlock5.png'), (res, res))
windowBlock6 = pygame.transform.scale(pygame.image.load('static/WindowBlock6.png'), (res, res))
blockTopBottom = pygame.transform.scale(pygame.image.load('static/blockBottomTop.png'), (res, res))
blockTopLeftBottom = pygame.transform.scale(pygame.image.load('static/blockBottomLeftTop.png'), (res, res))
blockTopRightBottom = pygame.transform.scale(pygame.image.load('static/blockBottomRightTop.png'), (res, res))
blockBorders = pygame.transform.scale(pygame.image.load('static/blockBorders.png'), (res, res))
blockLeftTopRight = pygame.transform.scale(pygame.image.load('static/blockLeftTopRight.png'), (res, res))
portalImage = pygame.transform.scale(pygame.image.load('static/portal.png').convert_alpha(), (portal_res, portal_res))
lst_of_windows = [windowBlock1, windowBlock2, windowBlock3, windowBlock4, windowBlock5, windowBlock6]


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.set_image(cell, size)
        # self.image.fill((10, 17, 25))
        self.rect = self.image.get_rect(topleft=pos)

    def set_image(self, cell, s):
        if cell == '0':
            self.image.blit(lst_of_windows[random.randint(0, 5)], (0, 0))
        elif cell == '1':
            self.image.blit(blockLeft, (0, 0))
        elif cell == '2':
            self.image.blit(blockTop, (0, 0))
        elif cell == '3':
            self.image.blit(blockRight, (0, 0))
        elif cell == '4':
            self.image.blit(blockBottom, (0, 0))
        elif cell == '5':
            self.image.blit(blockLeftTop, (0, 0))
        elif cell == '6':
            self.image.blit(blockTopRight, (0, 0))
        elif cell == '7':
            self.image.blit(blockRightBottom, (0, 0))
        elif cell == '8':
            self.image.blit(blockBottomLeft, (0, 0))
        elif cell == '9':
            self.image.blit(blockTopBottom, (0, 0))
        elif cell == 'm':
            self.image.blit(blockTopLeftBottom, (0, 0))
        elif cell == 'n':
            self.image.blit(blockTopRightBottom, (0, 0))
        elif cell == 'b':
            self.image.blit(blockBorders, (0, 0))
        elif cell == 'c':
            self.image.blit(blockLeftTopRight, (0, 0))
        elif cell == 'X':
            self.image.blit(block, (0, 0))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((portal_res, portal_res), pygame.SRCALPHA)
        self.image.blit(portalImage, (0, 0))
        self.rect = self.image.get_rect(topright=(pos[0] - 8, pos[1] - 40))
        print(self.rect)

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]