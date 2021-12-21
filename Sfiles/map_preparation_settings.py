import pygame

level1_map = [  # 18
    'XXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXX                                      XXXX         XXXXXXXX     XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX        P    XXXX                                                     XXXX          XXXXX       XXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX               XXXX                   XXXXX              XX             XXXXXXXXX     XXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX         XXXXXXXXXX                   XXXXX          XXXXXX             XXXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXX    XXXXXXXXXX   XXXXXXXXXXXXXXXXXXX            XX        XXXXXX    XXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXN                XXXXX         XXXXX     XX               XXXXXX    XXXXXXXX     XXXXX  XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXXX                                       XXXXX            XXXXXX      XXXXXX     XXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX  XXXXX     XXXX       N                      XXXXX          XXXXXXXXXX    XXXXXX   XXXXXXX    XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXX     XXXX u  XXXX      XXXX          XXXXX       XXX          XXXXXXXXXX             XXXXXXXXX    XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXX     XXXX    XXXXXX    XX     XXXX   XXXXX       XXX             XXXXXXXX            XXX  XXXX    XXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXXX   XXXXX           XXXX     XXX       XXXXXXXX           XXXXX  XXXXXXX              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXXX   XXXX                     XXX     XXXXXXXXXX                  XXXXXXX              XXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX     XXX                                      XXXXXXXX         XX         XXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX                                              XXXXXX           XX            XXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX          XXXXXXXXXX         XXXXX        XXXXXXXX           XXXX            XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX N      XXXXXXXXXXXXXX     XXXXXXX        XXXXXXXXXX         XXXX            XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXX     XXXXXXXXX      XXXXXXXXXXXXXXXX   XXX      XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size