import pygame
player1QImage = pygame.image.load('static/hero1animations/atackQ/leftQ/Q1.png').convert_alpha()
playerImages = {
    'Hero1': pygame.image.load('static/charackter64x64Preview.png').convert_alpha(),
    'Hero2': pygame.image.load('static/paladin27x78.png').convert_alpha(),
    'Hero3': pygame.image.load('static/sniper37x75.png').convert_alpha(),
}


class Enemy_hero3(pygame.sprite.Sprite):
    def __init__(self, player_enemy):
        super().__init__()
        self.block_moving = False

        self.name = player_enemy.name
        self.power = player_enemy.power
        self.maxHp = player_enemy.maxHp
        self.hp = player_enemy.maxHp
        self.width = player_enemy.width
        self.height = player_enemy.height
        self.pos = (player_enemy.x, player_enemy.y)
        self.direction_x = 1
        self.current_sprite = 0

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=self.pos)

        self.Q_ACTIVE = False
        self.CURRENT_SPRITE_Q = 0
        self.E_ACTIVE = False
        self.CURRENT_SPRITE_E = 0
        self.SIDE = 'right'
        self.SHIELD_ACTIVE = False
        self.AA = False
        self.CURRENT_SPRITE_AA = 0

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

    def start_e(self):
        self.CURRENT_SPRITE_E += 0.2
        self.image.fill((0, 0, 0, 0))
        try:
            if self.SIDE == 'left':
                self.image.blit(self.images['attack_e_right'][int(self.CURRENT_SPRITE_E)], (0, 0))
            elif self.SIDE == 'right':
                self.image.blit(self.images['attack_e_left'][int(self.CURRENT_SPRITE_E)], (0, 0))
        except:
            if self.SIDE == 'left':
                self.image.blit(self.images['attack_e_right'][-1], (0, 0))
            elif self.SIDE == 'right':
                self.image.blit(self.images['attack_e_left'][-1], (0, 0))

    def get_input(self):
        if self.E_ACTIVE:
            self.start_e()
        else:
            self.current_sprite += 0.2
            self.image.fill((0, 0, 0, 0))
            if self.direction_x == 1:
                if self.Q_ACTIVE:
                    self.image.blit(self.images['q_right_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
                else:
                    self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
                self.SIDE = 'right'
            elif self.direction_x == -1:
                if self.Q_ACTIVE:
                    self.image.blit(self.images['q_left_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
                else:
                    self.image.blit(self.images['left_walk'][int(self.current_sprite)], (0, 0))
                self.SIDE = 'left'
            else:
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
            if self.AA:
                if self.SIDE == 'right':
                    self.image.blit(self.images['auto_attack_right'][int(self.CURRENT_SPRITE_AA)], (0, 0))
                else:
                    self.image.blit(self.images['auto_attack_left'][int(self.CURRENT_SPRITE_AA)], (0, 0))
            if self.SHIELD_ACTIVE:
                self.image.blit(self.images['shield'], (0, 0))
            if self.current_sprite >= 1:
                self.current_sprite = 0
            if self.Q_ACTIVE:
                self.CURRENT_SPRITE_Q += 0.2
                if self.CURRENT_SPRITE_Q >= 6:
                    self.CURRENT_SPRITE_Q = 0
            if self.E_ACTIVE:
                self.CURRENT_SPRITE_E += 0.2
            if self.AA:
                self.CURRENT_SPRITE_AA += 0.25
                if self.CURRENT_SPRITE_AA >= 3:
                    self.CURRENT_SPRITE_AA = 0

    def update_values(self, enemy):
        self.Q_ACTIVE = enemy.Q
        self.E_ACTIVE = enemy.E
        self.direction_x = enemy.direction_x
        self.hp = enemy.hp
        self.AA = enemy.simpleAttack
        self.SHIELD_ACTIVE = enemy.E_ACTIVE_SHIELD
