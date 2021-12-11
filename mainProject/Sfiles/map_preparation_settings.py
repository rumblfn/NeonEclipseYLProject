import pygame

level1_map = [
    '                                                                        ',
    '                     XX                                                 ',
    '        P            XX                                                 ',
    ' XX    XXX           XXXX     XX                   XXX                  ',
    ' XX                    XXXX         XXX                                 ',
    ' XXXX         XX                                                        ',
    ' XXXX       XXX                                                         ',
    ' XX       XXXX    XX  XX              XX    XXX                         ',
    '       X  XXXX    XX  XXX                                               ',
    '    XXXX  XXXXXX        XXXX                                            ',
    'XXXXXXXX  XXXXX                XXXXX                                    ',
    'XXXX                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    '             XXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    '          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size
