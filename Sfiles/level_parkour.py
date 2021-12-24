import pygame
import random

from tiles_parkour import Tile, Portal, MovingTile, Gold, UpArrow, Web, Bridge, Bird, KeysAndDoors, Invisible, Resizer
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
        self.ready_bridge = False
        self.bridge_work = False
        self.build_bird = False
        self.is_invisible = False
        self.is_resizable = False
        self.resizer_worked = False
        self.cur_gold = ''
        self.last_bird_block = ''
        self.finsh_bridge = -100
        self.moving_t_direct = 'up'
        self.cur_key = ''
        self.height = pygame.display.Info().current_h
        text = f'GEMS COLLECTED: {gold_max - len(list(self.golds))}'
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
        self.bridge = pygame.sprite.Group()
        self.bird = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.open_doors = pygame.sprite.Group()
        self.key_screen = pygame.sprite.Group()
        self.invisible = pygame.sprite.Group()
        self.resizer = pygame.sprite.Group()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(level_parkour_map)
        self.tile_size = tile_size

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
                    tile = Gold((col_index, row_index), tile_size, cell)
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
                elif cell == 'B':
                    tile = Bridge((col_index, row_index), tile_size, cell)
                    self.bridge.add(tile)
                elif cell == 'b':
                    tile = Bridge((col_index, row_index), tile_size, cell)
                    self.bridge.add(tile)
                elif cell == 'R':
                    tile = Bird((col_index, row_index), tile_size, cell)
                    self.bird.add(tile)
                elif cell == 'x':
                    tile = Bird((col_index, row_index), tile_size, cell)
                    self.bird.add(tile)
                elif cell == 'D':
                    tile = Bird((col_index, row_index), tile_size, cell)
                    self.bird.add(tile)
                elif cell == 'd':
                    tile = Bird((col_index, row_index), tile_size, cell)
                    self.bird.add(tile)
                elif cell == 'g':
                    tile = Gold((col_index, row_index), tile_size, cell)
                    self.golds.add(tile)
                elif cell in 'йцукенгшщ':
                    item = KeysAndDoors((col_index, row_index), tile_size, cell)
                    self.doors.add(item)
                elif cell in 'ЙЦУКЕНГШЩ':
                    item = KeysAndDoors((col_index, row_index), tile_size, cell)
                    self.keys.add(item)
                elif cell == 'I':
                    item = KeysAndDoors((col_index, row_index), tile_size, cell)
                    self.key_screen.add(item)
                elif cell in 'VY':
                    item = Invisible((col_index, row_index), tile_size, cell)
                    self.invisible.add(item)
                elif cell in 'ZCc':
                    item = Resizer((col_index, row_index), tile_size, cell)
                    self.resizer.add(item)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, level_parkour_map, self.player_col)
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

        for sprite in self.doors.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

        for sprite in self.bridge.sprites():
            if sprite.cell == 'B':
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.direction.x = 0
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.direction.x = 0
            else:
                if self.bridge_work:
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

        for sprite in self.doors.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.01

        for sprite in self.bridge.sprites():
            if sprite.cell == 'B':
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = -0.01
            else:
                if self.bridge_work:
                    sprite.update_vision(True)
                    if sprite.rect.colliderect(player.rect):
                        if player.direction.y > 0:
                            player.rect.bottom = sprite.rect.top
                            player.direction.y = 0
                        elif player.direction.y < 0:
                            player.rect.top = sprite.rect.bottom
                            player.direction.y = -0.01
                else:
                    sprite.update_vision(False)

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
        text = f'GEMS COLLECTED: {gold_max - len(list(self.golds))}'
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
                    for el in list(filter(lambda x: x.cell == 'a', list(self.up_arrows))):
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

    def check_bridge(self):
        player = self.player.sprite
        s = 0
        for block in self.bridge:
            if block.cell == 'B':
                s = block.rect.x, block.rect.y
        rec = pygame.Rect(s[0], s[1] - self.tile_size - 2, self.tile_size, self.tile_size)
        if rec.colliderect(player.rect):
            self.ready_bridge = True

    def build_bridge(self, finish, cur):
        if self.finsh_bridge == -100:
            self.finsh_bridge = finish
        if cur < self.finsh_bridge:
            self.bridge_work = True
        else:
            self.bridge_work = False
            self.ready_bridge = False
            self.finsh_bridge = -100

    def check_bird(self):
        player = self.player.sprite
        for bird in self.bird:
            if bird.cell == 'R':
                if bird.rect.colliderect(player.rect):
                    self.build_bird = True
                    for gold in self.golds:
                        if gold.cell == 'g':
                            gold.update_bird_gems(True)

    def make_bird(self):
        player = self.player.sprite
        player.bird_mode = True
        for bird in self.bird:
            if bird.cell == 'd':
                bird.image.fill((102, 255, 0, 90))
                if bird.rect.colliderect(player.rect):
                    self.build_bird = False
                    player.bird_mode = False
                    self.last_bird_block = 'd'
            elif bird.cell == 'D':
                bird.image.fill((255, 0, 0, 90))
                if bird.rect.colliderect(player.rect):
                    self.build_bird = False
                    player.bird_mode = False
                    self.last_bird_block = 'D'
            elif bird.cell == 'R':
                bird.image.fill((255, 0, 0, 0))

    def crush_bird(self):
        for gold in self.golds:
            if gold.cell == 'g':
                gold.update_bird_gems(False)
        if self.last_bird_block == 'D':
            self.check_fall = True
        else:
            for bird in self.bird:
                if bird.cell == 'd':
                    bird.image.fill((0, 255, 0, 0))
                elif bird.cell == 'D':
                    bird.image.fill((255, 0, 0, 0))

    def check_key(self):
        player = self.player.sprite
        for key in self.keys:
            if key.rect.colliderect(player.rect):
                self.cur_key = key
                self.update_key_screen()
                self.keys.remove(key)

    def update_key_screen(self):
        for key in self.key_screen:
            key.update_screen(self.cur_key)

    def check_door(self):
        player = self.player.sprite
        for door in self.doors:
            if door.rect.colliderect(player.rect):
                self.compare_door_key(door)

    def compare_door_key(self, door):
        try:
            if door.cell.upper() == self.cur_key.cell:
                self.open_door(door)
        except:
            pass

    def open_door(self, door):
        door.open()
        self.doors.remove(door)
        self.open_doors.add(door)

    def check_invisible(self):
        player = self.player.sprite
        for item in self.invisible:
            if item.cell == 'V':
                if item.rect.colliderect(player.rect):
                    self.is_invisible = True
            else:
                if item.rect.colliderect(player.rect):
                    self.is_invisible = False

    def invisible_on(self):
        player = self.player.sprite
        player.invis_mode = True
        player.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 100)))

    def invisible_off(self):
        player = self.player.sprite
        player.invis_mode = False
        player.image = player.start_img

    def check_resizer(self):
        player = self.player.sprite
        for item in self.resizer:
            if item.cell == 'Z':
                if item.rect.colliderect(player.rect):
                    self.is_resizable = True
            elif item.cell == 'C':
                if item.rect.colliderect(player.rect):
                    self.is_resizable = False

    def resizer_on(self):
        player = self.player.sprite
        player.resize(True)
        self.resizer_worked = True

    def resizer_off(self):
        player = self.player.sprite
        if self.resizer_worked:
            player.resize_helper = 0
            player.resize(False)
        self.resizer_worked = False

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

        self.bridge.update((self.world_shift_x, self.world_shift_y))
        self.bridge.draw(self.display_surface)

        self.bird.update((self.world_shift_x, self.world_shift_y))
        self.bird.draw(self.display_surface)

        self.doors.update((self.world_shift_x, self.world_shift_y))
        self.doors.draw(self.display_surface)

        self.keys.update((self.world_shift_x, self.world_shift_y))
        self.keys.draw(self.display_surface)

        self.open_doors.update((self.world_shift_x, self.world_shift_y))
        self.open_doors.draw(self.display_surface)

        self.key_screen.update((self.world_shift_x, self.world_shift_y))
        self.key_screen.draw(self.display_surface)

        self.invisible.update((self.world_shift_x, self.world_shift_y))
        self.invisible.draw(self.display_surface)

        self.resizer.update((self.world_shift_x, self.world_shift_y))
        self.resizer.draw(self.display_surface)

        self.scroll_x()
        self.player.update()

        self.check_portals()
        self.check_gold()
        self.arrow_work()
        self.check_web()
        self.check_bridge()
        self.check_bird()
        self.check_key()
        self.check_door()
        self.check_invisible()
        self.check_resizer()

        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)

        self.move_tiles()
        self.moving_tiles.update((self.world_shift_x, self.world_shift_y))
        self.moving_tiles.draw(self.display_surface)
        self.print_current_gold()

        if self.player.sprite.rect.y > self.height:
            self.check_fall = True


