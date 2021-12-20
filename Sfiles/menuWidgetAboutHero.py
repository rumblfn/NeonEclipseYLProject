import pygame


class AboutHeroWindow:
    def __init__(self, sc, font, obj, w, h):
        self.X_LEFT_TOP = round(0.066 * w)
        self.Y_LEFT_TOP = round((339 / 750) * h)
        self.X_RIGHT_BOT = round(0.366 * w)
        self.Y_RIGHT_BOT = round((703 / 750) * h)
        self.WIDGET_HEIGHT = round((364 / 750) * h)
        self.WIDGET_WIDTH = round(0.300 * w)
        self.width = w
        self.height = h

        self.BORDER_WIDTH = 4

        self.heroes = obj.heroes
        self.borderColor = (64, 128, 255)
        self.borderColor2 = (8, 16, 32)
        self.textAndBlockColor = (213, 255, 158)
        self.blockWidth = obj.blockWidth
        self.blockHeight = obj.blockHeight
        self.screen = sc
        self.font = font

    def draw_widget(self):
        mx, my = pygame.mouse.get_pos()
        rectHoverRect = pygame.Rect(self.X_LEFT_TOP + 2, self.Y_LEFT_TOP + 2, self.WIDGET_WIDTH - 4, self.WIDGET_HEIGHT - 4)

        # if rectHoverRect.collidepoint((mx, my)):
        #     pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)
        pygame.draw.rect(self.screen, self.borderColor2, rectHoverRect)

        pygame.draw.rect(self.screen, self.borderColor,
                         (self.X_LEFT_TOP, self.Y_LEFT_TOP, self.WIDGET_WIDTH, self.WIDGET_HEIGHT), self.BORDER_WIDTH, 10)
        self.choose_hero()

    def choose_hero(self):
        for hero in self.heroes:
            if not hero['selected']:
                pass
            else:
                self.draw_desc(hero)

    def draw_desc(self, hero):
        titleSurface = self.font.render(hero['name'], True, self.textAndBlockColor)
        self.screen.blit(titleSurface, (self.X_LEFT_TOP + 15, self.Y_LEFT_TOP + 10))
        info = {
            hero['attack power']: 'static/attackIconMenu.png',
            hero['maxHp']: 'static/healthIconMenu.png',
            hero['attackQ']: 'static/buttonQ.png',
            hero['attackE']: 'static/buttonE.png',
            hero['simpleAttack']: 'static/lmbIconMenu.png'
        }
        for i, el in enumerate(list(info.items())):
            surf = pygame.Surface((50, 50))
            surf.blit(pygame.image.load(el[1]), (0, 0))
            self.screen.blit(surf, ((self.X_LEFT_TOP + 30), (self.Y_LEFT_TOP + 60 * self.width // 1536) + 20 * i + 50 * i * self.width // 1536))

            textSurface = self.font.render(str(el[0]), True, self.textAndBlockColor)
            self.screen.blit(textSurface, (self.X_LEFT_TOP + 100, (self.Y_LEFT_TOP + 76 * self.width // 1536) + 20 * i + 50 * i * self.width // 1536))




