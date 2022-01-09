import pygame
from db_requests import *


class StatisticsWindow:
    def __init__(self, sc, w, h):
        self.w = w
        self.h = h
        self.X_LEFT_TOP = round(0.911 * w)
        self.Y_LEFT_TOP = round((30 / 750) * h)
        self.X_RIGHT_BOT = round(0.961 * w)
        self.Y_RIGHT_BOT = round((70 / 750) * h)
        self.WIDGET_WIDTH = round(0.05 * w)
        self.WIDGET_HEIGHT = round((20 / 750) * h)

        self.screen = sc
        self.font = pygame.font.SysFont('SFCompactItalic', round(0.036 * w))
        self.info = check_user_in_system()

    def update_info(self, arg):
        if arg:
            update_wins()
        else:
            update_loses()
        self.info = check_user_in_system()

    def draw_widget(self):
        win_surf = self.font.render(str(self.info[1]), True, (0, 255, 0))
        lose_surf = self.font.render(str(self.info[0]), True, (255, 0, 0))
        self.screen.blit(win_surf, (self.X_LEFT_TOP + round(0.003 * self.w), self.Y_LEFT_TOP + round(0.005 * self.w)))
        self.screen.blit(lose_surf, (self.X_LEFT_TOP + round(0.033 * self.w), self.Y_LEFT_TOP + round(0.005 * self.w)))
