import pygame
import random

# block1 = pygame.image.load('static/Bg.png')
# block2 = pygame.image.load('static/Bg1.png')
# block3 = pygame.image.load('static/Bg1-1.png')

blockLeft = pygame.image.load('static/blockLeft.png')
blockTop = pygame.image.load('static/blockTop.png')
blockRight = pygame.image.load('static/blockRight.png')
blockBottom = pygame.image.load('static/blockBottom.png')
blockLeftTop = pygame.image.load('static/blockLeftRight.png')
blockTopRight = pygame.image.load('static/blockTopRight.png')
blockRightBottom = pygame.image.load('static/blockRightBottom.png')
blockBottomLeft = pygame.image.load('static/blockLeftBottom.png')
block = pygame.image.load('static/block.png')
windowBlock1 = pygame.image.load('static/WindowBlock.png')
windowBlock2 = pygame.image.load('static/WindowBlock2.png')
windowBlock3 = pygame.image.load('static/WindowBlock3.png')
windowBlock4 = pygame.image.load('static/WindowBlock4.png')
windowBlock5 = pygame.image.load('static/WindowBlock5.png')
windowBlock6 = pygame.image.load('static/WindowBlock6.png')
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
            self.image.blit(pygame.transform.scale(lst_of_windows[random.randint(0, 5)], (s, s)), (0, 0))
        elif cell == '1':
            self.image.blit(pygame.transform.scale(blockLeft, (s, s)), (0, 0))
        elif cell == '2':
            self.image.blit(pygame.transform.scale(blockTop, (s, s)), (0, 0))
        elif cell == '3':
            self.image.blit(pygame.transform.scale(blockRight, (s, s)), (0, 0))
        elif cell == '4':
            self.image.blit(pygame.transform.scale(blockBottom, (s, s)), (0, 0))
        elif cell == '5':
            self.image.blit(pygame.transform.scale(blockLeftTop, (s, s)), (0, 0))
        elif cell == '6':
            self.image.blit(pygame.transform.scale(blockTopRight, (s, s)), (0, 0))
        elif cell == '7':
            self.image.blit(pygame.transform.scale(blockRightBottom, (s, s)), (0, 0))
        elif cell == '8':
            self.image.blit(pygame.transform.scale(blockBottomLeft, (s, s)), (0, 0))
        elif cell == 'X':
            self.image.blit(pygame.transform.scale(block, (s, s)), (0, 0))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]