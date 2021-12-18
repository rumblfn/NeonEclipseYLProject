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
pipe_vertical = pygame.transform.scale(pygame.image.load('static/vertical_pipe.png'), (res, round(res * 1.5)))
pipe_horizontal = pygame.transform.scale(pygame.image.load('static/pipe.png'), (round(res * 1.5), res))
blockLeft = pygame.transform.scale(pygame.image.load('static/blockLeft.png'), (res, res))
blockTop = pygame.transform.scale(pygame.image.load('static/blockTop.png'), (res, res))
blockRight = pygame.transform.scale(pygame.image.load('static/blockRight.png'), (res, res))
blockBottom = pygame.transform.scale(pygame.image.load('static/blockBottom.png'), (res, res))
blockLeftTop = pygame.transform.scale(pygame.image.load('static/blockLeftRight.png'), (res, res))
blockTopRight = pygame.transform.scale(pygame.image.load('static/blockTopRight.png'), (res, res))
blockRightBottom = pygame.transform.scale(pygame.image.load('static/blockRightBottom.png'), (res, res))
blockBottomLeft = pygame.transform.scale(pygame.image.load('static/blockLeftBottom.png'), (res, res))
block = pygame.transform.scale(pygame.image.load('static/block.png'), (res, res))
block2 = pygame.transform.scale(pygame.image.load('static/block2.png'), (res, res))
windowBlock1 = pygame.transform.scale(pygame.image.load('static/WindowBlock.png'), (res, res))
windowBlock2 = pygame.transform.scale(pygame.image.load('static/WindowBlock2.png'), (res, res))
windowBlock3 = pygame.transform.scale(pygame.image.load('static/WindowBlock3.png'), (res, res))
windowBlock4 = pygame.transform.scale(pygame.image.load('static/WindowBlock4.png'), (res, res))
windowBlock5 = pygame.transform.scale(pygame.image.load('static/WindowBlock5.png'), (res, res))
windowBlock6 = pygame.transform.scale(pygame.image.load('static/WindowBlock6.png'), (res, res))
windowBlock7 = pygame.transform.scale(pygame.image.load('static/window_transparent.png').convert_alpha(), (res, res))
blockTopBottom = pygame.transform.scale(pygame.image.load('static/blockBottomTop.png'), (res, res))
blockTopLeftBottom = pygame.transform.scale(pygame.image.load('static/blockBottomLeftTop.png'), (res, res))
blockTopRightBottom = pygame.transform.scale(pygame.image.load('static/blockBottomRightTop.png'), (res, res))
blockBorders = pygame.transform.scale(pygame.image.load('static/blockBorders.png'), (res, res))
blockLeftTopRight = pygame.transform.scale(pygame.image.load('static/blockLeftTopRight.png'), (res, res))
portalImage = pygame.transform.scale(pygame.image.load('static/portal_door_blue.png').convert_alpha(), (portal_res_x, portal_res))
platform = pygame.transform.scale(pygame.image.load('static/platform.png'), (res, res))
lst_of_windows = [windowBlock1, windowBlock2, windowBlock3, windowBlock4, windowBlock5, windowBlock6, windowBlock7, platform]
blockRightLeft = pygame.transform.scale(pygame.image.load('static/BlockRightLeft.png'), (res, res))
bgTile = pygame.transform.scale(pygame.image.load('static/bgTiles.png'), (res, res))
gold = pygame.transform.scale(pygame.image.load('static/gold.png'), (res, res))
up_arrow = pygame.transform.scale(pygame.image.load('static/up_arrow.png'), (res, res))
web = pygame.transform.scale(pygame.image.load('static/web.png'), (res, res))
red_gem = pygame.transform.scale(pygame.image.load('static/red_gem.png'), (res, res))
blue_gem = pygame.transform.scale(pygame.image.load('static/blue_gem.png'), (res, res))
green_gem = pygame.transform.scale(pygame.image.load('static/green_gem.png'), (res, res))
yellow_gem = pygame.transform.scale(pygame.image.load('static/yellow_gem.png'), (res, res))


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell, map, player_col):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.set_image(pos, cell, size, map, player_col)
        # self.image.fill((10, 17, 25))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))
        self.cell = cell
        self.size = size

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
            self.image.blit(lst_of_windows[random.randint(0, len(lst_of_windows)) - 1], (0, 0))
        elif cell == 'bg':
            self.image.blit(bgTile, (0, 0))
        elif cell == 'X':
            if not el_left and all([el_top, el_right, el_bottom]):
                self.image.blit(blockLeft, (0, 0))
            elif not el_left and not el_right and all([el_top, el_bottom]):
                self.image.blit(blockRightLeft, (0, 0))
            elif not el_top and all([el_left, el_bottom, el_right]):
                self.image.blit(blockTop, (0, 0))
            elif not el_right and all([el_top, el_bottom, el_left]):
                self.image.blit(blockRight, (0, 0))
            elif not el_bottom and all([el_left, el_top, el_right]):
                self.image.blit(blockBottom, (0, 0))
            elif el_right and el_bottom and not any([el_left, el_top]):
                self.image.blit(blockLeftTop, (0, 0))
            elif el_left and el_bottom and not any([el_top, el_right]):
                self.image.blit(blockTopRight, (0, 0))
            elif el_left and el_top and not any([el_right, el_bottom]):
                self.image.blit(blockRightBottom, (0, 0))
            elif el_top and el_right and not any([el_left, el_bottom]):
                self.image.blit(blockBottomLeft, (0, 0))
            elif el_left and el_right and not any([el_top, el_bottom]):
                self.image.blit(blockTopBottom, (0, 0))
            elif el_right and not any([el_bottom, el_left, el_top]):
                self.image.blit(blockTopLeftBottom, (0, 0))
            elif el_left and not any([el_top, el_right, el_bottom]):
                self.image.blit(blockTopRightBottom, (0, 0))
            elif not any([el_left, el_top, el_right, el_bottom]):
                self.image.blit(blockBorders, (0, 0))
            elif el_bottom and not any([el_left, el_top, el_right]):
                self.image.blit(blockLeftTopRight, (0, 0))
            elif el_top and el_left and el_bottom and el_right:
                self.image.blit(block, (0, 0))
        elif cell == 'п':  # vertical
            self.image = pygame.Surface((res, round(res * 1.5)), pygame.SRCALPHA)
            self.image.blit(pipe_vertical, (0, 0))
        elif cell == 'П':  # horizontal
            self.image = pygame.Surface((round(res * 1.5), res), pygame.SRCALPHA)
            self.image.blit(pipe_horizontal, (0, 0))

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
        self.image.blit(block2, (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class Gold(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.blit(random.choice([red_gem, blue_gem, green_gem, yellow_gem]), (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class UpArrow(pygame.sprite.Sprite):
    def __init__(self, pos, size, cell):
        super().__init__()
        self.cell = cell
        if cell == 'a':
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.fill((255, 255, 255, 0))
            self.able = False
        else:
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
            self.image.blit(up_arrow, (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]


class Web(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.blit(web, (0, 0))
        self.rect = self.image.get_rect(topleft=(pos[0] * size, pos[1] * size))

    def update(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]