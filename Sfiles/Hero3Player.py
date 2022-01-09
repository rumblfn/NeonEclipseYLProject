import pygame
from map_preparation_settings import level1_map


class Player_hero3(pygame.sprite.Sprite):
    def __init__(self, pos, player_settings):
        super().__init__()
        self.wins = 0
        self.player_settings = player_settings
        self.block_moving = False

        self.HEIGHT = pygame.display.Info().current_h
        self.WIDTH = pygame.display.Info().current_w
        self.name = player_settings['name']
        self.power = player_settings['attack power']
        self.maxHp = player_settings['maxHp']
        self.hp = player_settings['maxHp']
        self.started_pos = pos

        self.K_x = False
        self.Q_STUN_TIMER = 120
        self.Q_ACTIVE = False
        self.Q_ACTIVE_TIMER = 720
        self.Q_ACTIVE_TIMER_MAX = 720
        self.Q_TIMER = 480
        self.E_ACTIVE = False
        self.SHIELD_ACTIVE = False
        self.E_TIMER = 480
        self.E_TIMER_MAX = 480
        self.E_ACTIVE_TIMER = 180
        self.CURRENT_SPRITE = 0
        self.CURRENT_SPRITE_Q = 0
        self.CURRENT_SPRITE_E = 0
        self.SIDE = 'left'
        self.AA_TIMER = 42
        self.AA_TIMER_MAX = 42
        self.AA_ACTIVE = False
        self.CURRENT_SPRITE_AA = 0
        self.AA_TIMER_ACTIVE = False
        self.Q_END = False

        self.SHIELD_HP_KEF = 0.4
        self.SHIELD_HP = self.SHIELD_HP_KEF * self.maxHp

        re_size = (self.HEIGHT / len(level1_map)) / 64
        self.width = round(64 * re_size * 1.5) - 1
        self.height = round(64 * re_size * 1.5) - 1
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
        self.control_speed = round(9 * self.WIDTH / 1440)
        self.speed = round(9 * self.WIDTH / 1440)
        self.gravity = 0.8 * self.HEIGHT / 900
        self.jump_speed = -18 * self.HEIGHT / 900
        self.jump_bool = True
        self.spring_jump_bool = False

        self.server_player = None

        self.speed_potion_count = 0  # Увеличивает мс на 20%
        self.resistance_potion_count = 0  # Уменьшает весь входящий урон на  15%
        self.recharge_potion_count = 0  # Уменьшает время перезарядки обычной атака на 10%

        self.speed_potion = False
        self.resistance_potion = False
        self.recharge_potion = False

        self.speed_potion_boost = 0.2
        self.speed_potion_timer = 0
        self.speed_potion_timer_max = 300
        self.speed_potion_timer_ACTIVE = False

        self.resistance_potion_no_save = 0.85
        self.resistance_potion_timer = 0
        self.resistance_potion_timer_max = 300
        self.resistance_potion_timer_ACTIVE = False

        self.repulsion_weapon = False  # value to change
        self.aa_repulsion = False
        self.button_s = True
        self.timer_button_s = 0
        self.timer_button_s_max = 60

    def set_first_params(self):
        self.power = self.player_settings['attack power']
        self.maxHp = self.player_settings['maxHp']
        self.hp = self.player_settings['maxHp']

    def update_shield_hp(self):
        self.SHIELD_HP = self.SHIELD_HP_KEF * self.maxHp

    def update_size(self, new_width, new_height):
        self.HEIGHT = new_height
        self.WIDTH = new_width

    def get_input(self):
        self.CURRENT_SPRITE += 0.2
        self.CURRENT_SPRITE_Q += 0.2
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_1]:
            self.speed_potion = True
            self.resistance_potion = False
            self.recharge_potion = False
        if keys[pygame.K_2]:
            self.speed_potion = False
            self.resistance_potion = True
            self.recharge_potion = False
        if keys[pygame.K_3]:
            self.speed_potion = False
            self.resistance_potion = False
            self.recharge_potion = True

        if mouse[1]:
            if self.speed_potion:
                self.speed_potion = False
                if self.speed_potion_count > 0:
                    self.speed_potion -= 1
                    self.speed_potion_timer_ACTIVE = True
                    self.speed += self.speed_potion_boost

            elif self.resistance_potion:
                self.resistance_potion = False
                if self.resistance_potion_count > 0:
                    self.resistance_potion_count -= 1
                    self.resistance_potion_timer_ACTIVE = True

            elif self.recharge_potion:
                self.recharge_potion = False
                if self.recharge_potion_count > 0:
                    self.recharge_potion_count -= 1
                    self.AA_TIMER = 42
                    self.E_TIMER = 480
                    self.Q_ACTIVE_TIMER = 720

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if mouse[0]:
            self.speed_potion = False
            self.resistance_potion = False
            self.recharge_potion = False

        if self.speed_potion_timer_ACTIVE:
            self.speed_potion_timer += 1
            if self.speed_potion_timer >= self.speed_potion_timer_max:
                self.speed_potion_timer = 0
                self.speed_potion_timer_ACTIVE = False
                self.speed -= self.speed_potion_boost

        if self.resistance_potion_timer_ACTIVE:
            self.resistance_potion_timer += 1
            if self.resistance_potion_timer >= self.resistance_potion_timer_max:
                self.resistance_potion_timer = 0
                self.resistance_potion_timer_ACTIVE = False

        if self.Q_ACTIVE:
            self.Q_TIMER += 1
            if self.Q_TIMER >= 480:
                self.Q_ACTIVE = False
                if self.server_player:
                    self.server_player.Q = False
        if self.Q_ACTIVE_TIMER <= 720 and not self.Q_ACTIVE:
            self.Q_ACTIVE_TIMER += 1
        if self.Q_END:
            self.Q_ACTIVE = False
            self.Q_TIMER = 480
            self.Q_END = False
            self.Q_STUN_TIMER = 0
            if self.server_player:
                self.server_player.Q = False
        if self.Q_STUN_TIMER <= 120:
            self.Q_STUN_TIMER += 1

        if self.repulsion_weapon:
            if self.button_s:
                if keys[pygame.K_s]:
                    self.aa_repulsion = not self.aa_repulsion
                    self.button_s = False

        if not self.button_s:
            self.timer_button_s += 1
            if self.timer_button_s >= self.timer_button_s_max:
                self.timer_button_s = 0
                self.button_s = True

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.image.fill((0, 0, 0, 0))
            self.SIDE = 'right'
            if self.Q_ACTIVE:
                self.image.blit(self.images['q_right_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
            else:
                self.image.blit(self.images['right_walk'][int(self.CURRENT_SPRITE)], (0, 0))
            if self.server_player:
                self.server_player.direction_x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.image.fill((0, 0, 0, 0))
            if self.Q_ACTIVE:
                self.image.blit(self.images['q_left_animation'][int(self.CURRENT_SPRITE_Q)], (0, 0))
            else:
                self.image.blit(self.images['left_walk'][int(self.CURRENT_SPRITE)], (0, 0))
            self.SIDE = 'left'
            if self.server_player:
                self.server_player.direction_x = -1
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
            if self.server_player:
                self.server_player.direction_x = 0
        if self.AA_ACTIVE:
            self.AA_TIMER = 0
            self.image.fill((0, 0, 0, 0))
            self.CURRENT_SPRITE_AA += 0.25
            mx, my = pygame.mouse.get_pos()
            if self.server_player:
                self.server_player.simpleAttack = True
                self.server_player.mouse_pos_x, self.server_player.mouse_pos_y = pygame.mouse.get_pos()
            try:
                if mx < self.rect.x:
                    self.image.blit(self.images['auto_attack_left'][int(self.CURRENT_SPRITE_AA)], (0, 0))
                    self.rect.x -= 5
                else:
                    self.image.blit(self.images['auto_attack_right'][int(self.CURRENT_SPRITE_AA)], (0, 0))
                    self.rect.x += 5
            except:
                self.CURRENT_SPRITE_AA = 0
                self.AA_ACTIVE = False
                self.AA_TIMER_ACTIVE = True
                if self.server_player:
                    if self.server_player.simpleAttack:
                        self.server_player.simpleAttack = False
        if self.AA_TIMER_ACTIVE:
            self.AA_TIMER += 1
            if self.AA_TIMER >= 42:
                self.AA_TIMER_ACTIVE = False

        if self.SHIELD_ACTIVE:
            self.E_ACTIVE_TIMER += 1
            self.image.blit(self.images['shield'], (0, 0))
            if self.SHIELD_HP <= 0:
                self.update_shield_hp()
                self.E_ACTIVE_TIMER = 180
            if self.E_ACTIVE_TIMER >= 180:
                self.E_ACTIVE_TIMER = 0
                self.SHIELD_ACTIVE = False
                if self.server_player:
                    self.server_player.E_ACTIVE_SHIELD = False
        if not self.SHIELD_ACTIVE and self.E_TIMER <= 480:
            self.E_TIMER += 1

        if self.CURRENT_SPRITE >= 0.8:
            self.CURRENT_SPRITE = 0
        if self.CURRENT_SPRITE_Q >= 5.8:
            self.CURRENT_SPRITE_Q = 0

        if mouse[0]:
            if self.AA_TIMER >= 42:
                self.AA_ACTIVE = True
                if self.server_player:
                    self.server_player.simpleAttack = True
                    self.server_player.mouse_pos_x, self.server_player.mouse_pos_y = pygame.mouse.get_pos()
        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if self.spring_jump_bool:
            self.jump_bool = True
            self.spring_jump_bool = False
            self.direction.y = self.jump_speed * 2
        if not self.direction.y:
            self.jump_bool = True
        if keys[pygame.K_e]:
            if self.E_TIMER >= 480:
                self.block_moving = True
                self.E_ACTIVE = True
                self.E_TIMER = 0
                self.direction.x = 0
                if self.server_player:
                    self.server_player.E = True
        if keys[pygame.K_q]:
            if self.Q_ACTIVE_TIMER >= 720:
                self.Q_ACTIVE = True
                self.Q_ACTIVE_TIMER = 0
                self.Q_TIMER = 0
                if self.server_player:
                    self.server_player.Q = True

    def start_e(self):
        if self.server_player:
            self.server_player.E = True
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
            if self.server_player:
                self.server_player.E = False
                self.server_player.E_ACTIVE_SHIELD = True

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
            self.direction.x = 0
            self.start_e()

    def initialize_server_player(self, server_player):
        self.server_player = server_player
        self.server_player.hp = self.hp
        self.server_player.maxHp = self.maxHp
        self.server_player.power = self.power

    def update_server(self):
        self.server_player.hp = self.hp
        self.server_player.x = (self.rect.x / self.WIDTH) * 1920
        self.server_player.y = (self.rect.y / self.HEIGHT) * 1080
