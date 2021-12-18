import pygame

map = [  # 18
    'XXXXXXXXXXXX',
    'XX        XX',
    'XX        XX',
    'XX        XX',
    'XX        XX',
    'XX        XX',
    'XX  P  E  XX',
    'XX        XX',
    'XXXXXXXXXXXX',
]

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(map)
screen_width = len(map[0]) * tile_size
screen_height = len(map) * tile_size
