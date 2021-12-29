import pygame
import random
from map_parkour_settings import level_parkour_map

# block1 = pygame.image.load('static/Bg.png')
# block2 = pygame.image.load('static/Bg1.png')
# block3 = pygame.image.load('static/Bg1-1.png')
h = pygame.display.Info().current_h
res = h // len(level_parkour_map)
portal_res = round((82 / 900) * h)
portal_res_x = round((32 / 900) * h)

blockLeft = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockLeft.png'), (res, res))
blockTop = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockTop.png'), (res, res))
blockRight = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockRight.png'), (res, res))
blockBottom = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockBottom.png'), (res, res))
blockLeftTop = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockLeftRight.png'),
                                          (res, res))
blockTopRight = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockTopRight.png'),
                                           (res, res))
blockRightBottom = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockRightBottom.png'),
                                              (res, res))
blockBottomLeft = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockLeftBottom.png'),
                                             (res, res))
blockTopBottom = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockBottomTop.png'),
                                            (res, res))
blockTopLeftBottom = pygame.transform.scale(
        pygame.image.load('static/map_preparation_blocks/blockBottomLeftTop.png'), (res, res))
blockTopRightBottom = pygame.transform.scale(
        pygame.image.load('static/map_preparation_blocks/blockBottomRightTop.png'), (res, res))
blockBorders = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockBorders.png'),
                                          (res, res))
blockLeftTopRight = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/blockLeftTopRight.png'),
                                               (res, res))
blockRightLeft = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/BlockRightLeft.png'),
                                            (res, res))
blockLeftBottomRight = pygame.transform.scale(
        pygame.image.load('static/map_preparation_blocks/blockLeftBottomRightt.png'), (res, res))
block = pygame.transform.scale(pygame.image.load('static/map_preparation_blocks/block.png'), (res, res))

blockLeft_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockLeft.png'), (res, res))
blockTop_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockTop.png'), (res, res))
blockRight_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockRight.png'), (res, res))
blockBottom_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockBottom.png'), (res, res))
blockLeftTop_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockLeftRight.png'),
                                          (res, res))
blockTopRight_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockTopRight.png'),
                                           (res, res))
blockRightBottom_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockRightBottom.png'),
                                              (res, res))
blockBottomLeft_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockLeftBottom.png'),
                                             (res, res))
blockTopBottom_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockBottomTop.png'),
                                            (res, res))
blockTopLeftBottom_main = pygame.transform.scale(
        pygame.image.load('static/main_game_blocks/blockBottomLeftTop.png'), (res, res))
blockTopRightBottom_main = pygame.transform.scale(
        pygame.image.load('static/main_game_blocks/blockBottomRightTop.png'), (res, res))
blockBorders_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockBorders.png'),
                                          (res, res))
blockLeftTopRight_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/blockLeftTopRight.png'),
                                               (res, res))
blockRightLeft_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/BlockRightLeft.png'),
                                            (res, res))
blockLeftBottomRight_main = pygame.transform.scale(
        pygame.image.load('static/main_game_blocks/blockLeftBottomRightt.png'), (res, res))
block_main = pygame.transform.scale(pygame.image.load('static/main_game_blocks/block.png'), (res, res))
block2 = pygame.transform.scale(pygame.image.load('static/block2.png'), (res, res))
windowBlock1 = pygame.transform.scale(pygame.image.load('static/WindowBlock.png'), (res, res))
windowBlock2 = pygame.transform.scale(pygame.image.load('static/WindowBlock2.png'), (res, res))
windowBlock3 = pygame.transform.scale(pygame.image.load('static/WindowBlock3.png'), (res, res))
windowBlock4 = pygame.transform.scale(pygame.image.load('static/WindowBlock4.png'), (res, res))
windowBlock5 = pygame.transform.scale(pygame.image.load('static/WindowBlock5.png'), (res, res))
windowBlock6 = pygame.transform.scale(pygame.image.load('static/WindowBlock6.png'), (res, res))
windowBlock7 = pygame.transform.scale(pygame.image.load('static/window_transparent.png').convert_alpha(), (res, res))
portalImage = pygame.transform.scale(pygame.image.load('static/portal_door_blue.png').convert_alpha(), (portal_res_x, portal_res))
platform = pygame.transform.scale(pygame.image.load('static/platform.png'), (res, res))
lst_of_windows = [windowBlock1, windowBlock2, windowBlock3, windowBlock4, windowBlock5, windowBlock6, windowBlock7, platform]
bgTile = pygame.transform.scale(pygame.image.load('static/bgTiles.png'), (res, res))
gold = pygame.transform.scale(pygame.image.load('static/gold.png'), (res, res))
up_arrow = pygame.transform.scale(pygame.image.load('static/up_arrow.png'), (res, res))
web = pygame.transform.scale(pygame.image.load('static/web.png'), (res, res))
red_gem = pygame.transform.scale(pygame.image.load('static/red_gem.png'), (res, res))
blue_gem = pygame.transform.scale(pygame.image.load('static/blue_gem.png'), (res, res))
green_gem = pygame.transform.scale(pygame.image.load('static/green_gem.png'), (res, res))
yellow_gem = pygame.transform.scale(pygame.image.load('static/yellow_gem.png'), (res, res))
bird = pygame.transform.scale(pygame.image.load('static/bird.png'), (res, res))

open_door_red = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_red.png'), (res, res))
open_door_green = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_green.png'), (res, res))
open_door_yellow = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_yellow.png'), (res, res))
open_door_blue = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_blue.png'), (res, res))
open_door_black = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_black.png'), (res, res))
open_door_white = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_white.png'), (res, res))
open_door_violet = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_violet.png'), (res, res))
open_door_orange = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_orange.png'), (res, res))
open_door_pink = pygame.transform.scale(pygame.image.load('static/keys_doors/door_open_pink.png'), (res, res))

close_door_red = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_red.png'), (res, res))
close_door_green = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_green.png'), (res, res))
close_door_yellow = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_yellow.png'), (res, res))
close_door_blue = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_blue.png'), (res, res))
close_door_black = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_black.png'), (res, res))
close_door_white = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_white.png'), (res, res))
close_door_violet = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_violet.png'), (res, res))
close_door_orange = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_orange.png'), (res, res))
close_door_pink = pygame.transform.scale(pygame.image.load('static/keys_doors/door_close_pink.png'), (res, res))

key_red = pygame.transform.scale(pygame.image.load('static/keys_doors/key_red.png'), (res, res))
key_green = pygame.transform.scale(pygame.image.load('static/keys_doors/key_green.png'), (res, res))
key_yellow = pygame.transform.scale(pygame.image.load('static/keys_doors/key_yellow.png'), (res, res))
key_blue = pygame.transform.scale(pygame.image.load('static/keys_doors/key_blue.png'), (res, res))
key_black = pygame.transform.scale(pygame.image.load('static/keys_doors/key_black.png'), (res, res))
key_white = pygame.transform.scale(pygame.image.load('static/keys_doors/key_white.png'), (res, res))
key_violet = pygame.transform.scale(pygame.image.load('static/keys_doors/key_violet.png'), (res, res))
key_orange = pygame.transform.scale(pygame.image.load('static/keys_doors/key_orange.png'), (res, res))
key_pink = pygame.transform.scale(pygame.image.load('static/keys_doors/key_pink.png'), (res, res))


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell, map, player_col):
        super().__init__()
        self.new_tile_size = size
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.set_image(pos, cell, size, map, player_col)
        # self.image.fill((10, 17, 25))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        self.cell = cell

    def set_image(self, pos, cell, s, lvl_map, player_col):
        el_top, el_right, el_bottom, el_left = False, False, False, False
        try:
            el_top = True if lvl_map[pos[1] - 1][pos[0] + player_col] == 'X' else False
        except:
            pass
        try:
            el_right = True if lvl_map[pos[1]][pos[0] + player_col + 1] == 'X' else False
        except:
            pass
        try:
            el_left = True if lvl_map[pos[1]][pos[0] + player_col - 1] == 'X' else False
        except:
            pass
        try:
            el_bottom = True if lvl_map[pos[1] + 1][pos[0] + player_col] == 'X' else False
        except:
            pass
        if cell == '0':
            self.draw_block(lst_of_windows[random.randint(0, len(lst_of_windows)) - 1])
        elif cell == 'bg':
            self.draw_block(bgTile)
        elif cell == 'X':
            if not el_left and all([el_top, el_right, el_bottom]):
                self.draw_block(blockLeft)
            elif not el_left and not el_right and all([el_top, el_bottom]):
                self.draw_block(blockRightLeft)
            elif not el_top and all([el_left, el_bottom, el_right]):
                self.draw_block(blockTop)
            elif not el_right and all([el_top, el_bottom, el_left]):
                self.draw_block(blockRight)
            elif not el_bottom and all([el_left, el_top, el_right]):
                self.draw_block(blockBottom)
            elif el_right and el_bottom and not any([el_left, el_top]):
                self.draw_block(blockLeftTop)
            elif el_left and el_bottom and not any([el_top, el_right]):
                self.draw_block(blockTopRight)
            elif el_left and el_top and not any([el_right, el_bottom]):
                self.draw_block(blockRightBottom)
            elif el_top and el_right and not any([el_left, el_bottom]):
                self.draw_block(blockBottomLeft)
            elif el_left and el_right and not any([el_top, el_bottom]):
                self.draw_block(blockTopBottom)
            elif el_right and not any([el_bottom, el_left, el_top]):
                self.draw_block(blockTopLeftBottom)
            elif el_left and not any([el_top, el_right, el_bottom]):
                self.draw_block(blockTopRightBottom)
            elif not any([el_left, el_top, el_right, el_bottom]):
                self.draw_block(blockBorders)
            elif el_bottom and not any([el_left, el_top, el_right]):
                self.draw_block(blockLeftTopRight)
            elif el_top and el_left and el_bottom and el_right:
                self.draw_block(block)
            elif el_top and not el_left and not el_right and not el_bottom:
                self.draw_block(blockLeftBottomRight)
        elif cell == '#':
            if not el_left and all([el_top, el_right, el_bottom]):
                self.draw_block(blockLeft_main)
            elif not el_left and not el_right and all([el_top, el_bottom]):
                self.draw_block(blockRightLeft_main)
            elif not el_top and all([el_left, el_bottom, el_right]):
                self.draw_block(blockTop_main)
            elif not el_right and all([el_top, el_bottom, el_left]):
                self.draw_block(blockRight_main)
            elif not el_bottom and all([el_left, el_top, el_right]):
                self.draw_block(blockBottom_main)
            elif el_right and el_bottom and not any([el_left, el_top]):
                self.draw_block(blockLeftTop_main)
            elif el_left and el_bottom and not any([el_top, el_right]):
                self.draw_block(blockTopRight_main)
            elif el_left and el_top and not any([el_right, el_bottom]):
                self.draw_block(blockRightBottom_main)
            elif el_top and el_right and not any([el_left, el_bottom]):
                self.draw_block(blockBottomLeft_main)
            elif el_left and el_right and not any([el_top, el_bottom]):
                self.draw_block(blockTopBottom_main)
            elif el_right and not any([el_bottom, el_left, el_top]):
                self.draw_block(blockTopLeftBottom_main)
            elif el_left and not any([el_top, el_right, el_bottom]):
                self.draw_block(blockTopRightBottom_main)
            elif el_bottom and not any([el_left, el_top, el_right]):
                self.draw_block(blockLeftTopRight_main)
            elif el_top and el_left and el_bottom and el_right:
                self.draw_block(block_main)
            elif el_top and not el_left and not el_right and not el_bottom:
                self.draw_block(blockLeftBottomRight_main)
            elif not any([el_left, el_top, el_right, el_bottom]):
                self.draw_block(blockBorders_main)

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((portal_res_x, portal_res), pygame.SRCALPHA)
        self.image.blit(portalImage, (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0] + 5, pos[1] - 38))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class MovingTile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.new_tile_size = size
        self.draw_block(block2)
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Gold(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.cell = cell
        self.new_tile_size = size
        if cell == 'g':
            self.image.fill((255, 255, 255, 0))
        else:
            self.draw_block(random.choice([red_gem, blue_gem, green_gem, yellow_gem]))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def update_bird_gems(self, arg):
        if arg:
            self.draw_block(random.choice([red_gem, blue_gem, green_gem, yellow_gem]))
        else:
            self.image.fill((255, 255, 255, 0))

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class UpArrow(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.new_tile_size = size
        self.cell = cell
        if cell == 'a':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 255, 255, 0))
            self.able = False
        else:
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(up_arrow)
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Web(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.new_tile_size = size
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.draw_block(web)
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Bridge(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        self.new_tile_size = size
        if cell == 'B':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(gold)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        else:
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 255, 255, 0))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def update_vision(self, arg):
        if arg:
            self.image.blit(block2, (0, 0))
        else:
            self.image.fill((255, 255, 255, 0))

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        self.new_tile_size = size
        if cell == 'R':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(bird)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        elif cell == 'D':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 0, 0, 0))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        elif cell == 'd':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((0, 255, 0, 0))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def update_vision(self, arg):
        if arg:
            self.draw_block(block2)
        else:
            self.image.fill((255, 255, 255, 0))

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class KeysAndDoors(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        self.size = size
        self.new_tile_size = size
        if cell == 'й':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_pink)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'ц':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_white)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'у':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_violet)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'к':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_orange)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'е':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_blue)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'н':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_black)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'г':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_green)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'ш':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_red)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'щ':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(close_door_yellow)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Й':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_pink)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Ц':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_white)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'У':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_violet)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'К':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_orange)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Е':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_blue)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Н':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_black)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Г':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_green)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Ш':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_red)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'Щ':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.draw_block(key_yellow)
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        if cell == 'I':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((230, 230, 230))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def open(self):
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        if self.cell == 'й':
            self.draw_block(open_door_pink)
        if self.cell == 'ц':
            self.draw_block(open_door_white)
        if self.cell == 'у':
            self.draw_block(open_door_violet)
        if self.cell == 'к':
            self.draw_block(open_door_orange)
        if self.cell == 'е':
            self.draw_block(open_door_blue)
        if self.cell == 'н':
            self.draw_block(open_door_black)
        if self.cell == 'г':
            self.draw_block(open_door_green)
        if self.cell == 'ш':
            self.draw_block(open_door_red)
        if self.cell == 'щ':
            self.draw_block(open_door_yellow)

    def update_screen(self, key):
        try:
            self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            self.image = key.image
        except:
            pass

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Invisible(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        self.new_tile_size = size
        if cell == 'V':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 255, 0, 75))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        elif cell == 'Y':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 0, 255, 75))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))


class Resizer(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        self.new_tile_size = size
        if cell == 'Z':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 255, 0, 75))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        elif cell == 'C':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 0, 255, 75))
            self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))

