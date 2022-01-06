import random

import pygame
from map_preparation_settings import level1_map


npcImage = pygame.image.load('static/npcNormal2_64x64-export.png').convert_alpha()
npcLibrarian = pygame.image.load('static/librarian.png').convert_alpha()
fontTitle = pygame.font.SysFont('SFCompact', 14)

npcDisc = [
    {
        'name': 'librarian',
        'width': 128,
        'height': 128,
    },
    {
        'name': 'blacksmith',
        'width': 128,
        'height': 128,
    }
]


class BlackSmith(pygame.sprite.Sprite):
    def __init__(self, pos, count, sc, hero_name):
        super().__init__()
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.name = npcDisc[count]['name']
        self.screen = sc
        re_size = (self.h / len(level1_map)) / 64
        self.width = round(npcDisc[count]['width'] * re_size)
        self.height = round(npcDisc[count]['height'] * re_size)

        self.images = []
        self.images.append(npcImage)

        self.count = 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(self.images[int(self.count)], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - self.height // 2))

        self.items = dict()
        if hero_name == 'Hero1':
            self.items = {'1_bs': 'static/red_gem.png',
                          '2_bs': 'static/yellow_gem.png'
                          }
        if hero_name == 'Hero3':
            self.items = {'1_bs': 'static/hero3-bs-item1.png',
                          '2_bs': 'static/yellow_gem.png'
                          }

        self.bought_items = []
        self.purchase_done = False

    def show_msg(self):
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.msg_w = round((740 * self.w) / 1536)
        self.msg_h = round((400 * self.h) / 864)
        self.msg_x = self.w // 2 - self.msg_w // 2
        self.msg_y = 10
        self.msg_space = round((40 * self.w) / 1563)

        self.icon_w = round((70 * self.w) / 1563)
        self.icon_h = self.icon_w
        self.icon_y = self.msg_h // 3 - self.icon_h // 4 + self.msg_y

        self.icon_1_x = self.msg_x + self.msg_w // 2 - self.icon_w - self.msg_space
        self.icon_2_x = self.msg_x + self.msg_w // 2 + self.msg_space

        self.info_x = self.msg_x + round((140 * self.w) / 1536)
        self.info_y = self.msg_y + self.msg_h // 2
        self.info_w = self.msg_w - round((280 * self.w) / 1536)
        self.info_h = self.msg_h // 2 - round((80 * self.w) / 1536)

        msgImage = pygame.transform.scale(pygame.image.load('static/Talk-cloud.png').convert_alpha(), (self.msg_w, self.msg_h))
        self.screen.blit(msgImage, (self.msg_x, self.msg_y))

        first = pygame.Surface((self.icon_w, self.icon_h))
        if '1_bs' not in self.bought_items:
            first_img = pygame.transform.scale(pygame.image.load(self.items['1_bs']), (self.icon_w, self.icon_h))
            first.blit(first_img, (0, 0))
        else:
            first_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            first.blit(first_img, (0, 0))
        self.btn_first = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_1_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(first, (self.icon_1_x, self.icon_y))

        second = pygame.Surface((self.icon_w, self.icon_h))
        if '2_bs' not in self.bought_items:
            second_img = pygame.transform.scale(pygame.image.load(self.items['2_bs']), (self.icon_w, self.icon_h))
            second.blit(second_img, (0, 0))
        else:
            second_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            second.blit(second_img, (0, 0))
        self.btn_second = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_2_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(second, (self.icon_2_x, self.icon_y))

        pygame.draw.rect(self.screen, (66, 49, 137),
                         (self.info_x, self.info_y, self.info_w, self.info_h), round((10 * self.w) / 1536), 10)

        self.card_size = round(((self.icon_w / 2) * self.w) / 1536)
        self.card_x = 0

        font = pygame.font.SysFont('Avenir Next', round((50 * self.w) / 1536))

        for i in range(2):
            if i == 0:
                self.text_x = self.msg_x + self.msg_w / 2 - self.icon_w - self.msg_space + round((10 * self.w) / 1536)
                self.card_x = self.msg_x + self.msg_w / 2 - self.icon_w - self.msg_space + self.card_size
            else:
                self.text_x = self.msg_x + self.msg_w / 2 + self.msg_space + round((10 * self.w) / 1536)
                self.card_x = self.msg_x + self.msg_w / 2 + self.msg_space + self.card_size
            card_img = pygame.transform.scale(pygame.image.load('static/blacksmith_card.png'),
                                              (self.card_size, self.card_size))
            self.screen.blit(card_img, (self.card_x, self.msg_y + round((76 * self.h) / 864)))

            price = font.render('7', True, (255, 255, 255))
            self.screen.blit(price, (self.text_x, self.msg_y + round((80 * self.h) / 864)))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def check_show_info(self, is_on_check):
        mx, my = pygame.mouse.get_pos()
        if not is_on_check:
            is_on_check = True
            if self.btn_first.collidepoint((mx, my)):
                self.show_info('1_bs')
            elif self.btn_second.collidepoint((mx, my)):
                self.show_info('2_bs')
            else:
                self.show_info(False)
        else:
            is_on_check = False

    def check_click(self, player):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.btn_first.collidepoint((mx, my)):
                    self.plus_first(player)
                elif self.btn_second.collidepoint((mx, my)):
                    self.plus_second(player)

    def show_info(self, arg):
        if not arg:
            font = pygame.font.SysFont('Avenir Next', round((50 * self.w) / 1536))
            info = font.render('', True, (255, 255, 255))
            self.screen.blit(info, (self.info_x + round((10 * self.w) / 1536), self.info_y + round((10 * self.h) / 864)))
        else:
            font = pygame.font.SysFont('Avenir Next', round((50 * self.w) / 1536))
            info = font.render(arg, True, (255, 255, 255))
            self.screen.blit(info,
                             (self.info_x + round((10 * self.w) / 1536), self.info_y + round((10 * self.h) / 864)))

    def plus_first(self, player):
        if player['b_cards'] - 7 >= 0 and '1_bs' not in self.bought_items:
            player['b_cards'] -= 7
            self.bought_items.append('1_bs')
            self.purchase_done = True

    def plus_second(self, player):
        if player['b_cards'] - 7 >= 0 and '2_bs' not in self.bought_items:
            player['b_cards'] -= 7
            self.bought_items.append('2_bs')
            self.purchase_done = True


class Librarian(pygame.sprite.Sprite):
    def __init__(self, pos, count, sc, hero_name):
        super().__init__()
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.name = npcDisc[count]['name']
        self.screen = sc
        re_size = (self.h / len(level1_map)) / 64
        self.width = round(npcDisc[count]['width'] * re_size)
        self.height = round(npcDisc[count]['height'] * re_size)

        self.images = []
        for i in range(1, 13):
            self.images.append(pygame.transform.scale(
                pygame.image.load(f'static/npc_librarian/Shop_new_book{str(i)}.png').convert_alpha(),
                (self.width, self.height)))
        self.count = 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(self.images[int(self.count)], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - self.height // 2))

        if hero_name == 'Hero1':
            self.items = {'1_lib': 'static/hero1_librarian/upgrade_power.png',
                          '2_lib': 'static/hero1_librarian/upgrade_hp.png',
                          '3_lib': 'static/hero1_librarian/hero1_q_hp_boost.png',
                          '4_lib': 'static/hero1_librarian/e_hero1_freeze_time_upgrade.png',
                          '5_lib': 'static/hero1_librarian/hero1_e_power_keff.png'}
        if hero_name == 'Hero3':
            self.items = {'1_lib': 'static/yellow_gem.png',
                          '2_lib': 'static/green_gem.png',
                          '3_lib': 'static/blue_gem.png',
                          '4_lib': 'static/red_gem.png',
                          '5_lib': 'static/yellow_gem.png'}

        self.hero_name = hero_name

        self.bought_items = []
        self.purchase_done = False

    def update_npc(self):
        if self.count >= len(self.images) - 1:
            self.count = 0
        self.count += 0.25
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(self.images[int(self.count)], (self.width, self.height)), (0, 0))

    def show_msg(self):
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.msg_w = round((740 * self.w) / 1536)
        self.msg_h = round((400 * self.h) / 864)
        self.msg_x = self.w // 2 - self.msg_w // 2
        self.msg_y = 10
        self.msg_space = round((40 * self.w) / 1563)

        self.icon_w = round((70 * self.w) / 1563)
        self.icon_h = self.icon_w
        self.icon_y = self.msg_h // 3 - self.icon_h // 4 + self.msg_y

        self.icon_a_x = self.msg_x + self.msg_space * 3
        self.icon_h_x = self.msg_x + self.msg_space * 4 + self.icon_w
        self.icon_q_x = self.msg_x + self.msg_space * 5 + self.icon_w * 2
        self.icon_e_x = self.msg_x + self.msg_space * 6 + self.icon_w * 3
        self.icon_k_x = self.msg_x + self.msg_space * 7 + self.icon_w * 4

        self.info_x = self.msg_x + round((140 * self.w) / 1536)
        self.info_y = self.msg_y + self.msg_h // 2
        self.info_w = self.msg_w - round((280 * self.w) / 1536)
        self.info_h = self.msg_h // 2 - round((80 * self.w) / 1536)

        msgImage = pygame.transform.scale(pygame.image.load('static/Talk-cloud.png').convert_alpha(), (self.msg_w, self.msg_h))
        self.screen.blit(msgImage, (self.msg_x, self.msg_y))

        attack = pygame.Surface((self.icon_w, self.icon_h))
        if '1_lib' not in self.bought_items:
            attack_img = pygame.transform.scale(pygame.image.load(self.items['1_lib']), (self.icon_w, self.icon_h))
            attack.blit(attack_img, (0, 0))
        else:
            attack_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            attack.blit(attack_img, (0, 0))
        self.btn_a = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_a_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(attack, (self.icon_a_x, self.icon_y))

        health = pygame.Surface((self.icon_w, self.icon_h))
        if '2_lib' not in self.bought_items:
            health_img = pygame.transform.scale(pygame.image.load(self.items['2_lib']), (self.icon_w, self.icon_h))
            health.blit(health_img, (0, 0))
        else:
            health_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            health.blit(health_img, (0, 0))
        self.btn_h = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_h_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(health, (self.icon_h_x, self.icon_y))

        q = pygame.Surface((self.icon_w, self.icon_h))
        if '3_lib' not in self.bought_items:
            q_img = pygame.transform.scale(pygame.image.load(self.items['3_lib']), (self.icon_w, self.icon_h))
            q.blit(q_img, (0, 0))
        else:
            q_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            q.blit(q_img, (0, 0))
        self.btn_q = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_q_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(q, (self.icon_q_x, self.icon_y))

        e = pygame.Surface((self.icon_w, self.icon_h))
        if '4_lib' not in self.bought_items:
            e_img = pygame.transform.scale(pygame.image.load(self.items['4_lib']), (self.icon_w, self.icon_h))
            e.blit(e_img, (0, 0))
        else:
            e_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            e.blit(e_img, (0, 0))
        self.btn_e = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_e_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(e, (self.icon_e_x, self.icon_y))

        k = pygame.Surface((self.icon_w, self.icon_h))
        if '5_lib' not in self.bought_items:
            k_img = pygame.transform.scale(pygame.image.load(self.items['5_lib']), (self.icon_w, self.icon_h))
            k.blit(k_img, (0, 0))
        else:
            k_img = pygame.transform.scale(pygame.image.load('static/bs-ItemNone.png'), (self.icon_w, self.icon_h))
            k.blit(k_img, (0, 0))
        self.btn_k = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_k_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(k, (self.icon_k_x, self.icon_y))

        pygame.draw.rect(self.screen, (66, 49, 137),
                         (self.info_x, self.info_y, self.info_w, self.info_h), round((10 * self.w) / 1536), 10)

        self.gem_size = round(((self.icon_w / 2) * self.w) / 1536)
        self.gem_x = 0

        font = pygame.font.SysFont('Avenir Next', round((50 * self.w) / 1536))

        for i in range(5):
            self.text_x = self.msg_x + self.msg_space * (i + 3) + self.icon_w * i + round((10 * self.w) / 1536)
            self.gem_x = self.msg_x + self.msg_space * (i + 3) + self.icon_w * i + self.gem_size
            gold_img = pygame.transform.scale(pygame.image.load('static/green_gem.png'),
                (self.gem_size, self.gem_size))
            self.screen.blit(gold_img, (self.gem_x, self.msg_y + round((76 * self.h) / 864)))

            price = font.render('5', True, (255, 255, 255))
            self.screen.blit(price, (self.text_x, self.msg_y + round((80 * self.h) / 864)))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def check_show_info(self, is_on_check):
        mx, my = pygame.mouse.get_pos()
        if not is_on_check:
            is_on_check = True
            if self.btn_h.collidepoint((mx, my)):
                info = 'increase the maximum health reserve by 10%' if self.hero_name == 'Hero1' else '1'
                self.show_info(info, 1)
            elif self.btn_a.collidepoint((mx, my)):
                info = 'increase attack power by 4' if self.hero_name == 'Hero1' else '2'
                self.show_info(info, 1)
            elif self.btn_q.collidepoint((mx, my)):
                info = '30% increase in recoverable health after using the super (buttonQ)' if self.hero_name == 'Hero1' else '3'
                self.show_info(info, 2)
            elif self.btn_e.collidepoint((mx, my)):
                info = "increase the enemy's deceleration time by 10% after hitting the enemy with the " \
                       "second attack (E button)" if self.hero_name == 'Hero1' else '4'
                self.show_info(info, 2)
            elif self.btn_k.collidepoint((mx, my)):
                info = 'increase the force coefficient of a normal attack during the action of super by 23% (Q button)' if self.hero_name == 'Hero1' else '5'
                self.show_info(info, 2)
            else:
                self.show_info(False, 0)
        else:
            is_on_check = False

    def check_click(self, player):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.btn_h.collidepoint((mx, my)):
                    self.plus_health(player)
                elif self.btn_a.collidepoint((mx, my)):
                    self.plus_attack(player)
                elif self.btn_q.collidepoint((mx, my)):
                    self.plus_q(player)
                elif self.btn_e.collidepoint((mx, my)):
                    self.plus_e(player)
                elif self.btn_k.collidepoint((mx, my)):
                    self.plus_k(player)

    def show_info(self, arg, strings):
        if not arg:
            font = pygame.font.SysFont('Avenir Next', round((25 * self.w) / 1536))
            info = font.render('', True, (255, 255, 255))
            self.screen.blit(info, (self.info_x + round((15 * self.w) / 1536), self.info_y + round((15 * self.h) / 864)))
        else:
            font = pygame.font.SysFont('Avenir Next', round((25 * self.w) / 1536))
            if strings > 1:
                arg = arg.split(' ')
                info1 = font.render(' '.join(arg[:len(arg) // 2]), True, (255, 255, 255))
                info2 = font.render(' '.join(arg[len(arg) // 2:]), True, (255, 255, 255))
            else:
                info1 = font.render(arg, True, (255, 255, 255))
                info2 = font.render('', True, (255, 255, 255))
            self.screen.blit(info1,
                             (self.info_x + round((15 * self.w) / 1536), self.info_y + round((15 * self.h) / 864)))
            self.screen.blit(info2,
                             (self.info_x + round((15 * self.w) / 1536), self.info_y + round((45 * self.h) / 864)))

    def plus_attack(self, player):
        if player['gold'] - 5 >= 0 and '1_lib' not in self.bought_items:
            player['gold'] -= 5
            self.bought_items.append('1_lib')
            self.purchase_done = True

    def plus_health(self, player):
        if player['gold'] - 5 >= 0 and '2_lib' not in self.bought_items:
            player['gold'] -= 5
            self.bought_items.append('2_lib')
            self.purchase_done = True

    def plus_q(self, player):
        if player['gold'] - 5 >= 0 and '3_lib' not in self.bought_items:
            player['gold'] -= 5
            self.bought_items.append('3_lib')
            self.purchase_done = True

    def plus_e(self, player):
        if player['gold'] - 5 >= 0 and '4_lib' not in self.bought_items:
            player['gold'] -= 5
            self.bought_items.append('4_lib')
            self.purchase_done = True

    def plus_k(self, player):
        if player['gold'] - 5 >= 0 and '5_lib' not in self.bought_items:
            player['gold'] -= 5
            self.bought_items.append('5_lib')
            self.purchase_done = True

    def update_player_characteristics(self, sprite):
        if self.bought_items[-1] == '1_lib':
            sprite.power += 10

        if self.bought_items[-1] == '2_lib':
            sprite.maxHp += 10
            sprite.hp += 10

        if self.bought_items[-1] == '3_lib':
            sprite.q_hp_recovery += 5

        if self.bought_items[-1] == '4_lib':
            sprite.e_time_speed_to_low += 0.4

        if self.bought_items[-1] == '5_lib':
            sprite.attack_power_kef += 0.1