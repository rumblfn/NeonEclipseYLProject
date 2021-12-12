import pygame

level1_map = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                       ',
    ' XXXX         XX         XX ',
    ' XXXX       XXX             ',
    ' XX       XXXX    XX  XX    ',
    '       X  XXXX    X   XXX   ',
    '    XXXX  XXXXXX        XXXX',
    'XXXXXXXX  XXXXXX   X       X',
    'XXXX                       X',
    '                      XXXXXX',
    '          XXXXXX  XX  XXXXXX',
    'XX        XXXXXX  XX  XXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

player1Preview = pygame.image.load('static/charackter64x64Preview.png')
player2Paladin = pygame.image.load('static/paladin27x78.png')
player3Sniper = pygame.image.load('static/sniper37x75.png')
playerImages = {
    'Hero1': player1Preview,
    'Hero2': player3Sniper,
    'Hero3': player2Paladin,
}


class Player_map_preparation(pygame.sprite.Sprite):
    def __init__(self, pos, player_settings):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = player_settings['name']
        self.power = player_settings['attack power']
        self.maxHp = player_settings['maxHp']
        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(player_settings['width'] * re_size)
        self.height = round(player_settings['height'] * re_size)
        self.image = pygame.Surface((self.width, self.height))
        self.image.blit(player_settings['imagePreview'], (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.control_speed = round(7 * WIDTH / 1440)
        self.speed = round(7 * WIDTH / 1440)
        self.gravity = 0.8 * HEIGHT / 900
        self.jump_speed = -18 * HEIGHT / 900
        self.jump_bool = True

    def get_input(self):
        keys = pygame.key.get_pressed()

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
        self.get_input()


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ready = None  # True
