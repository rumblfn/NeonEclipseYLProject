import pygame
import math


bullet_image = pygame.transform.scale(pygame.image.load('static/Harchok.png').convert_alpha(), (24, 24))
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        self.image.blit(bullet_image, (0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10

        m_x, m_y = pygame.mouse.get_pos()
        bullet_x, bullet_y = pos
        distance_x = m_x - bullet_x
        distance_y = m_y - bullet_y
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = self.speed * math.cos(angle)
        self.speed_y = self.speed * math.sin(angle)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            self.kill()

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

