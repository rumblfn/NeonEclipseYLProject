import pygame


class AboutGameWindow:
    def __init__(self, sc, font, obj):
        self.x_left_top = obj['x1']
        self.y_left_top = obj['y1']
        self.x_right_bot = obj['x2']
        self.y_right_bot = obj['y2']
        self.widgetWidth = self.x_right_bot - self.x_left_top
        self.widgetHeight = self.y_right_bot - self.y_left_top
        self.borderColor = (64, 128, 255)
        self.borderColor2 = (8, 16, 32)
        self.textColor = (213, 255, 158)
        self.titleSurface = font.render(obj['titleText'], False, self.textColor)
        text = 'Neon Eclipses is an online game that can be played from the same network'
        newFont = pygame.font.SysFont('SFCompact', round(25 * self.widgetWidth / 808))
        self.mainTextSurface = newFont.render(text, False, (255, 183, 0))
        self.screen = sc

    def draw_widget(self):
        mx, my = pygame.mouse.get_pos()
        rectHoverRect = pygame.Rect(self.x_left_top + 2, self.y_left_top + 2, self.widgetWidth - 4,
                                    self.widgetHeight - 4)

        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)
        # if rectHoverRect.collidepoint((mx, my)):
        #     pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)

        pygame.draw.rect(self.screen, self.borderColor,
                         (self.x_left_top, self.y_left_top, self.widgetWidth, self.widgetHeight), 4, 10)
        self.screen.blit(self.titleSurface, (self.x_left_top + 15, self.y_left_top + 10))
        self.screen.blit(self.mainTextSurface, (self.x_left_top + 30, self.y_left_top + 47))