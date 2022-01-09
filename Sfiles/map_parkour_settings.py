import pygame

f = open('maps/map_parkour.txt', 'r')
level_parkour_map = [line.rstrip('\n') for line in f]
f.close()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
tile_size = HEIGHT // len(level_parkour_map)
screen_width = len(level_parkour_map[0]) * tile_size
screen_height = len(level_parkour_map) * tile_size
gold_max = 0
for el in level_parkour_map:
    for s in el:
        if s in ['G', 'g']:
            gold_max += 1