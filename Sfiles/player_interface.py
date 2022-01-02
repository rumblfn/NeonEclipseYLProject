import pygame
import time


class Interface:
    def __init__(self, screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        sprite_kef = screen_width / 1000
        self.sprite_kef = sprite_kef
        size = round(50 * sprite_kef)
        hpImage = pygame.transform.scale(pygame.image.load('static/healthIconMenu.png'),
                                         (size, size))
        self.hpBarWidth = round(160 * sprite_kef)
        self.hpBarHeight = round(32 * sprite_kef)
        hpBar = pygame.transform.scale(pygame.image.load('static/hpBar.png'),
                                       (self.hpBarWidth, self.hpBarHeight))
        self.hpImageSurface = pygame.Surface((size, size), pygame.SRCALPHA)
        self.hpImageSurface.blit(hpImage, (0, 0))
        self.hpBarSurface = pygame.Surface((self.hpBarWidth, self.hpBarHeight), pygame.SRCALPHA)
        self.hpBarSurface.blit(hpBar, (0, 0))

        self.hpBarEnemySurface = pygame.Surface((self.hpBarWidth, self.hpBarHeight), pygame.SRCALPHA)
        self.hpBarEnemySurface.blit(hpBar, (0, 0))

        powerImage = pygame.transform.scale(pygame.image.load('static/attackIconMenu.png'),
                                            (size, size))
        self.powerImageSurface = pygame.Surface((size, size), pygame.SRCALPHA)
        self.powerImageSurface.blit(powerImage, (0, 0))

        chestImage = pygame.transform.scale(pygame.image.load('static/chest.png'),
                                            (size, size))
        self.chestImageSurface = pygame.Surface((size, round(45 * sprite_kef)), pygame.SRCALPHA)
        self.chestImageSurface.blit(chestImage, (0, 0))
        self.chest_rect = self.chestImageSurface.get_rect(topleft=(self.screen_width - 50 * self.sprite_kef - 10,
                                                                   self.screen_height - 45 * self.sprite_kef - 10))

        self.screen = screen
        self.font = pygame.font.SysFont('Avenir Next', round(26 * self.screen_width / 1440))
        self.fontTitle = pygame.font.SysFont('SFCompactItalic', 42)

        self.inventory = []
        self.current_item = 0
        self.inventory_visible = False
        for i in range(5):
            self.add_inventory('')

        self.item_rects = []

        self.aa_image_normal = pygame.transform.scale(pygame.image.load('static/lmbIconMenu.png'), (size, size))
        self.e_image_normal = pygame.transform.scale(pygame.image.load('static/buttonE.png'), (size, size))
        self.q_image_normal = pygame.transform.scale(pygame.image.load('static/buttonQ.png'), (size, size))
        self.aa_image = pygame.transform.scale(pygame.image.load('static/lmbIconMenu.png').convert(),
                                               (size, size))
        self.e_image = pygame.transform.scale(pygame.image.load('static/buttonE.png').convert(),
                                               (size, size))
        self.q_image = pygame.transform.scale(pygame.image.load('static/buttonQ.png').convert(),
                                               (size, size))
        self.aa_image.set_alpha(128)
        self.e_image.set_alpha(128)
        self.q_image.set_alpha(128)
        self.pos1 = self.aa_image.get_rect(bottomleft=(20, self.screen_height - 20))
        self.pos2 = self.e_image.get_rect(bottomleft=(40 + self.aa_image.get_width(), self.screen_height - 20))
        self.pos3 = self.q_image.get_rect(
            bottomleft=(60 + self.aa_image.get_width() + self.e_image.get_width(), self.screen_height - 20))
        self.pos1_center = self.pos1.center
        self.pos2_center = self.pos2.center
        self.pos3_center = self.pos3.center

    def draw_attacks_timers(self, time_aa, time_aa_max, time_e, time_e_max, time_q, time_q_max):
        t_a = round((time_aa_max - time_aa) / 60, 1)
        t_e = round((time_e_max - time_e) / 60, 1)
        t_q = round((time_q_max - time_q) / 60, 1)
        if t_a > 0:
            text1 = self.font.render(str(t_a), False, (0, 0, 255))
            text1_pos = text1.get_rect(center=self.pos1_center)
            self.screen.blit(self.aa_image, self.pos1)
            self.screen.blit(text1, text1_pos)
        else:
            self.screen.blit(self.aa_image_normal, self.pos1)
        if t_e > 0:
            text2 = self.font.render(str(t_e), False, (0, 0, 255))
            text2_pos = text2.get_rect(center=self.pos2_center)
            self.screen.blit(self.e_image, self.pos2)
            self.screen.blit(text2, text2_pos)
        else:
            self.screen.blit(self.e_image_normal, self.pos2)
        if t_q > 0:
            text3 = self.font.render(str(t_q), False, (0, 0, 255))
            text3_pos = text3.get_rect(center=self.pos3_center)
            self.screen.blit(self.q_image, self.pos3)
            self.screen.blit(text3, text3_pos)
        else:
            self.screen.blit(self.q_image_normal, self.pos3)

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

    def draw_game_progress(self, wins_player, wins_enemy):
        wins_text = self.fontTitle.render(wins_player, False, (0, 0, 255))
        vs = self.fontTitle.render("VS", False, (12, 255, 17))
        loses_text = self.fontTitle.render(wins_enemy, False, (0, 0, 255))
        pos_midtop = vs.get_rect(midtop=(self.screen_width // 2, 10))
        self.screen.blit(vs, pos_midtop)
        self.screen.blit(wins_text, (pos_midtop[0] - 50, pos_midtop[1]))
        self.screen.blit(loses_text, (pos_midtop[0] + 100, pos_midtop[1]))

    def draw_enemy_health(self, hp, max_hp):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.screen_width - self.hpBarWidth - 7, 28, (hp / max_hp) * self.hpBarWidth - 6,
                          self.hpBarHeight - 6))
        pygame.draw.rect(self.screen, (64, 128, 255),
                         (self.screen_width - self.hpBarWidth - 7, 28, self.hpBarWidth - 6,
                          self.hpBarHeight - 6), 4)
        titleSurface = self.font.render(f'{hp}/{max_hp}', False, (0, 255, 0))
        pos = titleSurface.get_rect(midleft=(self.screen_width - self.hpBarWidth, 28 + self.hpBarHeight // 2))
        self.screen.blit(titleSurface, pos)

    def add_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory_visible:
            self.inventory_visible = False
        else:
            self.inventory_visible = True

    def draw_inventory(self):
        if self.inventory_visible:
            for i, item in enumerate(self.inventory):
                itemImage = pygame.transform.scale(pygame.image.load('static/green_gem.png'),
                                                    (round(50 * self.sprite_kef), round(50 * self.sprite_kef)))
                self.itemImageSurface = pygame.Surface((round(50 * self.sprite_kef), round(50 * self.sprite_kef)),
                                                       pygame.SRCALPHA)
                if i == self.current_item:
                    self.itemImageSurface.fill((0, 255, 0, 50))
                self.itemImageSurface.blit(itemImage, (0, 0))
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
                        print(self.current_item)