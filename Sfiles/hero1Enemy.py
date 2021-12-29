import pygame
from CBullet import Bullet
from hero1e import Hero1AtackE
player1QImage = pygame.image.load('static/hero1animations/atackQ/leftQ/Q1.png').convert_alpha()
playerImages = {
    'Hero1': pygame.image.load('static/charackter64x64Preview.png').convert_alpha(),
    'Hero2': pygame.image.load('static/paladin27x78.png').convert_alpha(),
    'Hero3': pygame.image.load('static/sniper37x75.png').convert_alpha(),
}


class Enemy_hero1(pygame.sprite.Sprite):
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

        self.normalImage = pygame.transform.scale(playerImages[self.name], (self.width, self.height))
        self.QImage = pygame.transform.scale(player1QImage, (self.width, self.height))

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(self.normalImage, (0, 0))
        self.rect = self.image.get_rect(topleft=self.pos)

        self.bullets = pygame.sprite.Group()
        self.attacksE = pygame.sprite.Group()

        self.Q_ACTIVE = False
        self.E_ACTIVE = False

        animations = {  # paths
            'right_walk': 'static/hero1animations/rightWalkImages/rightwalk',  # + 14 + $ 1...2...14 + .png
            'left_walk': 'static/hero1animations/leftWalkImages/leftwalk',
            'right_jump': 'static/hero1animations/rightjump/rightjump',
            'left_jump': 'static/hero1animations/leftjump/leftjump',
            'q_right_animation': 'static/hero1animations/atackQ/rightQ/Q',
            'q_left_animation': 'static/hero1animations/atackQ/leftQ/Q'
        }

        self.images = {}
        for el in animations.keys():
            self.images[el] = []
            for i in range(1, 15):
                image = pygame.transform.scale(
                    pygame.image.load(f'{animations[el]}{i}.png').convert_alpha(),
                    (self.width, self.height))
                self.images[el].append(image)

    def get_input(self):
        self.current_sprite += 0.25
        if self.Q_ACTIVE:
            if self.direction_x == 1:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['q_right_animation'][int(self.current_sprite)], (0, 0))
            elif self.direction_x == -1:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['q_left_animation'][int(self.current_sprite)], (0, 0))
        else:
            if self.direction_x == 1:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['right_walk'][int(self.current_sprite)], (0, 0))
            elif self.direction_x == -1:
                self.image.fill((0, 0, 0, 0))
                self.image.blit(self.images['left_walk'][int(self.current_sprite)], (0, 0))
        if self.E_ACTIVE:
            self.attacksE.add(Hero1AtackE(self.rect.midbottom))
        if self.current_sprite >= 13:
            self.current_sprite = 0

    def create_bullet(self, mouse_pos):
        return Bullet((self.rect.centerx + 10, self.rect.centery - self.height / 4), mouse_pos)

    def update_values(self, enemy):
        self.Q_ACTIVE = enemy.Q
        self.E_ACTIVE = enemy.E
        self.direction_x = enemy.direction_x
        self.hp = enemy.hp
