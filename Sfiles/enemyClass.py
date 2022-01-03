import pygame

playerImages = {
    'Hero1': pygame.image.load('static/charackter64x64Preview.png').convert_alpha(),
    'Hero2': pygame.image.load('static/paladin27x78.png').convert_alpha(),
    'Hero3': pygame.image.load('static/sniper37x75.png').convert_alpha(),
}


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_enemy):
        super().__init__()
        self.name = player_enemy.name
        self.power = player_enemy.power
        self.maxHp = player_enemy.maxHp
        self.hp = player_enemy.maxHp
        self.width = int(player_enemy.width)
        self.height = int(player_enemy.height)
        self.pos = (player_enemy.x, player_enemy.y)
        self.direction_x = 1

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(playerImages[self.name], (self.width, self.height)), (0, 0))
        self.rect = self.image.get_rect(topleft=self.pos)

        self.Q_ACTIVE = False
        self.E_ACTIVE = False
