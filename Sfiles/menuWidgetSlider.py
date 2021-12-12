import pygame


class SliderWindow:
    def __init__(self, sc, w, h):
        self.x_left_top = round(0.911 * w)
        self.y_left_top = round((87 / 750) * h)
        self.x_right_bot = round(0.961 * w)
        self.y_right_bot = round((289 / 750) * h)
        self.widgetWidth = round(0.05 * w)
        self.widgetHeight = round((202 / 750) * h)
        self.borderColor = (64, 128, 255)
        self.borderColor2 = (8, 16, 32)
        self.screen = sc

    def draw_widget(self):
        rectHoverRect = pygame.Rect(self.x_left_top + 2, self.y_left_top + 2, self.widgetWidth - 4,
                                    self.widgetHeight - 4)
        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)
        pygame.draw.rect(self.screen, self.borderColor,
                         (self.x_left_top, self.y_left_top, self.widgetWidth, self.widgetHeight), 4, 10)

