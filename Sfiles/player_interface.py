import pygame
import time


class Interface:
    def __init__(self, screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        sprite_kef = screen_width / 1000
        self.sprite_kef = sprite_kef
        hpImage = pygame.transform.scale(pygame.image.load('static/healthIconMenu.png'),
                                         (round(50 * sprite_kef), round(50 * sprite_kef)))
        self.hpBarWidth = round(160 * sprite_kef)
        self.hpBarHeight = round(32 * sprite_kef)
        hpBar = pygame.transform.scale(pygame.image.load('static/hpBar.png'),
                                       (self.hpBarWidth, self.hpBarHeight))
        self.hpImageSurface = pygame.Surface((round(50 * sprite_kef), round(50 * sprite_kef)), pygame.SRCALPHA)
        self.hpImageSurface.blit(hpImage, (0, 0))
        self.hpBarSurface = pygame.Surface((self.hpBarWidth, self.hpBarHeight), pygame.SRCALPHA)
        self.hpBarSurface.blit(hpBar, (0, 0))

        self.hpBarEnemySurface = pygame.Surface((self.hpBarWidth, self.hpBarHeight), pygame.SRCALPHA)
        self.hpBarEnemySurface.blit(hpBar, (0, 0))

        powerImage = pygame.transform.scale(pygame.image.load('static/attackIconMenu.png'),
                                            (round(50 * sprite_kef), round(50 * sprite_kef)))
        self.powerImageSurface = pygame.Surface((round(50 * sprite_kef), round(50 * sprite_kef)), pygame.SRCALPHA)
        self.powerImageSurface.blit(powerImage, (0, 0))

        chestImage = pygame.transform.scale(pygame.image.load('static/chest.png'),
                                            (round(50 * sprite_kef), round(45 * sprite_kef)))
        self.chestImageSurface = pygame.Surface((round(50 * sprite_kef), round(45 * sprite_kef)), pygame.SRCALPHA)
        self.chestImageSurface.blit(chestImage, (0, 0))
        self.chest_rect = self.chestImageSurface.get_rect(topleft=(self.screen_width - 50 * self.sprite_kef - 10,
                                                                   self.screen_height - 45 * self.sprite_kef - 10))

        self.screen = screen
        self.font = pygame.font.SysFont('Avenir Next', round(26 * self.screen_width / 1440))
        self.fontTitle = pygame.font.SysFont('SFCompactItalic', 42)

        self.inventory = []
        self.current_item = 0
        self.inventory_visible = False

        self.item_rects = []

        self.bought_items_interface = []

    def update_screen_size(self, w, h):
        self.screen_width = w
        self.screen_height = h

    def draw(self, hp, max_hp, power):
        self.screen.blit(self.hpImageSurface, (10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (23 + 50 * self.sprite_kef, 28, (hp / max_hp) * self.hpBarWidth - 6, self.hpBarHeight - 6))
        titleSurface = self.font.render(f'{hp}/{max_hp}', False, (0, 255, 0))
        self.screen.blit(titleSurface, (40 + 50 * self.sprite_kef, 30))
        self.screen.blit(self.hpBarSurface, (20 + 50 * self.sprite_kef, 25))
        self.screen.blit(self.powerImageSurface, (10, 20 + 50 * self.sprite_kef))
        titleSurface = self.font.render(str(power), False, (0, 255, 0))
        self.screen.blit(titleSurface, (20 + 50 * self.sprite_kef, 30 + 50 * self.sprite_kef))
        self.screen.blit(self.chestImageSurface, (self.screen_width - 50 * self.sprite_kef - 10,
                                                  self.screen_height - 45 * self.sprite_kef - 10))

    def draw_enemy_health(self, hp, max_hp):
        titleSurface = self.fontTitle.render("VS", False, (12, 255, 17))
        pos = titleSurface.get_rect(midtop=(self.screen_width // 2, 10))
        self.screen.blit(titleSurface, pos)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.screen_width - self.hpBarWidth - 7, 28, (hp / max_hp) * self.hpBarWidth - 6,
                          self.hpBarHeight - 6))
        pygame.draw.rect(self.screen, (64, 128, 255),
                         (self.screen_width - self.hpBarWidth - 7, 28, self.hpBarWidth - 6,
                          self.hpBarHeight - 6), 4)
        titleSurface = self.font.render(f'{hp}/{max_hp}', False, (0, 255, 0))
        pos = titleSurface.get_rect(midleft=(self.screen_width - self.hpBarWidth, 28 + self.hpBarHeight // 2))
        self.screen.blit(titleSurface, pos)

    def add_inventory(self, bought_items, all_items):
        for i in bought_items:
            if i not in self.bought_items_interface:
                self.bought_items_interface.append(i)
                self.inventory.append(all_items[i])

    def show_inventory(self, arg=True):
        if arg:
            if self.inventory_visible:
                self.inventory_visible = False
            else:
                self.inventory_visible = True
        else:
            self.inventory_visible = True

    def draw_inventory(self):
        if self.inventory_visible:
            for i, item in enumerate(self.inventory[-1::-1]):
                itemImage = pygame.transform.scale(pygame.image.load(item),
                                                    (round(50 * self.sprite_kef) - 6, round(50 * self.sprite_kef) - 6))
                self.itemImageSurface = pygame.Surface((round(50 * self.sprite_kef), round(50 * self.sprite_kef)),
                                                       pygame.SRCALPHA)
                if i == self.current_item:
                    self.itemImageSurface.fill((0, 255, 0))
                self.itemImageSurface.blit(itemImage, (3, 3))
                self.screen.blit(self.itemImageSurface,
                                 ((self.screen_width - 50 * self.sprite_kef * (i + 2) - 10 * (i + 2),
                                                          self.screen_height - 45 * self.sprite_kef - 10)))
                self.item_rect = self.itemImageSurface.get_rect(topleft=(self.screen_width - 50 * self.sprite_kef * (i + 2) - 10 * (i + 2),
                                                                         self.screen_height - 45 * self.sprite_kef - 10))
                if i + 1 > len(self.item_rects):
                    self.item_rects.append(self.item_rect)

    def check_item_choice(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, rect in enumerate(self.item_rects):
                    if rect.collidepoint((mx, my)):
                        self.current_item = i
