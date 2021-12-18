import pygame
from tiles import Tile
from main_map_settings import *


class LevelG:
    def __init__(self, level_data, surface, player):
        self.display_surface = surface
        self.level_data = level_data
        self.player_sprite = player
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.player_col = 0
        self.pos_x = 0
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.portalParkour = False

    def setup_level(self, layout, default_player=False):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(map)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'P':
                    self.player_col = col_index // 2
                    break
            if self.player_col != 0:
                break
        self.player_col = 0

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                # col_index -= self.player_col
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player.add(self.player_sprite)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, map, self.player_col)
                    self.tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < self.width / 2 and direction_x < 0:
            # self.world_shift_x = player.control_speed
            player.speed = 8
        elif player_x >= self.width / 2 and direction_x > 0:
            # self.world_shift_x = -player.control_speed
            player.speed = -8
        else:
            self.world_shift_x = 0
            player.speed = player.control_speed

    def horizontal_movement_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

    def vertical_movement_collisions(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.01

    def run(self):
        self.tiles.update((self.world_shift_x, self.world_shift_y))
        self.tiles.draw(self.display_surface)

        self.scroll_x()

        self.player.update()
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)