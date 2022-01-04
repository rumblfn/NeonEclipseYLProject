import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, tile_size):
        super().__init__()
        self.image = pygame.Surface((tile_size // 2, tile_size // 2), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(
            pygame.image.load('static/ball_gun/ball.png'),
            (tile_size // 2, tile_size // 2)
        ), (0, 0))
        self.rect = self.image.get_rect(midleft=pos)
        self.speed = 17

    def update(self):
        self.rect.x += self.speed
