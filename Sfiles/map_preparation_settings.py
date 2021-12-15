import pygame

level1_map = [
    '                           ',
    '                           ',
    '                           ',
    '                  0         u',
    '          P 0          56  ',
    '   56    m9n          08426',
    '  013N    0              87',
    '   1026                    ',
    '  01X44999992226       N 0 ',
    '   87пППППп01XX3     m22n  ',
    '    Пп5226  10X30     87   ',
    '  52224447  8X0X26         ',
    '  84470      84447      0  ',
    '   0                       ',
    '                           ',
    '            5222222226     ',
    '  c  N    05XXXXXXXXXX60   ',
    '  899999999444444444444999n',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size
