import pygame
from map_preparation_settings import level1_map


npcImage = pygame.image.load('static/npcNormal2_64x64-export.png').convert_alpha()
msgImage = pygame.transform.scale(pygame.image.load('static/Talk-cloud.png').convert_alpha(), (64, 64))
fontTitle = pygame.font.SysFont('SFCompact', 14)
npcDisc = [
    {
        'name': 'guide',
        'width': 128,
        'height': 128,
    },
    {
        'name': 'blacksmith',
        'width': 128,
        'height': 128,
    },
    {
        'name': 'librarian',
        'width': 128,
        'height': 128,
    }
]


class Class_npc(pygame.sprite.Sprite):
    def __init__(self, pos, count, sc):
        super().__init__()
        HEIGHT = pygame.display.Info().current_h
        WIDTH = pygame.display.Info().current_w
        self.name = npcDisc[count]['name']
        self.screen = sc

        re_size = (HEIGHT / len(level1_map)) / 64
        self.width = round(npcDisc[count]['width'] * re_size)
        self.height = round(npcDisc[count]['height'] * re_size)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(npcImage, (self.width, self.height)), (0, 0))
        # surfTitle = fontTitle.render(self.name, False, (0, 0, 0))
        # self.image.blit(pygame.transform.scale(surfTitle, (10, 10)), (self.width // 2, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - self.height // 2))

    def show_msg(self):
        self.screen.blit(msgImage, (self.rect.x + self.width // 2 + 10, self.rect.y - 50))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]
