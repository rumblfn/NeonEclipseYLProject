import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                                XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         0         0         0         0         0          0 0 0                                               XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXG WWWW  XXXXXXXX                                                                                                                XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  a                    0         0         0         0              0 0 0 0                                           XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXX           0         0         0                   0          0   0                                          XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXaXXXXX                                                                                                            XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXG a  XXXXXaXXXXX                                                                                                            XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaX  XXXXAXXXXX                                                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXX      XXXXX                               P                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXX                                 00000 0000 00         L                                                          XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXu    0                          0     0    0  00                                                                  XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                                    0  0      00                                                               XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXG           0                    0        0  0        G                                                        XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                   0                0        0000   000                                                 XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXaXXXXXXXXXXXXX                                                0    0                                                  XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXAXXXX                                    0                0 0G0    G     00 00                                       XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXX                                             0     0      G                                                               XXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                  0     0000Bbb bbb    bbb   b   b  b bb b  b  b   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
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
