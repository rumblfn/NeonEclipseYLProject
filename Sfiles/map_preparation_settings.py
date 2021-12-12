import pygame

level1_map = [
    '                                                               ',
    '                                                               ',
    '                                                               ',
    '                     56                                        ',
    '        P 0          13       0                     0          ',
    ' 56    526           8X26     8                    526         ',
    ' 13                    8426    1    526                        ',
    ' 1X26         56               1                               ',
    ' 10XX222222226                 1            526      5         ',
    ' 87       10X3       522226   2       56     8      5     56   ',
    '    5226  1XX3        44     2                222222           ',
    '5222X447  8X0X26            2                    847           ',
    '8447       84447               5226                 126        ',
    '                            522    5226                226     ',
    '                         522      5    X22222226               ',
    '          5222222226             5              6              ',
    '6        5          6           5                226    5222226',
    ' 22222222            22222222222                    2222       ',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size
