import pygame
import random


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
        self.chestImageSurface = pygame.Surface((size, round(50 * sprite_kef)), pygame.SRCALPHA)
        self.chestImageSurface.blit(chestImage, (0, 0))
        self.chest_rect = self.chestImageSurface.get_rect(topleft=(self.screen_width - 50 * self.sprite_kef - 10,
                                                                   self.screen_height - 45 * self.sprite_kef - 10))

        self.screen = screen
        self.font = pygame.font.SysFont('Avenir Next', round(26 * self.screen_width / 1440))
        self.fontTitle = pygame.font.SysFont('SFCompactItalic', 42)
        self.enemyNameFont = pygame.font.SysFont('SFCompact', 16)

        self.player_mark = pygame.image.load('static/Player_mark.png')
        self.enemy_mark = pygame.image.load('static/Enemy_mark.png')

        self.inventory = []
        self.current_item = 0
        self.inventory_visible = False
        self.item_rects = []
        self.bought_items_interface = []
        self.keys_count = 0
        self.cards_count = 0
        self.sprite = None
        self.draw_bs_count = 0
        self.last_cards = 0
        self.chest = None
        self.draw_bs = False
        self.cards_mov_x = 0
        self.cards_mov_y = 0

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

    def add_dicts(self, lib, bs):
        self.item_dict = {**lib, **bs, **{'V': 'static/potion1.png',
                             'G': 'static/potion2.png',
                             'Y': 'static/potion3.png'}}

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
        titleSurface = self.font.render(f'{round(hp, 2)}/{round(max_hp, 2)}', False, (0, 255, 0))
        self.screen.blit(titleSurface, (40 + 50 * self.sprite_kef, 30))
        self.screen.blit(self.hpBarSurface, (20 + 50 * self.sprite_kef, 25))
        self.screen.blit(self.powerImageSurface, (10, 20 + 50 * self.sprite_kef))
        titleSurface = self.font.render(str(round(power, 2)), False, (0, 255, 0))
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

    def draw_lvl_progress_time(self, time):
        time_to = self.fontTitle.render(f'time to prepare: {round(time / 60)}', False, (12, 255, 17))
        pos_midtop = time_to.get_rect(topleft=(self.screen_width // 3, 10))
        self.screen.blit(time_to, pos_midtop)

    def draw_enemy_health(self, hp, max_hp):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.screen_width - self.hpBarWidth - 7, 28, (hp / max_hp) * self.hpBarWidth - 6,
                          self.hpBarHeight - 6))
        pygame.draw.rect(self.screen, (64, 128, 255),
                         (self.screen_width - self.hpBarWidth - 7, 28, self.hpBarWidth - 6,
                          self.hpBarHeight - 6), 4)
        titleSurface = self.font.render(f'{round(hp, 2)}/{round(max_hp, 2)}', False, (0, 255, 0))
        pos = titleSurface.get_rect(midleft=(self.screen_width - self.hpBarWidth, 28 + self.hpBarHeight // 2))
        self.screen.blit(titleSurface, pos)

    def draw_names(self, pos_enemy, pos_player):
        pos1 = self.player_mark.get_rect(midbottom=pos_player)
        pos2 = self.enemy_mark.get_rect(midbottom=pos_enemy)
        self.screen.blit(self.player_mark, pos1)
        self.screen.blit(self.enemy_mark, pos2)

    def add_inventory_librarian(self, bought_items, all_items):
        for i in bought_items:
            if i not in self.bought_items_interface:
                self.bought_items_interface.append(i)
                self.inventory.append(all_items[i])

    def add_inventory_blacksmith(self, bought_items, all_items):
        for i in bought_items:
            if i not in self.bought_items_interface:
                self.bought_items_interface.append(i)
                self.inventory.append(all_items[i])

    def add_inventory_keys(self, bought_items, all_items):
        for i in bought_items:
            if i not in self.bought_items_interface:
                self.bought_items_interface.append(i)
                self.inventory.append(all_items[i])

    def add_inventory_potions(self, potion, all_potions):
        if potion.cell not in self.bought_items_interface:
            self.inventory.append(all_potions[potion.cell])
        self.bought_items_interface.append(potion.cell)

    def add_keys(self, keys, sprite):
        self.sprite = sprite
        self.keys_count = keys
        if 'static/chest_key.png' not in self.inventory:
            self.inventory.append('static/chest_key.png')

    def add_blacksmith_card(self, sprite, chest):
        self.sprite = sprite
        self.chest = chest
        if 'static/blacksmith_card.png' not in self.inventory:
            self.inventory.append('static/blacksmith_card.png')
        cards = random.randint(1, 5)
        self.last_cards = cards
        sprite['b_cards'] += cards
        self.cards_count += cards
        self.update_blacksmith_cards()
        self.draw_bs = True

    def draw_bs_cards_got(self):
        text = f'+{self.last_cards}'
        bs_cards_count_size = round((50 * self.screen_width) / 1536)
        newFont = pygame.font.SysFont('SFCompact', bs_cards_count_size)
        txt_surf = newFont.render(text, False, (255, 183, 0))
        self.screen.blit(txt_surf, (self.chest.rect.x - self.chest.rect.w // 3 + self.cards_mov_x * self.draw_bs_count,
                                    self.chest.rect.y + self.cards_mov_y * self.draw_bs_count))

        itemImage = pygame.transform.scale(pygame.image.load('static/blacksmith_card.png'),
                                           (round(25 * self.sprite_kef) - 6, round(25 * self.sprite_kef) - 6))
        self.itemImageSurface = pygame.Surface((round(25 * self.sprite_kef), round(25 * self.sprite_kef)),
                                               pygame.SRCALPHA)
        self.itemImageSurface.blit(itemImage, (0, 0))
        self.screen.blit(self.itemImageSurface,
                         ((self.chest.rect.x + self.chest.rect.w // 2 + self.cards_mov_x * self.draw_bs_count,
                           self.chest.rect.y + self.cards_mov_y * self.draw_bs_count)))
        if self.screen_width - self.chest.rect.x < self.cards_mov_x * self.draw_bs_count + self.chest_rect.w or \
                self.screen_height - self.chest.rect.y < self.cards_mov_y * self.draw_bs_count + self.chest_rect.h:
            self.draw_bs_count = 0
            self.draw_bs = False
            self.cards_mov_x = 0
            self.cards_mov_y = 0

    def check_draw_bs(self):
        if self.draw_bs:
            self.draw_bs_count += 1
            if self.draw_bs_count == 1:
                self.cards_mov_x = round((self.screen_width - self.chest.rect.x) / 100)
                self.cards_mov_y = round((self.screen_height - self.chest.rect.y) / 100)
            else:
                self.draw_bs_cards_got()

    def update_blacksmith_cards(self):
        if self.sprite:
            self.cards_count = self.sprite['b_cards']
            if self.cards_count == 0:
                try:
                    self.inventory.remove('static/blacksmith_card.png')
                except:
                    pass

    def update_chest_keys(self):
        if self.sprite:
            self.keys_count = self.sprite['keys']
            if self.keys_count == 0:
                try:
                    self.inventory.remove('static/chest_key.png')
                except:
                    pass

    def draw_inventory(self):
        self.update_chest_keys()
        self.update_blacksmith_cards()
        self.check_draw_bs()
        if self.inventory_visible:
            for i, item in enumerate(self.inventory):
                itemImage = pygame.transform.scale(pygame.image.load(item),
                                                   (round(50 * self.sprite_kef) - 12,
                                                    round(50 * self.sprite_kef) - 12))
                self.itemImageSurface = pygame.Surface((round(50 * self.sprite_kef), round(50 * self.sprite_kef)),
                                                       pygame.SRCALPHA)
                if i == self.current_item:
                    pygame.draw.rect(self.itemImageSurface, (0, 255, 0), (0, 0, round(50 * self.sprite_kef), round(50 * self.sprite_kef)), 6, 4)
                self.itemImageSurface.blit(itemImage, (6, 6))

                if item == 'static/chest_key.png':
                    text = f'{self.keys_count}'
                elif item == 'static/blacksmith_card.png':
                    text = f'{self.cards_count}'
                else:
                    key = list(self.item_dict.keys())[list(self.item_dict.values()).index(item)]
                    text = str(self.bought_items_interface.count(key))
                newFont = pygame.font.SysFont('SFCompact', round((20 * self.screen_width) / 1536))
                txt_surf = newFont.render(text, False, (0, 255, 0))
                self.itemImageSurface.blit(txt_surf, (10, 10))

                self.screen.blit(self.itemImageSurface,
                                     ((self.screen_width - 50 * self.sprite_kef * (i + 2) - 10 * (i + 2),
                                                              self.screen_height - 45 * self.sprite_kef - 10)))

                self.item_rect = self.itemImageSurface.get_rect(topleft=(self.screen_width - 50 * self.sprite_kef * (i + 2) - 10 * (i + 2),
                                                                             self.screen_height - 45 * self.sprite_kef - 10))
                if i + 1 > len(self.item_rects):
                    self.item_rects.append(self.item_rect)

    def show_inventory(self, arg=True):
        if arg:
            if self.inventory_visible:
                self.inventory_visible = False
            else:
                self.inventory_visible = True
        else:
            self.inventory_visible = True

    def check_inv_change_key(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_TAB]:
                    self.show_inventory()
                if keys[pygame.K_RIGHT]:
                    self.current_item -= 1
                    if self.current_item < 0:
                        self.current_item = len(self.inventory) - 1
                if keys[pygame.K_LEFT]:
                    self.current_item += 1
                    if self.current_item > len(self.inventory) - 1:
                        self.current_item = 0

    def prepare_for_main(self):
        try:
            self.inventory.remove('static/blacksmith_card.png')
        except:
            pass
        try:
            self.inventory.remove('static/chest_key.png')
        except:
            pass