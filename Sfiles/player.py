import pygame
from time import sleep

try:
    from CBullet import Bullet
    from map_preparation_settings import level1_map
except:
    print('game not started')


def speed_to_low(player):
    player.speed = 4
    sleep(4)
    player.speed = player.control_speed


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ready = True  # None

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
        self.current_pos = pos

        self.K_x = False
        self.current_sprite = 0

        from map_parkour_settings import level_parkour_map

        self.lvl = level_parkour_map
        self.settings = player_settings

        re_size = (HEIGHT / len(self.lvl)) / 64
        re_size_h = (HEIGHT / len(self.lvl)) / self.settings['height']
        re_size_w = (HEIGHT / len(self.lvl)) / self.settings['width']
        self.start_height = HEIGHT
        self.width = round(self.settings['width'] * re_size_w) - round(14 * re_size_w)
        self.height = round(self.settings['height'] * re_size_h) - round(14 * re_size_h)
        self.start_width = self.width
        self.start_height = self.height
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.images = False
        self.player_settings = player_settings
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
        self.start_img = self.image
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(7 * WIDTH / 1440)
        self.speed = round(7 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True
        self.bird_mode = False
        self.invis_mode = False
        self.resize_helper = 0

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
                if self.invis_mode:
                    self.image.fill((255, 255, 255, 0))
                else:
                    self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
        elif keys[pygame.K_a]:
            if self.bird_mode:
                self.direction.x = -0.4
            else:
                self.direction.x = -1
            if self.images:
                self.image.fill((0, 0, 0, 0))
                if self.invis_mode:
                    self.image.fill((255, 255, 255, 0))
                else:
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

    def resize(self, arg):
        if arg:
            self.resize_helper += 1
            if self.resize_helper % 50 == 0:
                x, y = self.rect.x, self.rect.y
                self.current_pos = self.rect.x, self.rect.y
                w = 10
                h = 10
                self.width = w
                self.height = h
                self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                self.images = False
                if self.settings['animations'] is None:
                    self.image.blit(pygame.transform.scale(self.settings['imagePreview'], (self.width, self.height)),
                                    (0, 0))
                else:
                    self.images = {}
                    for el in self.settings['animations'].keys():
                        self.images[el] = []
                        for i in range(1, 15):
                            image = pygame.transform.scale(
                                pygame.image.load(f'{self.settings["animations"][el]}{i}.png').convert_alpha(),
                                (self.width, self.height))
                            self.images[el].append(image)
                    self.image.blit(pygame.transform.scale(self.settings['imagePreview'], (self.width, self.height)),
                                    (0, 0))
                self.rect = self.image.get_rect(topleft=(x, y))


