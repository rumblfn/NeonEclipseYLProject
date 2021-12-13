import pygame


class Background:
    def __init__(self, screen, image):
        self.image = image
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (0, 0))


class BackgroundMenu(Background):
    def draw_with_mouse_pos(self, w, h):
        mx, my = pygame.mouse.get_pos()
        lx = (w // 2 - mx) / 30 - 100
        ly = (h // 2 - my) / 30 - 100
        self.screen.blit(self.image, (lx, ly))
