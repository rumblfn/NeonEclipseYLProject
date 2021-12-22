import pygame


class Interface:
    def __init__(self, screen_width, screen_height, screen):
        sprite_kef = screen_width / 1000
        self.sprite_kef = sprite_kef
        hpImage = pygame.transform.scale(pygame.image.load('static/healthIconMenu.png'),
                                         (round(50 * sprite_kef), round(50 * sprite_kef)))
        hpBar = pygame.transform.scale(pygame.image.load('static/hpBar.png'),
                                       (round(160 * sprite_kef), round(32 * sprite_kef)))
        self.hpImageSurface = pygame.Surface((round(50 * sprite_kef), round(50 * sprite_kef)), pygame.SRCALPHA)
        self.hpImageSurface.blit(hpImage, (0, 0))
        self.hpBarWidth = round(160 * sprite_kef)
        self.hpBarHeight = round(32 * sprite_kef)
        self.hpBarSurface = pygame.Surface((round(160 * sprite_kef), round(32 * sprite_kef)), pygame.SRCALPHA)
        self.hpBarSurface.blit(hpBar, (0, 0))

        powerImage = pygame.transform.scale(pygame.image.load('static/attackIconMenu.png'),
                                         (round(50 * sprite_kef), round(50 * sprite_kef)))
        self.powerImageSurface = pygame.Surface((round(50 * sprite_kef), round(50 * sprite_kef)), pygame.SRCALPHA)
        self.powerImageSurface.blit(powerImage, (0, 0))

        chestImage = pygame.transform.scale(pygame.image.load('static/chest.png'),
                                         (round(50 * sprite_kef), round(45 * sprite_kef)))
        self.chestImageSurface = pygame.Surface((round(50 * sprite_kef), round(45 * sprite_kef)), pygame.SRCALPHA)
        self.chestImageSurface.blit(chestImage, (0, 0))

        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont('Avenir Next', round(26 * self.screen_width / 1440))

    def update_screen_size(self, w, h):
        self.screen_width = w
        self.screen_height = h

    def draw(self, hp, max_hp, power):
        self.screen.blit(self.hpImageSurface, (10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (23 + 50 * self.sprite_kef, 28, (hp / max_hp) * self.hpBarWidth - 6, self.hpBarHeight - 6))
        titleSurface = self.font.render(f'{hp}/{max_hp}', False, (0, 255, 0))
        self.screen.blit(titleSurface, (40 + 50 * self.sprite_kef, 30))
        self.screen.blit(self.hpBarSurface, (20 + 50 * self.sprite_kef, 25))
        self.screen.blit(self.powerImageSurface, (10, 20 + 50 * self.sprite_kef))
        titleSurface = self.font.render(str(power), False, (0, 255, 0))
        self.screen.blit(titleSurface, (20 + 50 * self.sprite_kef, 30 + 50 * self.sprite_kef))
        self.screen.blit(self.chestImageSurface, (self.screen_width - 50 * self.sprite_kef - 10, 10))