import pygame

f = open('maps/map_preparation.txt', 'r')
level1_map = [line.rstrip('\n') for line in f]
f.close()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level1_map)
screen_width = len(level1_map[0]) * tile_size
screen_height = len(level1_map) * tile_size