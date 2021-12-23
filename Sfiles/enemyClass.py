import pygame

try:
    from CBullet import Bullet
    player1Preview = pygame.image.load('static/charackter64x64Preview.png').convert_alpha()
    player2Paladin = pygame.image.load('static/paladin27x78.png').convert_alpha()
    player3Sniper = pygame.image.load('static/sniper37x75.png').convert_alpha()

    player1QImage = pygame.image.load('static/hero1animations/atackQ/leftQ/Q1.png').convert_alpha()
    playerImages = {
        'Hero1': player1Preview,
        'Hero2': player3Sniper,
        'Hero3': player2Paladin,
    }
except:
    print('game not started')


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_enemy):
        super().__init__()
        self.name = player_enemy.name
        self.power = player_enemy.power
        self.maxHp = player_enemy.maxHp
        self.width = player_enemy.width
        self.height = player_enemy.height
        self.pos = (player_enemy.x, player_enemy.y)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(playerImages[self.name], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=self.pos)


class Enemy_hero1(pygame.sprite.Sprite):
    def __init__(self, player_enemy):
        super().__init__()
        self.block_moving = False

        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w

        self.name = player_enemy.name
        self.power = player_enemy.power
        self.maxHp = player_enemy.maxHp
        self.width = player_enemy.width
        self.height = player_enemy.height
        self.pos = (player_enemy.x, player_enemy.y)

        self.normalImage = pygame.transform.scale(playerImages[self.name], (self.width, self.height))
        self.QImage = pygame.transform.scale(player1QImage, (self.width, self.height))

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(self.normalImage, (0, 0))
        self.rect = self.image.get_rect(topleft=self.pos)

        self.bullets = pygame.sprite.Group()
        self.attacksE = pygame.sprite.Group()

        self.Q_ACTIVE = False

    def get_input(self):
        if self.Q_ACTIVE:
            self.image.fill((0, 0, 0, 0))
            self.image.blit(self.QImage, (0, 0))
        else:
            self.image.blit(self.normalImage, (0, 0))

    def create_bullet(self, mouse_pos):
        return Bullet((self.rect.centerx + 10, self.rect.centery - self.height / 4), mouse_pos)