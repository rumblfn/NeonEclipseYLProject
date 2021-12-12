import pygame


class PlayerMapPreparation:
    def __init__(self, hero, sc):
        self.x = 400
        self.y = 600
        self.width = hero['width']
        self.height = hero['height']
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 5
        self.screen = sc
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.blit(hero['imagePreview'], (0, 0))

    def draw(self):
        self.screen.blit(self.surf, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        # if keys[pygame.K_UP]:
        #     self.y -= self.vel
        #
        # if keys[pygame.K_DOWN]:
        #     self.y += self.vel