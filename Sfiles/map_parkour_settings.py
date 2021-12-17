import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXX                                                                                                              XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXX0XXXXXX          0         0         0         0         0          0 0 0                                               XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX   P                                                                                                           XXXXX0XXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX     0         0         0         0         0              0 0 0 0                                           XXXXXXXXXXXXXXXXXXXXX',
    'XXX0XXXXXXXXXXXXXX          0         0         0         0         0          0   0                                          XXXXXXXXXXXXXXX0XXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                                                                                            XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                                                                                            XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXX0XXXXXXXXXX                                                                                                              XXXX0XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXX                                                        L                                                         XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXu    0                                                                                                            XXXXXXXXXXXXX0XXXXX',
    'XXXXX0XXXXXXXXXXXX                                                                                                              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX         0       0                                                                                            XXXXXX0XXXXXXXXXXXXXX',
    'XXXXXXXXXXXX0XXXXX                                                                                                        XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX                      0         0                                                                       XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX                                             0       0                                               XXXXXXXXXXXXXXXXXXXXXX0XXXXXX',
    'XXXXX0XXXXXXXXXXXXXX                         0         0                                                                XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXX                                          00    0                                                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level_parkour_map)
screen_width = len(level_parkour_map[0]) * tile_size
screen_height = len(level_parkour_map) * tile_size
