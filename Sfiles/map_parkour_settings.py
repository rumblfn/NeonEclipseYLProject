import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXX                                                                                                              XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXX0XXXXXXG         0         0         0         0         0          0 0 0                                               XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX                                                                                                               XXXXX0XXXXXXXXXXXX',
    'XXXXXXXXXXXXXX0XXX     0         0         0         0         0              0 0 0 0                                           XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXX0XXXXXXXXXXX          0         0         0         0         0          0   0                                          XXXXXXXXXXXXXXX0XXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                                                                                            XXXXXXXXXXXXXXXXXXXXXXX',
    'XXG    XXXXX                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXaX  XXX  XXXXX                                                                                                              XXXX0XXXXXXXXXXXXXXXX',
    'XXXXaXX     XX0XXX                                                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXaXXXXXXXXXXX                                                         L                                                        XXXXXXXXXXXXXXXXXXX',
    'XXXXaXXXXXX0XXXXuP   0                                                                                                            XXXXXXXXXXXXX0XXXXX',
    'XXXXaXXXXXXXXXXXXX                                                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXaXXXX0XXXXXXXG         0       0                                   G                                                        XXXXXX0XXXXXXXXXXXXXX',
    'XXXXaXXXXXXX0XXXXX                                                    000                                                 XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXaXXXXXXXXXXXXX                      0         0                                                                       XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXAXXXX                                                  0    0                                                       XXXXXXXXXXXXXXXXXXXXXX0XXXXXX',
    'XXXX      XXXXXXXXXX                         0         0                                                                XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXX                                                                                                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level_parkour_map)
screen_width = len(level_parkour_map[0]) * tile_size
screen_height = len(level_parkour_map) * tile_size
gold_max = 0
for el in level_parkour_map:
    for s in el:
        if s == 'G':
            gold_max += 1
