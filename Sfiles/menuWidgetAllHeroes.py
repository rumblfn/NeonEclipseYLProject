import pygame


class AllHeroesWindow:
    def __init__(self, sc, font, obj):
        self.x_left_top = obj['x1']
        self.y_left_top = obj['y1']
        self.x_right_bot = obj['x2']
        self.y_right_bot = obj['y2']
        self.widgetWidth = obj['width']
        self.widgetHeight = obj['height']
        self.heroes = obj['heroes']
        self.currentHeroIndex = 0
        self.borderColor = (64, 128, 255)
        self.textAndBlockColor = (213, 255, 158)
        self.selectedHeroColor = (213, 158, 255)
        self.blockWidth = obj['blockWidth']
        self.blockHeight = obj['blockHeight']
        self.screen = sc
        self.titleSurface = font.render(obj['titleText'], True, self.textAndBlockColor)

    def draw_block(self, hero, x_blocks_start, start_x_pos, col):
        surf = pygame.Surface((64, 64))
        surf.blit(hero['imagePreview'], (0, 0))
        pygame.draw.rect(self.screen, col,
                         (start_x_pos + x_blocks_start, self.y_left_top + 40, self.blockWidth, self.blockHeight))
        self.screen.blit(surf, (start_x_pos + x_blocks_start + 4, self.y_left_top + 44))

    def draw_widget(self):
        # pygame.draw.rect(self.screen, self.borderColor,
        #                  (self.x_left_top, self.y_left_top, self.widgetWidth, self.widgetHeight), 4, 10)
        self.screen.blit(self.titleSurface, (self.x_left_top + 15, self.y_left_top + 10))
        x_blocks_start = 10
        start_x_pos = self.x_left_top
        for hero in self.heroes:
            if not hero['selected']:
                self.draw_block(hero, x_blocks_start, start_x_pos, self.textAndBlockColor)
            else:
                self.draw_block(hero, x_blocks_start, start_x_pos, self.selectedHeroColor)
            start_x_pos += x_blocks_start + self.blockWidth
