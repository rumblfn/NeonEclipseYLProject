import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = (0, 255, 0)

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------         -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario Boy")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    x = y = 0  # координаты
    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                quit()
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR))
                    screen.blit(pf, (x, y))
                    pygame.display.update()
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0


if __name__ == "__main__":
    main()
