import pygame

level_parkour_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXX                                      XXXX         XXXXXXXX     XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX             XXXX                                                     XXXX          XXXXX       XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX               XXXX                   XXXXX              XX             XXXXXXXXX     XXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX         XXX     XX                   XXXXX          XXXXXX             XXXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXX    XXX     XX   XXX0XXXXXXXXXXXXXXX            XX        XXXXXX    XXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXN                XXXXX         XXXXX     XX               XXXXXX    XXXXXXXX     XXXXX  XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXXX                                       XXXXX            XXXXXX      XXXXXX     XXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXXX     XXXX                              XXXXX          XXXXXXXXXX    XXXXXX   XXXXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXX     XXXX u  XXXX      XXXX          XXXXX       XXX          XXXXXXXXXX             XXXXXXXXX    XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXX     XXXX    XXXXXX    XX     XXXX   XXXXX       XXX             XXXXXXXX            XXX  XXXX    XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXXX   XXX0X           XXXX     XXX       XXXXXXXX           XXXXX  XXXXXXX              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXXX   XXXX                     XXX     XXXXXXXXXX                  XXXXXXX              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX     XXX                                      XXXXXXXX         XX         XXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                              XXXXXX           XX            XXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX        P                    0XXXX        XXXXXXXX           XXXX            XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX        XXXXXXX0XXXXXX     XXXXXXX        XXXXXXXXXX         XXXX            XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXX     XXXXXXXXX      XXXXXXXXXXXXXXXX   XXX      XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level_parkour_map)
screen_width = len(level_parkour_map[0]) * tile_size
screen_height = len(level_parkour_map) * tile_size
