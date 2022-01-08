import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, bullet_size, img, mouse_pos=False):
        super().__init__()
        self.image = pygame.Surface((bullet_size, bullet_size), pygame.SRCALPHA)
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10

        self.collide_count = 0

        if not mouse_pos:
            m_x, m_y = pygame.mouse.get_pos()
        else:
            m_x, m_y = mouse_pos

        bullet_x, bullet_y = pos
        distance_x = m_x - bullet_x
        distance_y = m_y - bullet_y
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = self.speed * math.cos(angle)
        self.speed_y = self.speed * math.sin(angle)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > 2000 or self.rect.x < 0 or self.rect.y > 1100 or self.rect.y < 0:
            self.kill()

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

