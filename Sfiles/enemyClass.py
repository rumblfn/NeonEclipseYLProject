import pygame


try:
    from CBullet import Bullet
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
