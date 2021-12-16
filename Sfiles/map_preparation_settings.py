import pygame

level1_map = [
    '                           ',
    '                  u        ',
    '                           ',
    '                  X        ',
    '          P 0          XX  ',
    '   XX    XXX          0XXXX',
    '  0XXN    0              XX',
    '   X0XX                    ',
    '  0XXXXXXXXXXXXX       N 0 ',
    '   XXпП П  0XXXX     XXXX  ',
    '   П  XXXX  X0XX0     XX   ',
    '  XXXXXXXX  XX0XXX         ',
    '  XXXX0      XXXXX      0  ',
    '   0                       ',
    '                           ',
    '            XXXXXXXXXX     ',
    '  X  N    XXXXXXXXXXXXXX   ',
    '  XXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size
