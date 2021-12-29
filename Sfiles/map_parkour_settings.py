import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                00000000   G   00000000                                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXGGGGGGGX   0   0                                       0000   0000                                         0              GXXШ     a XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXGWWWWWW XXXXXXXXX            0                  0                 Z 0 0 V                 0                 0             Y       uXXXXXXXXXa к ЙXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   a                                            0   00000 00     00 00000   0                                      0      GXXXЩ    г aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXX                0      0      0                     0   0                     0      0      0                    GXXXXXXXXXXXa ц УXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXXX                                                    0 0        DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD   GXXXXК     у aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXG a  XXXXXaXXXXX                                                    0 0         d D   D   D   D   D   D   D   D   D        D XXXXXXXXXXXXXXXa е НXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaX  XXXXAXXXXX                                                    0 0         d D   D   g   D   g   D   D   D   D        D XXXXXXЦ      н aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXX      XXXXX                                                    0 0         d g   D       D           D   g   D        D XXXXXXXXXXXXXXXa щ ЕXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXX                               00000000G00000000                   d g           D       g           g        D XXXIXGGGGGGGGй aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXu P                               0    0    0          0L0         d g   g   D   g   D       g                D XXXXXXXXXXXXXXXa ш ГXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX0  0                                                            d D       D       D   D       D            D  XXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXG           0                    0       0           0G0         d D   D   D       D   D   D   D   D      R D                aXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                   0                0        000    000    000  DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                                              G0           0G                                      XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXAXXXX                                    0                 000           000                                      XXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXX                                                              G                                                              GXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                         00000B   bbb    bbb   b   b    bb       bXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
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
