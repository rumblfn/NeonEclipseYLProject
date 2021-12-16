import pygame


class Background:
    def __init__(self, screen, image):
        self.image = image
        self.screen = screen
        self.pos_x = 0
        self.pos_y = 0

    def update(self, shift):
        self.pos_x += shift[0]
        self.pos_y += shift[1]
        if self.pos_x > 0:
            self.pos_x -= 960

    def draw(self):
        self.pos_y -= 0.5
        if self.pos_y <= -1080:
            self.pos_y = 0
        self.screen.blit(self.image, (self.pos_x, self.pos_y))


class BackgroundMenu(Background):
    def draw_with_mouse_pos(self, w, h):
        mx, my = pygame.mouse.get_pos()
        lx = (w // 2 - mx) / 30 - 100
        ly = (h // 2 - my) / 30 - 100
        self.screen.blit(self.image, (lx, ly))
