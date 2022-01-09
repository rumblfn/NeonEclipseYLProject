from copy import copy

import pygame

f = open('maps/map.txt', 'r')
map = [line.rstrip('\n') for line in f]
f.close()

map1 = copy(map)

f = open('maps/map2.txt', 'r')
map2 = [line.rstrip('\n') for line in f]
f.close()

f = open('maps/map3.txt', 'r')
map3 = [line.rstrip('\n') for line in f]
f.close()

f = open('maps/map4.txt', 'r')
map4 = [line.rstrip('\n') for line in f]
f.close()

f = open('maps/map5.txt', 'r')
map5 = [line.rstrip('\n') for line in f]
f.close()

try:
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    tile_size = HEIGHT // len(map)
    screen_width = len(map[0]) * tile_size
    screen_height = len(map) * tile_size
except:
    pass
