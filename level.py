import pygame
from tiles import Tile, Portal, Potion, Chest
from map_preparation_settings import level1_map
from Hero1Player import Player_hero1
from Hero3Player import Player_hero3
from NPC import Librarian, BlackSmith
from random import randrange
from Enemy import Enemy
from dataConsts import bgMapPreparation
from pygame.locals import *


class Level:
    def __init__(self, level_data, surface, player_settings, interface, sleeper_time):
        self.sleeper_time = sleeper_time
        self.display_surface = surface
        self.level_data = level_data
        self.player_settings = player_settings
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.player_col = 0
        self.pos_x = 0
        self.interface = interface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.portalParkour = False
        self.showed_inv_by_shop = False
        self.item_clicked = False
        self.first_start = True
        self.is_on_check = False

    def setup_level(self, layout, default_player=False):
        self.interface.update_screen_size(self.width, self.height)
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.decoration = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.portals = pygame.sprite.Group()
        self.npces = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.potions = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        HEIGHT = pygame.display.Info().current_h
        tile_size = HEIGHT // len(level1_map)

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
                # tile = Tile((col_index, row_index), tile_size, 'bg', level1_map)
                # self.decoration.add(tile)
                if cell == 'P':
                    if not default_player:
                        if self.player_settings['name'] == 'Hero1':
                            self.player_sprite = Player_hero1((x, y), self.player_settings)
                        elif self.player_settings['name'] == 'Hero3':
                            self.player_sprite = Player_hero3((x, y), self.player_settings)
                        self.player_sprite.block_moving = False
                        self.player.add(self.player_sprite)
                        self.all_sprites.add(self.player_sprite)
                    else:
                        pos = default_player.started_pos
                        default_player.rect = default_player.image.get_rect(topleft=(pos[0], pos[1] - 300))
                        self.player_sprite = default_player
                        self.player.add(self.player_sprite)
                        self.all_sprites.add(self.player_sprite)
                elif cell == 'u':
                    portal = Portal((x, y))
                    self.portals.add(portal)
                    self.all_sprites.add(portal)
                elif cell == 'B':
                    npc = BlackSmith((x, y), len(self.npces.sprites()), self.display_surface, self.player_settings['name'])
                    self.npces.add(npc)
                    self.all_sprites.add(npc)
                elif cell == 'L':
                    npc = Librarian((x, y), len(self.npces.sprites()), self.display_surface, self.player_settings['name'])
                    self.npces.add(npc)
                    self.all_sprites.add(npc)
                elif cell == 'п' or cell == 'П':
                    tile = Tile((col_index, row_index), tile_size, cell, level1_map, self.player_col)
                    self.decoration.add(tile)
                    self.all_sprites.add(tile)
                elif cell == 'V':
                    potion = Potion((col_index, row_index), tile_size, cell)
                    self.potions.add(potion)
                elif cell == 'G':
                    potion = Potion((col_index, row_index), tile_size, cell)
                    self.potions.add(potion)
                elif cell == 'Y':
                    potion = Potion((col_index, row_index), tile_size, cell)
                    self.potions.add(potion)
                elif cell == 'C':
                    chest = Chest((col_index, row_index), tile_size, cell)
                    self.chests.add(chest)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, level1_map, self.player_col)
                    self.tiles.add(tile)
                    self.all_sprites.add(tile)
        for i in range(randrange(1, 3)):
            enemy = Enemy(self)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)

    def check_portals(self):
        player = self.player.sprite
        if player.K_x:
            for portal in self.portals:
                if portal.rect.colliderect(player.rect):
                    self.player_settings['b_cards'] = 0
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

    def player_pos_checker(self):
        player = self.player_sprite
        if player.rect.y > self.height + 300 or player.rect.y < - 300:
            self.setup_level(self.level_data, self.player_sprite)
            for sprite in self.npces.sprites():
                if sprite.name == 'librarian':
                    sprite.bought_items = []
                if sprite.name == 'blacksmith':
                    sprite.bought_items = []
            self.interface.inventory = []
            self.interface.item_rects = []
            self.interface.bought_items_interface = []
            self.interface.current_item = 0
            self.interface.inventory_visible = False
            self.player_settings['keys'] = 0
            self.player_settings['b_cards'] = 0
            self.player_sprite.set_first_params()

    def npc_collisions(self):
        player = self.player.sprite
        for sprite in self.npces.sprites():
            if sprite.name == 'librarian':
                sprite.update_npc()
                if sprite.rect.colliderect(player.rect):
                    player.interface_mode = True
                    sprite.show_msg()
                    sprite.check_show_info(self.is_on_check)
                    sprite.check_click(self.player_settings)
                    self.interface.add_inventory_librarian(sprite.bought_items, sprite.items)
                    self.interface.show_inventory(False)
                    self.showed_inv_by_shop = True
                else:
                    if self.showed_inv_by_shop:
                            player.interface_mode = False
                            self.interface.show_inventory(True)
                            self.showed_inv_by_shop = False
            else:
                if sprite.rect.colliderect(player.rect):
                    player.interface_mode = True
                    sprite.show_msg()
                    sprite.check_show_info(self.is_on_check)
                    sprite.check_click(self.player_settings)
                    self.interface.add_inventory_blacksmith(sprite.bought_items, sprite.items)
                    self.interface.show_inventory(False)
                    self.showed_inv_by_shop = True
                else:
                    if self.showed_inv_by_shop:
                            player.interface_mode = False
                            self.interface.show_inventory(True)
                            self.showed_inv_by_shop = False

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
                    # player.direction.y = 0  # feature

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

    def print_current_gold(self):
        text = f'GEMS: {self.player_settings["gold"]}'
        s = 130
        if self.player_settings["gold"] > 9:
            s = 150
        newFont = pygame.font.SysFont('SFCompact', round((40 * self.width) / 1536))
        txt_surf = newFont.render(text, False, (255, 183, 0))
        self.display_surface.blit(txt_surf, (self.width - round((s * self.width) / 1536), round((20 * self.width) / 1536)))

    def add_keys_to_inv(self):
        self.interface.update_keys_in_inventory(self.player_settings["keys"])

    def check_inventory(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.interface.chest_rect.collidepoint((mx, my)):
                    self.player.sprite.interface_mode = True
                    self.interface.show_inventory()
                else:
                    self.player.sprite.interface_mode = False
                for i, rect in enumerate(self.interface.item_rects):
                    if rect.collidepoint((mx, my)):
                        self.interface.current_item = i
                        self.item_clicked = True
                        self.player.sprite.interface_mode = True
                if not self.item_clicked:
                    self.player.sprite.interface_mode = False
                    self.item_clicked = False
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_TAB]:
                    self.interface.show_inventory()
                if keys[pygame.K_RIGHT]:
                    self.interface.current_item -= 1
                    if self.interface.current_item < 0:
                        self.interface.current_item = len(self.interface.inventory) - 1
                if keys[pygame.K_LEFT]:
                    self.interface.current_item += 1
                    if self.interface.current_item > len(self.interface.inventory) - 1:
                        self.interface.current_item = 0

    def check_potions_taken(self):
        player = self.player.sprite
        for pot in self.potions:
            if pot.rect.colliderect(player.rect):
                self.take_potion(pot)

    def take_potion(self, potion):
        self.potions.remove(potion)
        self.interface.add_inventory_potions(potion, potion.all_potions)

    def check_chest(self):
        player = self.player.sprite
        if player.K_x:
            for chest in self.chests:
                if chest.rect.colliderect(player.rect):
                        self.open_chest(chest)

    def open_chest(self, chest):
        if not chest.opened:
            if self.interface.keys_count - 1 >= 0:
                self.interface.keys_count -= 1
                self.player_settings["keys"] -= 1
                chest.redraw_block()
                chest.opened = True
                self.interface.add_blacksmith_card(self.player_settings, chest)

    def check_sprite_updates(self):
        for sprite in self.npces.sprites():
            if sprite.name == 'librarian':
                if sprite.purchase_done:
                    sprite.update_player_characteristics(self.player_sprite)
                    sprite.purchase_done = False

    def run(self):
        bgMapPreparation.update((self.world_shift_x, self.world_shift_y))
        self.decoration.update((self.world_shift_x, self.world_shift_y))
        self.decoration.draw(self.display_surface)

        self.tiles.update((self.world_shift_x, self.world_shift_y))
        self.tiles.draw(self.display_surface)

        self.potions.update((self.world_shift_x, self.world_shift_y))
        self.potions.draw(self.display_surface)

        self.portals.update((self.world_shift_x, self.world_shift_y))
        self.portals.draw(self.display_surface)

        self.npces.update((self.world_shift_x, self.world_shift_y))
        self.npces.draw(self.display_surface)

        self.chests.update((self.world_shift_x, self.world_shift_y))
        self.chests.draw(self.display_surface)

        self.scroll_x()

        self.npc_collisions()
        self.check_inventory()
        self.interface.check_item_choice()
        self.interface.draw_inventory()
        self.player.update()
        self.player_pos_checker()
        self.check_portals()
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)
        self.print_current_gold()
        self.check_potions_taken()
        self.add_keys_to_inv()
        self.check_chest()
        self.check_sprite_updates()

        for enemy in self.enemies.sprites():
            enemy.bullets.update((self.world_shift_x, self.world_shift_y))
            enemy.bullets.draw(self.display_surface)
            self.bullets_settings()

        if self.player_sprite.name == 'Hero1':
            self.player_sprite.bullets.update((self.world_shift_x, self.world_shift_y))
            self.player_sprite.bullets.draw(self.display_surface)
            self.player_sprite.attacksE.update((self.world_shift_x, self.world_shift_y))
            self.player_sprite.attacksE.draw(self.display_surface)
            self.ESettings()
            self.bullets_settings()
            self.interface.draw_attacks_timers(self.player_sprite.shoot_bool, self.player_sprite.shoot_bool_max,
                                               self.player_sprite.attacksEBool, self.player_sprite.attacksEBool_max,
                                               self.player_sprite.Q_SLEEPER, self.player_sprite.Q_SLEEPER_MAX)
        elif self.player_sprite.name == 'Hero3':
            self.interface.draw_attacks_timers(self.player_sprite.AA_TIMER, self.player_sprite.AA_TIMER_MAX,
                                               self.player_sprite.E_TIMER, self.player_sprite.E_TIMER_MAX,
                                               self.player_sprite.Q_ACTIVE_TIMER, self.player_sprite.Q_ACTIVE_TIMER_MAX)

        self.interface.draw(self.player_sprite.hp, self.player_sprite.maxHp, self.player_sprite.power)
        self.interface.draw_lvl_progress_time(self.sleeper_time)
