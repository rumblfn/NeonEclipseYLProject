import pygame


class ElectorWindow:
    def __init__(self, sc, font, obj, w, h):
        self.w = w
        self.h = h
        self.X_LEFT_TOP = round(0.066 * w)
        self.Y_LEFT_TOP = round((86 / 750) * h)
        self.X_RIGHT_BOT = round(0.498 * w)
        self.Y_RIGHT_BOT = round((289 / 750) * h)
        self.WIDGET_HEIGHT = round((203 / 750) * h)
        self.WIDGET_WIDTH = round(0.432 * w)

        self.ARROW_HEIGHT = round((140 / 864) * h)
        self.ARROW_WIDTH = round((90 / 1536) * w)
        self.IMAGE_BLOCK_HEIGHT = round((140 / 864) * h)
        self.IMAGE_BLOCK_WIDTH1 = round((140 / 1536) * w)
        self.IMAGE_BLOCK_WIDTH2 = round((50 / 1536) * w)
        self.BORDER_WIDTH = 4

        self.ARROW_LEFT_X1 = round((self.WIDGET_WIDTH / 10) + self.X_LEFT_TOP)
        self.ARROW_LEFT_Y1 = round((self.WIDGET_HEIGHT / 2 - self.ARROW_HEIGHT / 2) + self.Y_LEFT_TOP)

        self.ARROW_RIGHT_X1 = round(self.WIDGET_WIDTH - (self.ARROW_LEFT_X1 - self.X_LEFT_TOP))
        self.ARROW_RIGHT_Y1 = round(self.WIDGET_HEIGHT / 2 - self.ARROW_HEIGHT / 2 + self.Y_LEFT_TOP)

        self.IMAGE_BLOCK_X1 = round(self.WIDGET_WIDTH / 2 - self.IMAGE_BLOCK_WIDTH1 / 2 + self.X_LEFT_TOP)
        self.IMAGE_BLOCK_Y1 = round(self.WIDGET_HEIGHT / 2 - self.IMAGE_BLOCK_HEIGHT / 2 + self.Y_LEFT_TOP)

        self.heroes = obj.heroes
        self.heroes = self.heroes[1:] + [self.heroes[0]]
        self.borderColor = (64, 128, 255)
        self.borderColor2 = (8, 16, 32)
        self.textAndBlockColor = (213, 255, 158)
        self.blockWidth = obj.blockWidth
        self.blockHeight = obj.blockHeight
        self.screen = sc
        self.titleSurface = font.render('Choose your hero', True, self.textAndBlockColor)

    def draw_widget(self):
        self.w = pygame.display.Info().current_w
        self.h = pygame.display.Info().current_h
        mx, my = pygame.mouse.get_pos()
        rectHoverRect = pygame.Rect(self.X_LEFT_TOP + 2, self.Y_LEFT_TOP + 2, self.WIDGET_WIDTH - 4,
                                    self.WIDGET_HEIGHT - 4)

        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)
        # if rectHoverRect.collidepoint((mx, my)):
        #     pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)

        pygame.draw.rect(self.screen, self.borderColor,
                         (self.X_LEFT_TOP, self.Y_LEFT_TOP, self.WIDGET_WIDTH, self.WIDGET_HEIGHT), self.BORDER_WIDTH,
                         10)
        self.screen.blit(self.titleSurface, (self.X_LEFT_TOP + 15, self.Y_LEFT_TOP + 10))
        self.draw_arrows()
        self.draw_image_block(self.heroes[-1]['imagePreviewBig'])

    def draw_arrows(self):
        arr_left = pygame.Surface((self.ARROW_WIDTH, self.ARROW_HEIGHT))
        img_l = pygame.transform.scale(pygame.image.load('static/leftArrow.png'),
                                       (self.ARROW_WIDTH, self.ARROW_HEIGHT))
        arr_left.blit(img_l, (0, 0))
        self.btl = pygame.draw.rect(self.screen, self.borderColor,
                                    (self.ARROW_LEFT_X1, self.ARROW_LEFT_Y1,
                                     self.ARROW_WIDTH, self.ARROW_HEIGHT))
        self.screen.blit(arr_left, (self.ARROW_LEFT_X1, self.ARROW_LEFT_Y1))

        arr_right = pygame.Surface((self.ARROW_WIDTH, self.ARROW_HEIGHT), 1)
        img_r = pygame.transform.scale(pygame.image.load('static/rightArrow.png'),
                                       (self.ARROW_WIDTH, self.ARROW_HEIGHT))
        arr_right.blit(img_r, (0, 0))
        self.btr = pygame.draw.rect(self.screen, self.borderColor,
                                    (self.ARROW_RIGHT_X1, self.ARROW_RIGHT_Y1,
                                     self.ARROW_WIDTH, self.ARROW_HEIGHT))
        self.screen.blit(arr_right, (self.ARROW_RIGHT_X1, self.ARROW_RIGHT_Y1))

    def draw_image_block(self, src):
        if self.heroes[-1]['name'] == 'Hero1':
            width = self.IMAGE_BLOCK_WIDTH1
            width_help = 0
        if self.heroes[-1]['name'] == 'Hero3':
            width = self.IMAGE_BLOCK_WIDTH2
            width_help = self.IMAGE_BLOCK_WIDTH1 // 2 - width // 2
        img = pygame.transform.scale(src,
                                       (width - self.BORDER_WIDTH, self.IMAGE_BLOCK_HEIGHT - self.BORDER_WIDTH))
        pygame.draw.rect(self.screen, self.borderColor,
                         (self.IMAGE_BLOCK_X1, self.IMAGE_BLOCK_Y1, self.IMAGE_BLOCK_WIDTH1, self.IMAGE_BLOCK_HEIGHT),
                         self.BORDER_WIDTH)
        self.screen.blit(img,
                         (self.IMAGE_BLOCK_X1 + self.BORDER_WIDTH / 2 + width_help, self.IMAGE_BLOCK_Y1 + self.BORDER_WIDTH / 2))

    def change_image(self, arg):
        if arg[0] == 'mouse':
            mx, my = pygame.mouse.get_pos()
            if self.btl.collidepoint((mx, my)):
                if pygame.mouse.get_pressed():
                    self.change_to_left()
            elif self.btr.collidepoint((mx, my)):
                if pygame.mouse.get_pressed():
                    self.change_to_right()
        else:
            if arg[-1].key == pygame.K_LEFT:
                self.change_to_left()
            if arg[-1].key == pygame.K_RIGHT:
                self.change_to_right()

    def change_to_left(self):
        self.heroes[-1]['selected'] = False
        self.heroes = [self.heroes[-1]] + self.heroes[:-1]
        self.heroes[-1]['selected'] = True
        self.draw_image_block(self.heroes[-1]['imagePreviewBig'])

    def change_to_right(self):
        self.heroes[-1]['selected'] = False
        self.heroes = self.heroes[1:] + [self.heroes[0]]
        self.heroes[-1]['selected'] = True
        self.draw_image_block(self.heroes[-1]['imagePreviewBig'])
