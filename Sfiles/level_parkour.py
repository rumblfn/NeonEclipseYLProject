import pygame
from tiles_parkour import Tile, Portal, MovingTile
from map_parkour_settings import level_parkour_map
from player import Player_map_parkour


class LevelParkour:
    def __init__(self, level_data, surface, player_settings):
        self.display_surface = surface
        self.level_data = level_data
        self.player_settings = player_settings
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.portalParkour = False
        self.check_fall = False
        self.moving_t_direct = 'up'
        self.height = pygame.display.Info().current_h

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.moving_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.portals = pygame.sprite.Group()
        self.npces = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(level_parkour_map)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player_sprite = Player_map_parkour((x, y), self.player_settings)
                    self.player.add(self.player_sprite)
                    print(self.player_sprite)
                elif cell == 'u':
                    portal = Portal((x, y))
                    self.portals.add(portal)
                elif cell == 'L':
                    tile = MovingTile((col_index, row_index), tile_size)
                    self.moving_tiles.add(tile)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, level_parkour_map)
                    self.tiles.add(tile)

    def check_portals(self):
        player = self.player.sprite
        if player.K_x:
            for portal in self.portals:
                if portal.rect.colliderect(player.rect):
                    self.portalParkour = True
                    return True

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < self.width / 2 and direction_x < 0:
            self.world_shift_x = player.control_speed
            player.speed = 0
        elif player_x >= self.width / 2 and direction_x > 0:
            self.world_shift_x = -player.control_speed
            player.speed = 0
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

        for sprite in self.moving_tiles.sprites():
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

        for sprite in self.moving_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.01

    def move_tiles(self):
        last_y = 0
        if self.moving_t_direct == 'up':
            for tile in self.moving_tiles:
                tile.rect.y -= 1
                last_y = tile.rect.y
            if last_y <= self.height // 5:
                self.moving_t_direct = 'down'

        if self.moving_t_direct == 'down':
            for tile in self.moving_tiles:
                tile.rect.y += 1
                last_y = tile.rect.y
            if last_y >= self.height // 5 * 3:
                self.moving_t_direct = 'up'

    def run(self):
        self.tiles.update((self.world_shift_x, self.world_shift_y))
        self.tiles.draw(self.display_surface)

        self.portals.update((self.world_shift_x, self.world_shift_y))
        self.portals.draw(self.display_surface)

        self.scroll_x()

        self.player.update()
        self.check_portals()
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)

        self.move_tiles()
        self.moving_tiles.update((self.world_shift_x, self.world_shift_y))
        self.moving_tiles.draw(self.display_surface)

        if self.player.sprite.rect.y > self.height:
            self.check_fall = True


