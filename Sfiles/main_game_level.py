import pygame
from tiles import Tile
from main_map_settings import *
from enemyClass import Enemy_hero1, Enemy
from _thread import start_new_thread
from player import speed_to_low


class LevelG:
    def __init__(self, level_data, surface, player_main, player_enemy, network, server_player, interface):
        self.display_surface = surface
        self.level_data = level_data
        self.player_sprite = player_main
        self.player_enemy = player_enemy
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        self.server_player = server_player
        self.player_col = 0
        self.pos_x = 0
        self.network = network
        self.interface = interface

        self.enemy = pygame.sprite.GroupSingle()
        if self.player_enemy.name == 'Hero1':
            self.enemy_hero1_bullets = pygame.sprite.Group()
            enemy = Enemy_hero1(self.player_enemy)
        else:
            enemy = Enemy(self.player_enemy)

        self.enemy.add(enemy)
        self.setup_level(level_data)

    def setup_level(self, layout, default_player=False):
        self.interface.update_screen_size(self.width, self.height)
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        tile_size = self.height // len(map)
        self.width = len(map[0]) * tile_size
        self.player_sprite.initialize_server_player(self.server_player)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player_sprite.server_player.x = x
                    self.player_sprite.server_player.y = y
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

    def update_enemy(self):
        self.player_sprite.update_server()

        player_enemy = self.network.send(self.player_sprite.server_player)
        self.server_player.E = False
        self.server_player.damage_given = 0

        self.enemy.sprite.rect.x = (player_enemy.x / 1920) * self.width
        self.enemy.sprite.rect.y = (player_enemy.y / 1080) * self.height
        self.player_sprite.hp -= player_enemy.damage_given
        self.server_player.hp -= player_enemy.damage_given
        self.enemy.sprite.update_values(player_enemy)

        if player_enemy.name == 'Hero1':
            self.enemy.sprite.get_input()
            if player_enemy.simpleAttack:
                self.enemy_hero1_bullets.add(self.enemy.sprite.create_bullet((player_enemy.mouse_pos_x, player_enemy.mouse_pos_y)))

            for sprite in self.enemy_hero1_bullets.sprites():
                if sprite.rect.colliderect(self.player_sprite.rect):
                    sprite.kill()
                for tile in self.tiles.sprites():
                    if tile.rect.collidepoint(sprite.rect.center):
                        sprite.kill()
                sprite.move()

            self.enemy.sprite.attacksE.draw(self.display_surface)
            for sprite in self.enemy.sprite.attacksE.sprites():
                sprite.rect.midbottom = self.enemy.sprite.rect.midbottom
                sprite.run_attackE()
                if sprite.rect.colliderect(self.player_sprite.rect):
                    if sprite.rect.x < self.player_sprite.rect.x:
                        self.player_sprite.rect.left = sprite.rect.right
                    else:
                        self.player_sprite.rect.right = sprite.rect.left
                    start_new_thread(speed_to_low, (self.player_sprite,))

            self.enemy_hero1_bullets.draw(self.display_surface)

    def bullets_settings(self):
        for sprite in self.player_sprite.bullets.sprites():
            for tile in self.tiles.sprites():
                if tile.rect.collidepoint(sprite.rect.center):
                    sprite.kill()
            sprite.move()

    def ESettings(self):
        for sprite in self.player_sprite.attacksE:
            sprite.rect.midbottom = self.player_sprite.rect.midbottom
            sprite.run_attackE()

    def run(self):
        self.tiles.draw(self.display_surface)

        self.horizontal_movement_collisions(self.player.sprite)
        self.vertical_movement_collisions(self.player.sprite)

        self.enemy.draw(self.display_surface)
        self.update_enemy()

        self.player.update()
        self.player.draw(self.display_surface)

        if self.player_sprite.name == 'Hero1':
            self.player_sprite.bullets.draw(self.display_surface)
            self.player_sprite.attacksE.draw(self.display_surface)
            for sprite in self.player_sprite.bullets.sprites():
                if sprite.rect.colliderect(self.enemy.sprite.rect):
                    self.enemy.sprite.hp -= self.player_sprite.power
                    self.server_player.damage_given = self.player_sprite.power
                    sprite.kill()
            self.ESettings()
            self.bullets_settings()
        elif self.player_sprite.name == 'Hero2':
            pass
        elif self.player_sprite.name == 'Hero3':
            pass

        self.interface.draw(self.player_sprite.hp, self.player_sprite.maxHp, self.player_sprite.power)
        self.interface.draw_enemy_health(self.enemy.sprite.hp, self.enemy.sprite.maxHp)