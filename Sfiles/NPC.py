import random

import pygame
from map_preparation_settings import level1_map


npcImage = pygame.image.load('static/npcNormal2_64x64-export.png').convert_alpha()
npcLibrarian = pygame.image.load('static/librarian.png').convert_alpha()
fontTitle = pygame.font.SysFont('SFCompact', 14)

npcDisc = [
    {
        'name': 'blacksmith',
        'width': 128,
        'height': 128,
    },
    {
        'name': 'librarian',
        'width': 128,
        'height': 128,
    }
]


class BlackSmith(pygame.sprite.Sprite):
    def __init__(self, pos, count, sc):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = npcDisc[count]['name']
        self.screen = sc

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(npcDisc[count]['width'] * re_size)
        self.height = round(npcDisc[count]['height'] * re_size)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(npcImage, (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - self.height // 2))

    def show_msg(self):
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        msgImage = pygame.transform.scale(pygame.image.load('static/Talk-cloud.png').convert_alpha(),
                                          ((384 * w) // 1563,
                                           (128 * h) // 864))
        self.screen.blit(msgImage, (pygame.display.Info().current_w // 2 - 192, 10))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def check_click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.btn_a.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_health()
                elif self.btn_h.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_attack()


class Librarian(pygame.sprite.Sprite):
    def __init__(self, pos, count, sc):
        super().__init__()
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.name = npcDisc[count]['name']
        self.screen = sc

        re_size = (self.h / len(level1_map)) / 64
        self.width = round(npcDisc[count]['width'] * re_size)
        self.height = round(npcDisc[count]['height'] * re_size)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(npcLibrarian, (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - self.height // 2))

    def show_msg(self):
        self.h = pygame.display.Info().current_h
        self.w = pygame.display.Info().current_w
        self.msg_w = round((740 * self.w) / 1563)
        self.msg_h = round((200 * self.h) / 864)
        self.msg_x = self.w // 2 - self.msg_w // 2
        self.msg_y = 10
        self.msg_space = round((40 * self.w) / 1563)

        self.icon_w = round((100 * self.w) / 1563)
        self.icon_h = self.icon_w
        self.icon_y = self.msg_h // 2 - self.icon_h // 4 + self.msg_y

        self.icon_a_x = self.msg_x + self.msg_space
        self.icon_h_x = self.msg_x + self.msg_space * 2 + self.icon_w
        self.icon_q_x = self.msg_x + self.msg_space * 3 + self.icon_w * 2
        self.icon_e_x = self.msg_x + self.msg_space * 4 + self.icon_w * 3
        self.icon_k_x = self.msg_x + self.msg_space * 5 + self.icon_w * 4

        msgImage = pygame.transform.scale(pygame.image.load('static/Talk-cloud.png').convert_alpha(), (self.msg_w, self.msg_h))
        self.screen.blit(msgImage, (self.msg_x, self.msg_y))

        attack = pygame.Surface((self.icon_w, self.icon_h))
        attack_img = pygame.transform.scale(pygame.image.load('static/attackIconMenu.png'), (self.icon_w, self.icon_h))
        attack.blit(attack_img, (0, 0))
        self.btn_a = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_a_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(attack, (self.icon_a_x, self.icon_y))

        health = pygame.Surface((self.icon_w, self.icon_h))
        health_img = pygame.transform.scale(pygame.image.load('static/healthIconMenu.png'), (self.icon_w, self.icon_h))
        health.blit(health_img, (0, 0))
        self.btn_h = pygame.draw.rect(self.screen, (255, 255, 255), (self.icon_h_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(health, (self.icon_h_x, self.icon_y))

        q = pygame.Surface((self.icon_w, self.icon_h))
        q_img = pygame.transform.scale(pygame.image.load('static/buttonQ.png'), (self.icon_w, self.icon_h))
        q.blit(q_img, (0, 0))
        self.btn_q = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_q_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(q, (self.icon_q_x, self.icon_y))

        e = pygame.Surface((self.icon_w, self.icon_h))
        e_img = pygame.transform.scale(pygame.image.load('static/buttonE.png'), (self.icon_w, self.icon_h))
        e.blit(e_img, (0, 0))
        self.btn_e = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_e_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(e, (self.icon_e_x, self.icon_y))

        k = pygame.Surface((self.icon_w, self.icon_h))
        k_img = pygame.transform.scale(pygame.image.load('static/Harchok.png'), (self.icon_w, self.icon_h))
        k.blit(k_img, (0, 0))
        self.btn_k = pygame.draw.rect(self.screen, (255, 255, 255),
                                      (self.icon_k_x, self.icon_y, self.icon_w, self.icon_h))
        self.screen.blit(k, (self.icon_k_x, self.icon_y))

        self.gem_size = round(((self.icon_w // 2) * self.w) / 1536)
        self.gem_x = 0

        font = pygame.font.SysFont('Avenir Next', 60)
        col = (0, 0, 0)

        for i in range(5):
            self.gem_x = self.msg_x + self.msg_space * (i + 1) + self.icon_w * i + self.gem_size - round((10 * self.w) / 1536)
            self.text_x = self.msg_x + self.msg_space * (i + 1) + self.icon_w * i + round((10 * self.w) / 1536)
            gold_img = pygame.transform.scale(pygame.image.load('static/green_gem.png'),
                (self.gem_size, self.gem_size))
            self.screen.blit(gold_img, (self.gem_x, self.msg_y + self.msg_h - self.icon_y - 2 * self.gem_size))

            titleSurface = font.render(f'{i + 1}', True, col)
            self.screen.blit(titleSurface, (self.text_x, self.msg_y + self.msg_h - self.icon_y - 2 * self.gem_size + round((7 * self.w) / 1536)))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def check_click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.btn_h.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_health()
                elif self.btn_a.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_attack()
                elif self.btn_q.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_q()
                elif self.btn_e.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_e()
                elif self.btn_k.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed():
                        self.plus_k()

    def plus_health(self):
        print('+h')
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.icon_h_x, self.icon_y, self.icon_w, self.icon_h))

    def plus_attack(self):
        print('+a')
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.icon_a_x, self.icon_y, self.icon_w, self.icon_h))

    def plus_q(self):
        print('+q')
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.icon_q_x, self.icon_y, self.icon_w, self.icon_h))

    def plus_e(self):
        print('+e')
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.icon_e_x, self.icon_y, self.icon_w, self.icon_h))

    def plus_k(self):
        print('+k')
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.icon_k_x, self.icon_y, self.icon_w, self.icon_h))