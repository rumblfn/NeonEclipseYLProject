import pygame
from time import sleep
from _thread import start_new_thread
from pygame.constants import *

try:
    from CBullet import Bullet
    from hero1e import Hero1AtackE
    from map_preparation_settings import level1_map
    player1Preview = pygame.image.load('static/charackter64x64Preview.png').convert_alpha()
    player2Paladin = pygame.image.load('static/paladin27x78.png').convert_alpha()
    player3Sniper = pygame.image.load('static/sniper37x75.png').convert_alpha()
    playerImages = {
        'Hero1': player1Preview,
        'Hero2': player3Sniper,
        'Hero3': player2Paladin,
    }
except:
    print('game not started')


def speed_to_low(player):
    player.speed = 4
    sleep(4)
    player.speed = player.control_speed


class Player_hero1(pygame.sprite.Sprite):
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

        self.bullets = pygame.sprite.Group()
        self.attacksE = pygame.sprite.Group()

        self.K_x = False
        self.attacksEBool = 300
        self.current_sprite = 0

        self.Q_ACTIVE = False
        self.Q_ACTIVE_TIMER = 600
        self.q_side = 'q_right_animation'
        self.Q_SLEEPER = self.Q_ACTIVE_TIMER * 3

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(player_settings['width'] * re_size) - 1
        self.height = round(player_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.images = {}
        for el in player_settings['animations'].keys():
            self.images[el] = []
            for i in range(1, 15):
                image = pygame.transform.scale(
                    pygame.image.load(f'{player_settings["animations"][el]}{i}.png').convert_alpha(),
                    (self.width, self.height))
                self.images[el].append(image)

        self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(7 * WIDTH / 1440)
        self.speed = round(7 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True
        self.shoot_bool = 1

        self.server_player = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def get_input(self):
        self.Q_SLEEPER += 1
        self.current_sprite += 0.25
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if self.Q_ACTIVE:
            self.Q_ACTIVE_TIMER += 1
            self.image.fill((0, 0, 0, 0))
            self.image.blit(self.images[self.q_side][int(self.current_sprite)], (0, 0))
            if self.Q_ACTIVE_TIMER >= 600:
                self.Q_ACTIVE = False
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
                if self.server_player:
                    self.server_player.Q = False

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.q_side = 'q_right_animation'
            if not self.Q_ACTIVE:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
            if self.server_player:
                self.server_player.direction_x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.q_side = 'q_left_animation'
            if not self.Q_ACTIVE:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['left_walk'][int(self.current_sprite)], (0, 0))
            if self.server_player:
                self.server_player.direction_x = -1
        else:
            self.direction.x = 0
            if self.server_player:
                self.server_player.direction_x = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if not self.direction.y:
            self.jump_bool = True

        if self.server_player:
            if self.server_player.simpleAttack:
                self.server_player.simpleAttack = False

        if pygame.mouse.get_pressed()[0]:
            if self.shoot_bool >= 1:
                self.bullets.add(self.create_bullet())
                if self.server_player:
                    self.server_player.simpleAttack = True
                    self.server_player.mouse_pos_x, self.server_player.mouse_pos_y = pygame.mouse.get_pos()

        if keys[pygame.K_e]:
            if self.attacksEBool >= 300:
                self.attacksE.add(Hero1AtackE(self.rect.midbottom))
                self.attacksEBool = 0
                if self.server_player:
                    self.server_player.E = True
        if keys[pygame.K_q]:
            if self.Q_SLEEPER >= 1800:
                self.Q_ACTIVE = True
                self.Q_ACTIVE_TIMER = 0
                self.current_sprite = 0
                self.Q_SLEEPER = 0
                if self.server_player:
                    self.server_player.Q = True

        if self.current_sprite >= 13:
            self.current_sprite = 0

    def create_bullet(self):
        self.shoot_bool = 0
        return Bullet((self.rect.centerx + 10, self.rect.centery - self.height / 4))

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        self.shoot_bool += 0.1
        self.attacksEBool += 1
        if not self.block_moving:
            self.get_input()

    def initialize_server_player(self, server_player):
        self.server_player = server_player

    def update_server(self):
        self.server_player.x = (self.rect.x / self.WIDTH) * 1920
        self.server_player.y = (self.rect.y / self.HEIGHT) * 1080


class Player_hero2(pygame.sprite.Sprite):
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

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(player_settings['width'] * re_size) - 1
        self.height = round(player_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = {}
        self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(9 * WIDTH / 1440)
        self.speed = round(9 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True

        self.server_player = None

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if not self.direction.y:
            self.jump_bool = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        if not self.block_moving:
            self.get_input()

    def initialize_server_player(self, server_player):
        self.server_player = server_player


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

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(player_settings['width'] * re_size) - 1
        self.height = round(player_settings['height'] * re_size) - 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(9 * WIDTH / 1440)
        self.speed = round(9 * WIDTH / 1440)
        self.gravity = 0.7 * HEIGHT / 900
        self.jump_speed = -16 * HEIGHT / 900
        self.jump_bool = True

        self.server_player = None

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
        if not self.direction.y:
            self.jump_bool = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        if not self.block_moving:
            self.get_input()

    def initialize_server_player(self, server_player):
        self.server_player = server_player


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ready = None # None

        self.name = None
        self.power = None
        self.maxHp = None
        self.hp = None

        self.width = None
        self.height = None

        self.Q = False
        self.E = False

        self.simpleAttack = False
        self.mouse_pos_x, self.mouse_pos_y = None, None

        self.direction_x = 1
        self.damage_given = 0


class Player_map_parkour(pygame.sprite.Sprite):
    def __init__(self, pos, player_settings):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = player_settings['name']
        self.power = player_settings['attack power']
        self.maxHp = player_settings['maxHp']
        self.started_pos = pos

        self.K_x = False
        self.current_sprite = 0

        from map_parkour_settings import level_parkour_map

        re_size = (HEIGHT / len(level_parkour_map)) / 64
        re_size_h = (HEIGHT / len(level_parkour_map)) / player_settings['height']
        re_size_w = (HEIGHT / len(level_parkour_map)) / player_settings['width']
        self.width = round(player_settings['width'] * re_size_w) - round(14 * re_size_w)
        self.height = round(player_settings['height'] * re_size_h) - round(14 * re_size_h)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        if player_settings['animations'] is None:
            self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        else:
            self.images = {}
            for el in player_settings['animations'].keys():
                self.images[el] = []
                for i in range(1, 15):
                    image = pygame.transform.scale(pygame.image.load(f'{player_settings["animations"][el]}{i}.png').convert_alpha(), (self.width, self.height))
                    self.images[el].append(image)
            self.image.blit(pygame.transform.scale(player_settings['imagePreview'], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(7 * WIDTH / 1440)
        self.speed = round(7 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True
        self.bird_mode = False

        self.shoot_bool = 1

    def get_input(self):
        self.current_sprite += 0.25
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.K_x = True
        else:
            self.K_x = False

        if keys[pygame.K_d]:
            if self.bird_mode:
                self.direction.x = 0
            else:
                self.direction.x = 1
            if self.images:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
        elif keys[pygame.K_a]:
            if self.bird_mode:
                self.direction.x = -0.4
            else:
                self.direction.x = -1
            if self.images:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['left_walk'][int(self.current_sprite)], (0, 0))
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jump_bool:
                self.jump()
            if self.bird_mode:
                h = pygame.display.Info().current_h
                w = pygame.display.Info().current_w
                self.direction.y = -3 * pygame.display.Info().current_h / 900
                self.control_speed = round(2.3 * w / 1440)
                self.speed = round(2.3 * w / 1440)
                self.gravity = 0.25 * h / 900
                self.jump_speed = -3 * h / 900

        if not self.direction.y:
            self.jump_bool = True

        if self.current_sprite >= 13:
            self.current_sprite = 0

    def create_bullet(self):
        self.shoot_bool = 0
        return Bullet((self.rect.centerx + 10, self.rect.centery - self.height / 4))

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.jump_bool = False
        self.direction.y = self.jump_speed

    def update(self):
        self.shoot_bool += 0.1
        self.get_input()

    def levitate(self):
        self.direction.y = -9 * pygame.display.Info().current_h / 900

    def web(self, arg):
        if arg:
            self.control_speed = round(pygame.display.Info().current_w / 1440)
            self.speed = round(pygame.display.Info().current_w / 1440)
        else:
            if self.bird_mode:
                self.control_speed = round(2.3 * pygame.display.Info().current_w / 1440)
                self.speed = round(2.3 * pygame.display.Info().current_w / 1440)
            else:
                self.control_speed = round(7 * pygame.display.Info().current_w / 1440)
                self.speed = round(7 * pygame.display.Info().current_w / 1440)
                self.gravity = 0.8 * pygame.display.Info().current_h / 900
                self.jump_speed = -18 * pygame.display.Info().current_h / 900

