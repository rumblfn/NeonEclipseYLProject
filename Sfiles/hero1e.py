import pygame

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
eWidth = 148 * WIDTH // 1440
eHeight = 70 * HEIGHT // 900


class Hero1AtackE(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images = []
        for i in range(1, 11):
            self.images.append(pygame.transform.scale(pygame.image.load(f'static/hero1animations/attackE/E{i}.png'),
                                                      (eWidth, eHeight)))
        self.current_sprite = 0
        self.image = pygame.Surface((eWidth, eHeight), pygame.SRCALPHA)
        self.rect = self.image.get_rect(midbottom=pos)

    def run_attackE(self):
        self.current_sprite += 0.25
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images[int(self.current_sprite)], (0, 0))
        if self.current_sprite >= 9:
            self.kill()

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

