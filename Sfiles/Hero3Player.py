import pygame
from map_preparation_settings import level1_map


class Player_hero3(pygame.sprite.Sprite):
    def __init__(self, pos, player_settings):
        super().__init__()
        self.block_moving = False

        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = player_settings['name']
        self.power = player_settings['attack power']
        self.maxHp = player_settings['maxHp']
        self.hp = player_settings['maxHp']
        self.started_pos = pos

        self.K_x = False
        self.Q_ACTIVE = False
        self.Q_ACTIVE_TIMER = 1200
        self.Q_TIMER = 400
        self.E_ACTIVE = False
        self.SHIELD_ACTIVE = False
        self.E_TIMER = 2400
        self.E_ACTIVE_TIMER = 600
        self.CURRENT_SPRITE = 0
        self.CURRENT_SPRITE_Q = 0
        self.CURRENT_SPRITE_E = 0
        self.SIDE = 'left'

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(64 * re_size) - 1
        self.height = round(64 * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        animations = {  # paths
            'left_walk': ['static/hero2animations/Run/Left/Paladin_run_left', 1, 2],  # + 14 + $ 1...2...14 + .png
            'right_walk': ['static/hero2animations/Run/Right/Paladin_run', 1, 2],
            'q_right_animation': ['static/hero2animations/Ult/Right/Paladin_ult', 1, 7],
            'q_left_animation': ['static/hero2animations/Ult/Left/Paladin_ult_left', 1, 7],
            'auto_attack_left': ['static/hero2animations/AA/Left/Paladin_aa_left', 1, 4],
            'auto_attack_right': ['static/hero2animations/AA/Right/Paladin_aa', 1, 4],
            'attack_e_right': ['static/hero2animations/E/Right/Paladin', 1, 12],
            'attack_e_left': ['static/hero2animations/E/Left/Paladin_E_left', 1, 12],
        }

        self.images = {'shield': pygame.transform.scale(pygame.image.load('static/hero2animations/Shield.png'),
                                                        (self.width, self.height))}
        for el in animations.keys():
            self.images[el] = []
            src = animations[el][0]
            number_of_last_image = animations[el][2]
            for i in range(1, number_of_last_image + 1):
                image = pygame.transform.scale(
                    pygame.image.load(f'{src}{i}.png').convert_alpha(),
                    (self.width, self.height))
                self.images[el].append(image)

        self.normal_image_left = self.images['attack_e_left'][0]
        self.normal_image_right = self.images['attack_e_right'][0]
        self.image.blit(self.normal_image_left, (0, 0))

        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(9 * WIDTH / 1440)
        self.speed = round(9 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True

        self.server_player = None

    def get_input(self):
        self.CURRENT_SPRITE += 0.2
        self.CURRENT_SPRITE_Q += 0.2
        keys = pygame.key.get_pressed()

        if self.Q_ACTIVE:
            self.Q_TIMER += 1
            if self.Q_TIMER >= 400:
                self.Q_ACTIVE = False
        if self.Q_ACTIVE_TIMER <= 1200:
            self.Q_ACTIVE_TIMER += 1

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.image.fill((0, 0, 0, 0))
            self.SIDE = 'right'
            if self.Q_ACTIVE:
                self.image.blit(self.images['q_right_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
            else:
                self.image.blit(self.images['right_walk'][int(self.CURRENT_SPRITE)], (0, 0))
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.image.fill((0, 0, 0, 0))
            if self.Q_ACTIVE:
                self.image.blit(self.images['q_left_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
            else:
                self.image.blit(self.images['left_walk'][int(self.CURRENT_SPRITE)], (0, 0))
            self.SIDE = 'left'
        else:
            self.direction.x = 0
            self.image.fill((0, 0, 0, 0))
            if self.SIDE == 'left':
                if self.Q_ACTIVE:
                    self.image.blit(self.images['q_left_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
                else:
                    self.image.blit(self.normal_image_left, (0, 0))
            else:
                if self.Q_ACTIVE:
                    self.image.blit(self.images['q_right_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
                else:
                    self.image.blit(self.normal_image_right, (0, 0))

        if self.SHIELD_ACTIVE:
            self.E_ACTIVE_TIMER += 1
            self.image.blit(self.images['shield'], (0, 0))
            if self.E_ACTIVE_TIMER >= 600:
                self.E_ACTIVE_TIMER = 0
                self.SHIELD_ACTIVE = False
        if not self.SHIELD_ACTIVE and self.E_TIMER <= 2400:
            self.E_TIMER += 1

        if self.CURRENT_SPRITE >= 0.8:
            self.CURRENT_SPRITE = 0
        if self.CURRENT_SPRITE_Q >= 5.8:
            self.CURRENT_SPRITE_Q = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if not self.direction.y:
            self.jump_bool = True
        if keys[pygame.K_e]:
            if self.E_TIMER >= 2400:
                self.block_moving = True
                self.E_ACTIVE = True
                self.E_TIMER = 0
        if keys[pygame.K_q]:
            if self.Q_ACTIVE_TIMER >= 1200:
                self.Q_ACTIVE = True
                self.Q_ACTIVE_TIMER = 0
                self.Q_TIMER = 0

    def start_e(self):
        self.CURRENT_SPRITE_E += 0.2
        self.image.fill((0, 0, 0, 0))
        try:
            if self.SIDE == 'left':
                self.image.blit(self.images['attack_e_right'][int(self.CURRENT_SPRITE_E)], (0, 0))
            elif self.SIDE == 'right':
                self.image.blit(self.images['attack_e_left'][int(self.CURRENT_SPRITE_E)], (0, 0))
        except Exception:
            self.block_moving = False
            self.E_ACTIVE = False
            self.CURRENT_SPRITE_E = 0
            self.E_ACTIVE_TIMER = 0
            self.SHIELD_ACTIVE = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        if not self.block_moving:
            self.get_input()
        elif self.block_moving and self.E_ACTIVE:
            self.start_e()

    def initialize_server_player(self, server_player):
        self.server_player = server_player
