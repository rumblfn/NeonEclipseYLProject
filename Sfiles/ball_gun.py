import pygame


class Ball_gun(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.images = []
        for i in range(5, 0, -1):
            self.images.append(
                pygame.transform.scale(
                    pygame.image.load(f'static/ball_gun/{i}.png'),
                    (size, size)
                )
            )

        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.blit(self.images[0], (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.timer_max = 120
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= self.timer_max:
            self.timer = 0
            self.timer_max = 120
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images[int(self.timer * 5 / self.timer_max)], (0, 0))

    # def update(self, shift):
    #     self.rect.x += shift[0]
    #     self.rect.y += shift[1]

