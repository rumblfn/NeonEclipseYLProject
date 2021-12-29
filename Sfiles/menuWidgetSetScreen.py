import pygame


class ScreenSizeWindow:
    def __init__(self, sc, font, w, h):
        self.X_LEFT_TOP = round(0.630 * w)
        self.Y_LEFT_TOP = round((310 / 750) * h)
        self.X_RIGHT_BOT = round(0.961 * w)
        self.Y_RIGHT_BOT = round((490 / 750) * h)
        self.WIDGET_WIDTH = round(0.331 * w)
        self.WIDGET_HEIGHT = round((130 / 750) * h)

        self.textAndBlockColor = (213, 255, 158)
        self.screen = sc
        self.titleSurface = font.render('Set window size', True, self.textAndBlockColor)
        self.borderColor = (64, 128, 255)
        self.BORDER_WIDTH = 4
        self.borderColor2 = (8, 16, 32)
        self.setted = 2
        self.colors = [self.borderColor, self.borderColor, self.borderColor]

    def draw_widget(self):
        rectHoverRect = pygame.Rect(self.X_LEFT_TOP + 2, self.Y_LEFT_TOP + 2, self.WIDGET_WIDTH - 4,
                                    self.WIDGET_HEIGHT - 4)
        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)
        pygame.draw.rect(self.screen, self.borderColor,
                         (self.X_LEFT_TOP, self.Y_LEFT_TOP, self.WIDGET_WIDTH, self.WIDGET_HEIGHT), self.BORDER_WIDTH,
                         10)
        self.screen.blit(self.titleSurface, (self.X_LEFT_TOP + 15, self.Y_LEFT_TOP + 10))
        self.draw_checkboxes()

    def draw_checkboxes(self):
        self.ch1 = pygame.draw.circle(self.screen, self.colors[0],
                                      (self.X_LEFT_TOP + round(self.WIDGET_WIDTH / 4),
                                       self.Y_LEFT_TOP + round(self.WIDGET_HEIGHT / 2)),
                                      10, 4)

        self.ch2 = pygame.draw.circle(self.screen, self.colors[1],
                                      (self.X_LEFT_TOP + round(self.WIDGET_WIDTH / 4 * 2),
                                       self.Y_LEFT_TOP + self.WIDGET_HEIGHT / 2),
                                      15, 4)

        self.ch3 = pygame.draw.circle(self.screen, self.colors[2],
                                      (self.X_LEFT_TOP + round(self.WIDGET_WIDTH / 4 * 3),
                                       self.Y_LEFT_TOP + round(self.WIDGET_HEIGHT / 2)),
                                      20, 4)

    def change_size(self):
        mx, my = pygame.mouse.get_pos()
        if self.ch1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed():
                pygame.display.set_mode((960, 600))
                self.colors = [self.borderColor, self.borderColor, self.borderColor]
                h = pygame.display.Info().current_h
        elif self.ch2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed():
                pygame.display.set_mode((1024, 640))
                self.colors = [self.borderColor, self.borderColor, self.borderColor]
        elif self.ch3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed():
                pygame.display.set_mode((1000, 1000))
                self.colors = [self.borderColor, self.borderColor, self.borderColor]
