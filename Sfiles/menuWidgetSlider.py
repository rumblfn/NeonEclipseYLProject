import pygame


class SliderWindow:
    def __init__(self, sc, w, h):
        self.w = w
        self.h = h
        self.x_left_top = round(0.911 * w)
        self.y_left_top = round((87 / 750) * h)
        self.x_right_bot = round(0.961 * w)
        self.y_right_bot = round((289 / 750) * h)
        self.widgetWidth = round(0.05 * w)
        self.widgetHeight = round((202 / 750) * h)
        self.borderColor = (64, 128, 255)
        self.borderColor2 = (8, 16, 32)
        self.lineColor = (188, 190, 192)
        self.screen = sc
        self.cur = ''
        self.rect = ''
        self.res = 50
        self.last_not_zero = self.res
        self.vol_changed = None
        self.cur_y = self.x_left_top + self.widgetWidth // 2 - (round(0.005 * self.w) // 2)
        self.cur_h = self.widgetHeight - self.widgetHeight // 5 - 30

    def draw_widget(self):
        rectHoverRect = pygame.Rect(self.x_left_top + 2, self.y_left_top + 2, self.widgetWidth - 4,
                                    self.widgetHeight - 4)
        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect, border_radius=3)
        pygame.draw.rect(self.screen, self.borderColor,
                         (self.x_left_top, self.y_left_top, self.widgetWidth, self.widgetHeight), 4, 10)

        self.rect = pygame.draw.rect(self.screen, self.borderColor2,
                         (self.x_left_top + self.widgetWidth // 4 - (round(0.005 * self.w) // 2),
                          self.y_left_top + 20, round(0.03 * self.w), self.widgetHeight - self.widgetHeight // 5 - 30))

        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.x_left_top + self.widgetWidth // 2 - (round(0.005 * self.w) // 2),
                          self.y_left_top + 20, round(0.005 * self.w), self.widgetHeight - self.widgetHeight // 5 - 30),
                         border_radius=4)
        self.cur_y = self.y_left_top + 20
        self.cur_h = self.widgetHeight - self.widgetHeight // 5 - 30

        if self.res == 1:
            sound = pygame.image.load('static/sound_off.png')
        else:
            sound = pygame.image.load('static/sound_on.png')
        sound = pygame.transform.scale(sound, (round(0.02 * self.w), round(0.02 * self.w)))
        self.soundoff = pygame.draw.rect(self.screen, self.borderColor2, (self.x_left_top + self.widgetWidth // 4 - (round(0.005 * self.w) // 2) + 10 * self.w // 1536,
                          self.y_left_top + round(self.widgetHeight * 0.75) + 10,
                          round(0.02 * self.w), round(0.02 * self.w)))
        self.screen.blit(sound, (self.x_left_top + self.widgetWidth // 4 - (round(0.005 * self.w) // 2) + 7 * self.w // 1536,
                          self.y_left_top + round(self.widgetHeight * 0.75) + 10,
                          round(0.02 * self.w), round(0.02 * self.w)))
        self.draw_cur()

    def draw_cur(self):
        self.cur = pygame.draw.rect(self.screen, self.borderColor,
                         (self.x_left_top + self.widgetWidth // 4 - (round(0.005 * self.w) // 2),
                          self.cur_y + round(self.cur_h * abs((1 - self.res / 100))),
                          round(0.03 * self.w), 10), border_radius=4)

    def check_click_onslider(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint((mx, my)):
            self.get_vol(my)

    def check_sound_off(self):
        mx, my = pygame.mouse.get_pos()
        if self.soundoff.collidepoint((mx, my)):
            self.get_vol(-1000)

    def get_vol(self, my):
        if my == -1000:
            if self.res == 1:
                self.res = self.last_not_zero
                self.vol_changed = self.res
            else:
                self.last_not_zero = self.res
                res = 1
                self.res = res
                self.vol_changed = self.res
        else:
            maxy = self.cur_y + self.cur_h
            miny = self.cur_y
            cur = my - miny
            maxx = maxy - miny
            res = (cur * 100) // maxx
            res = abs(100 - res)
            self.res = res
            self.vol_changed = self.res

    def track_mouse(self):
        for event in pygame.event.get():
            while event.type != pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if self.rect.collidepoint((mx, my)):
                    print(mx, my)

