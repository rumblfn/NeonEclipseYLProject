import pygame
from tiles import Tile
from main_map_settings import *
from enemyClass import Enemy


class LevelG:
    def __init__(self, level_data, surface, player_main, player_enemy, network, server_player):
        self.display_surface = surface
        self.level_data = level_data
        self.player_sprite = player_main
        self.player_enemy = player_enemy
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        self.player_col = 0
        self.pos_x = 0
        self.network = network
        self.server_player = server_player

        self.enemy = pygame.sprite.GroupSingle()
        enemy = Enemy(self.player_enemy)
        self.enemy.add(enemy)

        self.setup_level(level_data)

    def setup_level(self, layout, default_player=False):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        tile_size = self.height // len(map)
        self.width = len(map[0]) * tile_size

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.server_player.x = x
                    self.server_player.y = y
                    self.player_sprite.x = x
                    self.player_sprite.y = y
                    self.enemy.sprite.rect.x = x
                    self.enemy.sprite.rect.y = y
                    self.player.add(self.player_sprite)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, map, self.player_col)
                    self.tiles.add(tile)

    def horizontal_movement_collisions(self, player):
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

    def vertical_movement_collisions(self, player):
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.01

    def update_enemy_pos(self):
        self.server_player.x = (self.player.sprite.rect.x / self.width) * 1920
        self.server_player.y = (self.player.sprite.rect.y / self.height) * 1080

        player_enemy = self.network.send(self.server_player)
        self.enemy.sprite.rect.x = (player_enemy.x / 1920) * self.width
        self.enemy.sprite.rect.y = (player_enemy.y / 1080) * self.height

    def bullets_settings(self):
        for sprite in self.player_sprite.bullets.sprites():
            for tile in self.tiles.sprites():
                if tile.rect.collidepoint(sprite.rect.center):
                    sprite.kill()
            sprite.move()

    def run(self):
        self.tiles.draw(self.display_surface)
        self.update_enemy_pos()

        # self.scroll_x(self.player.sprite)
        self.horizontal_movement_collisions(self.player.sprite)
        self.vertical_movement_collisions(self.player.sprite)

        self.player.update()
        self.player.draw(self.display_surface)
        self.enemy.draw(self.display_surface)
        self.player_sprite.bullets.draw(self.display_surface)
        self.bullets_settings()