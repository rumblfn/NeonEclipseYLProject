import pygame
from tiles_parkour import Tile, Portal, MovingTile, Gold, UpArrow, Web
from map_parkour_settings import level_parkour_map, gold_max
from player import Player_map_parkour


class LevelParkour:
    def __init__(self, level_data, surface, player_settings):
        self.display_surface = surface
        self.level_data = level_data
        self.player_settings = player_settings
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.player_col = 0
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.portalParkour = False
        self.check_fall = False
        self.gold_taken = False
        self.arrow_works = False
        self.in_web = False
        self.cur_gold = ''
        self.moving_t_direct = 'up'
        self.height = pygame.display.Info().current_h
        text = f'GOLD COLLECTED: {gold_max - len(list(self.golds))}'
        newFont = pygame.font.SysFont('SFCompact', 40)
        txt_surf = newFont.render(text, False, (255, 183, 0))
        self.txt_surf = txt_surf

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.moving_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.portals = pygame.sprite.Group()
        self.golds = pygame.sprite.Group()
        self.up_arrows = pygame.sprite.Group()
        self.webs = pygame.sprite.Group()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(level_parkour_map)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'P':
                    self.player_col = col_index // 2
                    break
            if self.player_col != 0:
                break

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                col_index -= self.player_col
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player_sprite = Player_map_parkour((x, y), self.player_settings)
                    self.player.add(self.player_sprite)
                elif cell == 'u':
                    portal = Portal((x, y))
                    self.portals.add(portal)
                elif cell == 'L':
                    tile = MovingTile((col_index, row_index), tile_size)
                    self.moving_tiles.add(tile)
                elif cell == 'G':
                    tile = Gold((col_index, row_index), tile_size)
                    self.golds.add(tile)
                elif cell == 'A':
                    tile = UpArrow((col_index, row_index), tile_size, cell)
                    self.up_arrows.add(tile)
                elif cell == 'a':
                    tile = UpArrow((col_index, row_index), tile_size, cell)
                    self.up_arrows.add(tile)
                elif cell == 'W':
                    tile = Web((col_index, row_index), tile_size)
                    self.webs.add(tile)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, level_parkour_map)
                    self.tiles.add(tile)

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

    def check_portals(self):
        player = self.player.sprite
        if player.K_x:
            for portal in self.portals:
                if portal.rect.colliderect(player.rect):
                    self.portalParkour = True
                    return True

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
        self.scroll_x()
        self.player.update()
        self.player.draw(self.display_surface)

    def check_gold(self):
        player = self.player.sprite
        for gold in self.golds:
            if gold.rect.colliderect(player.rect):
                self.gold_taken = True
                self.cur_gold = gold

    def take_gold(self):
        self.golds.remove(self.cur_gold)
        text = f'GOLD COLLECTED: {gold_max - len(list(self.golds))}'
        newFont = pygame.font.SysFont('SFCompact', 40)
        txt_surf = newFont.render(text, False, (255, 183, 0))
        self.txt_surf = txt_surf
        self.print_current_gold()

    def print_current_gold(self):
        self.display_surface.blit(self.txt_surf, (20, 20))

    def arrow_work(self):
        player = self.player.sprite
        for arrow in self.up_arrows:
            if arrow.rect.colliderect(player.rect):
                if arrow.cell == 'a':
                    if arrow.able:
                        self.arrow_works = True
                    arrow.able = False
                if arrow.cell == 'A':
                    for el in list(self.up_arrows)[1:]:
                        el.able = True
                    self.arrow_works = True

    def raise_player(self):
        self.player_sprite.levitate()

    def check_web(self):
        player = self.player.sprite
        for web in self.webs:
            if web.rect.colliderect(player.rect):
                self.in_web = True
                return
            self.in_web = False

    def web_work(self, arg):
        if arg:
            self.player_sprite.web(True)
        else:
            self.player_sprite.web(False)

    def run(self):
        self.tiles.update((self.world_shift_x, self.world_shift_y))
        self.tiles.draw(self.display_surface)

        self.portals.update((self.world_shift_x, self.world_shift_y))
        self.portals.draw(self.display_surface)

        self.golds.update((self.world_shift_x, self.world_shift_y))
        self.golds.draw(self.display_surface)

        self.up_arrows.update((self.world_shift_x, self.world_shift_y))
        self.up_arrows.draw(self.display_surface)

        self.webs.update((self.world_shift_x, self.world_shift_y))
        self.webs.draw(self.display_surface)

        self.scroll_x()
        self.player.update()

        self.check_portals()
        self.check_gold()
        self.arrow_work()
        self.check_web()

        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)

        self.move_tiles()
        self.moving_tiles.update((self.world_shift_x, self.world_shift_y))
        self.moving_tiles.draw(self.display_surface)
        self.print_current_gold()

        if self.player.sprite.rect.y > self.height:
            self.check_fall = True


