import pygame


class Trap(pygame.sprite.Sprite):
    def __init__(self, pos, tile_size):
        super().__init__()
        self.images = []

        for i in range(1, 6):
            self.images.append(
                pygame.transform.scale(
                    pygame.image.load(f'static/trap_chain/{i}.png'),
                    (int(76 * tile_size / 64), int(178 * tile_size / 64))
                )
            )

        self.image = pygame.Surface((int(76 * tile_size / 64), int(178 * tile_size / 64)), pygame.SRCALPHA)
        self.image.blit(self.images[0], (0, 0))
        self.rect = self.image.get_rect(midtop=pos)

        self.timer = 0
        self.timer_max = 60
        self.ACTIVE = False
        self.READY = False

        self.new_timer = 0
        self.new_timer_max = 300

    def update(self):
        if self.ACTIVE:
            self.READY = False
            self.timer += 2
            if self.timer >= self.timer_max:
                self.ACTIVE = False
            self.image.fill((0, 0, 0, 0))
            self.image.blit(
                self.images[int(self.timer * 4 / self.timer_max)],
                (0, 0)
            )
        else:
            self.new_timer += 1
            if self.new_timer >= self.new_timer_max:
                self.timer = 0
                self.READY = True
                self.new_timer = 0
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images[0], (0, 0))
