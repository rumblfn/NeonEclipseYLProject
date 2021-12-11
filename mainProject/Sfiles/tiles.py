import pygame


block1 = pygame.image.load('static/Bg.png')
block2 = pygame.image.load('static/Bg1.png')
block3 = pygame.image.load('static/Bg1-1.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.blit(block3, (0, 0))
        # self.image.fill((10, 17, 25))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]