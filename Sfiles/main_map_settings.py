import pygame

map = [
    '                               ',
    '           P                   ',
    '                               ',
    '                  XXXX         ',
    '                  XXXXXXXX     ',
    '                    XXXX       ',
    '   XXXXX                       ',
    '   XXXXX        XX             ',
    ' XXXXXXXX       XXXXX          ',
    ' XXXXXXXX        XXXX          ',
    '  XXXXX                        ',
    '  XXXXX                        ',
    '   XX                XXX       ',
    '                     XXX       ',
    '                               ',
    '            XXXXXX             ',
    '             XXXX              ',
    '                               ',
    '                               ',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(map)
screen_width = len(map[0]) * tile_size
screen_height = len(map) * tile_size
