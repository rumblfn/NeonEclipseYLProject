import pygame


class Spring(pygame.sprite.Sprite):
    def __init__(self, pos, size):  # midbottom
        super().__init__()
        self.size = size
        self.mid_bottom_pos = pos
        image1 = pygame.transform.scale(pygame.image.load('static/spring/1.png').convert(), (size, size // 4))
        image2 = pygame.transform.scale(pygame.image.load('static/spring/2.png'), (size, size // 2))
        image1_alpha = pygame.transform.scale(pygame.image.load('static/spring/1.png').convert(), (size, size // 4))
        image2_alpha = pygame.transform.scale(pygame.image.load('static/spring/2.png'), (size, size // 2))
        image1_alpha.set_alpha(128)
        image2_alpha.set_alpha(128)
        self.image1 = image1
        self.image2 = image2
        self.image1_alpha = image1_alpha
        self.image2_alpha = image2_alpha
        self.surf1 = pygame.Surface((size, size // 4), pygame.SRCALPHA)
        self.surf1.blit(image1, (0, 0))
        self.surf2 = pygame.Surface((size, size // 2), pygame.SRCALPHA)
        self.surf2.blit(image2, (0, 0))
        self.image = self.surf1
        self.rect = self.image.get_rect(midbottom=pos)

        self.spring_hit = False
        self.timer = 0
        self.timer_max = 360

    def change_spring(self):
        self.timer += 1
        if self.timer >= self.timer_max:
            self.spring_hit = False
            self.timer = 0
            self.rect.y += self.size // 4
            self.image = self.surf1

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]