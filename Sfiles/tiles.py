import pygame
import random
from map_preparation_settings import level1_map

h = pygame.display.Info().current_h
res = h // len(level1_map)
portal_res = round((82 / 900) * h)
portal_res_x = round((32 / 900) * h)
pipe_vertical = pygame.transform.scale(pygame.image.load('static/vertical_pipe.png'), (res, round(res * 1.5)))
pipe_horizontal = pygame.transform.scale(pygame.image.load('static/pipe.png'), (round(res * 1.5), res))

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

windowBlock1 = pygame.transform.scale(pygame.image.load('static/WindowBlock.png'), (res, res))
windowBlock2 = pygame.transform.scale(pygame.image.load('static/WindowBlock2.png'), (res, res))
windowBlock3 = pygame.transform.scale(pygame.image.load('static/WindowBlock3.png'), (res, res))
windowBlock4 = pygame.transform.scale(pygame.image.load('static/WindowBlock4.png'), (res, res))
windowBlock5 = pygame.transform.scale(pygame.image.load('static/WindowBlock5.png'), (res, res))
windowBlock6 = pygame.transform.scale(pygame.image.load('static/WindowBlock6.png'), (res, res))
windowBlock7 = pygame.transform.scale(pygame.image.load('static/window_transparent.png').convert_alpha(),
                                          (res, res))

portalImage = pygame.transform.scale(pygame.image.load('static/portal_door_blue.png').convert_alpha(),
                                         (portal_res_x, portal_res))
lst_of_windows = [windowBlock1, windowBlock2, windowBlock3, windowBlock4, windowBlock5, windowBlock6, windowBlock7]
bgTile = pygame.transform.scale(pygame.image.load('static/bgTiles.png'), (res, res))

potion1 = pygame.transform.scale(pygame.image.load('static/potion1.png'),
                                          (res, res))
potion2 = pygame.transform.scale(pygame.image.load('static/potion2.png'),
                                          (res, res))
potion3 = pygame.transform.scale(pygame.image.load('static/potion3.png'),
                                          (res, res))

close_chest = pygame.transform.scale(pygame.image.load('static/close_chest.png'),
                                          (res, res))
open_chest = pygame.transform.scale(pygame.image.load('static/open_chest.png'),
                                          (res, res))

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell, map, player_col):
        super().__init__()
        self.new_tile_size = size
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.set_image(pos, cell, size, map, player_col)
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def set_image(self, pos, cell, s, lvl_map, player_col):
        el_top, el_right, el_bottom, el_left = False, False, False, False
        try:
            el_top = True if lvl_map[pos[1] - 1][pos[0] + player_col] == 'X' \
                             or lvl_map[pos[1] - 1][pos[0] + player_col] == '#' else False
        except:
            pass
        try:
            el_right = True if lvl_map[pos[1]][pos[0] + player_col + 1] == 'X' \
                               or lvl_map[pos[1]][pos[0] + player_col + 1] == '#' else False
        except:
            pass
        try:
            el_left = True if lvl_map[pos[1]][pos[0] + player_col - 1] == 'X' \
                              or lvl_map[pos[1]][pos[0] + player_col - 1] == '#' else False
        except:
            pass
        try:
            el_bottom = True if lvl_map[pos[1] + 1][pos[0] + player_col] == 'X' \
                                or lvl_map[pos[1] + 1][pos[0] + player_col] == '#' else False
        except:
            pass
        if cell == '0':
            self.image.blit(lst_of_windows[random.randint(0, len(lst_of_windows)) - 1], (0, 0))
        elif cell == 'bg':
            self.image.blit(bgTile, (0, 0))
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
        elif cell == 'п':  # vertical
            self.image = pygame.Surface((res, round(res * 1.5)), pygame.SRCALPHA)
            self.image.blit(pipe_vertical, (0, 0))
        elif cell == 'П':  # horizontal
            self.image = pygame.Surface((round(res * 1.5), res), pygame.SRCALPHA)
            self.image.blit(pipe_horizontal, (0, 0))

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
        self.rect = self.image.get_rect(topleft=(pos[0] - res // 2, pos[1]))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class Potion(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.cell = cell
        self.new_tile_size = size
        self.able = True
        if cell == 'V':
            self.draw_block(potion1)
            self.surf = potion1
        elif cell == 'G':
            self.draw_block(potion2)
            self.surf = potion2
        elif cell == 'Y':
            self.draw_block(potion3)
            self.surf = potion3

        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        self.all_potions = {'V': 'static/potion1.png',
                            'G': 'static/potion2.png',
                            'Y': 'static/potion3.png'}

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))

    def delete(self):
        self.image = pygame.Surface((self.new_tile_size, self.new_tile_size), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))
        self.able = False

    def recover(self):
        self.image = pygame.Surface((self.new_tile_size, self.new_tile_size), pygame.SRCALPHA)
        self.draw_block(self.surf)
        self.able = True


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.cell = cell
        self.new_tile_size = size
        self.draw_block(close_chest)
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        self.opened = False

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

    def draw_block(self, block_to_draw):
        self.image.blit(pygame.transform.scale(block_to_draw, (self.new_tile_size, self.new_tile_size)), (0, 0))

    def redraw_block(self):
        self.image = pygame.Surface((self.new_tile_size, self.new_tile_size), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(open_chest, (self.new_tile_size, self.new_tile_size)), (0, 0))