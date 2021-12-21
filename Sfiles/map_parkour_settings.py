import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                                  XXXс     aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXGWWWWWW  XXXXXXXX                                                                                                                 XXXXXXXXXXa к оXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  a                                                                                                                      XXXXм    г aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXX                                                                                                                 XXXXXXXXXXXXa ц дXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXXX                                                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD   XXXXXж     у aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXG a  XXXXXaXXXXX                                                                d D   D   D   D   D   D   D   D   D        D  XXXXXXXXXXXXXXa е яXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaX  XXXXAXXXXX                                               0                d D   D   g   D   g   D   D   D   D        D XXXXXXл      н aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXX      XXXXX                                               0                d g   D       D           D   g   D        D XXXXXXXXXXXXXXXa щ эXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXX                                 00000 0000 00   0     L          d g           D       g           g        D XXXXXGGGGGGGGй aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXuP   0                          0     0    0  00 0                d g   g   D   g   D       g                D XXXXXXXXXXXXXXXa ш чXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                                    0  0      00                d D       D       D   D       D            D XXXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXG           0                    0        0  0        G          d D   D   D       D   D   D   D   D      R D                aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                   0                0        000    000         DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                                              G0                                                   XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXAXXXX                                    0                0 00           00 00                                    XXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXX                                                          G                                                            GGG XXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX00000B   bbb    bbb   b   b    bb       bXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level_parkour_map)
screen_width = len(level_parkour_map[0]) * tile_size
screen_height = len(level_parkour_map) * tile_size
gold_max = 0
for el in level_parkour_map:
    for s in el:
        if s in ['G', 'g']:
            gold_max += 1
