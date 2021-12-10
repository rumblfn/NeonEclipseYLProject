import pygame

level1_map = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                       ',
    ' XXXX         XX         XX ',
    ' XXXX       XXX             ',
    ' XX       XXXX    XX  XX    ',
    '       X  XXXX    X   XXX   ',
    '    XXXX  XXXXXX        XXXX',
    'XXXXXXXX  XXXXXX   X       X',
    'XXXX                       X',
    '             XXX      XXXXXX',
    '          XXXXXX  XX  XXXXXX',
    'XX        XXXXXX  XX  XXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size
