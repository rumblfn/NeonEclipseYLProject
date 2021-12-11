import pygame
from menuWidgetAllHeroes import AllHeroesWindow
from menuWidgetAboutGame import AboutGameWindow
from menuWidgetElector import ElectorWindow
from menuWidgetAboutHero import AboutHeroWindow
from menuWidgetSetScreen import ScreenSizeWindow

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Neon eclipse")
pygame.font.init()
font = pygame.font.SysFont('Avenir Next', 26)
fontTitle = pygame.font.SysFont('SFCompactItalic', 36)
pygame.mouse.set_visible(False)
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
WI, HE = WIDTH, HEIGHT
clock = pygame.time.Clock()

# imageButtonStartHost = pygame.image.load('static/startHost.png')
# imageButtonJoinHost = pygame.image.load('static/JoinHostt.png')
imageButtonStartGame = pygame.image.load('static/StartGame.png')
buttonStartGameWidth = imageButtonStartGame.get_width()
buttonStartGameHeight = imageButtonStartGame.get_height()

background_map_preparation = pygame.image.load('static/Bg-straight-echo.png')

imageCursorNormal = pygame.image.load('static/Cursor_normal.png')
imageCursorClicked = pygame.image.load('static/Cursor_Clicked.png')

player1Preview = pygame.image.load('static/charackter64x64Preview.png')
player1BigGif = pygame.image.load('static/charackter136x136Bigt.gif')
player2Paladin = pygame.image.load('static/paladin27x78.png')
player2PaladinBig = pygame.image.load('static/paladin27x78Big1.png')
player3Sniper = pygame.image.load('static/sniper37x75.png')
player3SniperBig = pygame.image.load('static/sniper136Big.png')


HEROES = [
    {'name': 'Hero1',
     'attack power': 10,
     'maxHp': 100,
     'imagePreview': player1Preview,
     'imagePreviewBig': player1BigGif,
     'selected': True,
     'attackE': 'attackE - 1',
     'attackQ': 'attackQ - 1',
     'width': 64,
     'height': 64,
     'simpleAttack': 'attackLBM - 1'},
    {'name': 'Hero2',
     'attack power': 20,
     'maxHp': 70,
     'imagePreview': player3Sniper,
     'imagePreviewBig': player3SniperBig,
     'selected': False,
     'attackE': 'attackE - 2',
     'attackQ': 'attackQ - 2',
     'simpleAttack': 'attackLBM - 2',
     'width': 64,
     'height': 64},
    {'name': 'Hero3',
     'attack power': 5,
     'maxHp': 200,
     'imagePreview': player2Paladin,
     'imagePreviewBig': player2PaladinBig,
     'selected': False,
     'attackE': 'attackE - 3',
     'attackQ': 'attackQ - 3',
     'width': 27,
     'height': 78,
     'simpleAttack': 'attackLBM - 3'}
]


surfTitle = fontTitle.render('Neon Eclipse', False, (255, 183, 0))
objAllHeroesWidget = {'x1': round(0.545 * WIDTH), 'y1': round((87 / 750) * HEIGHT),
                          'x2': round(0.961 * WIDTH), 'y2': round((289 / 750) * HEIGHT),
                          'width': round(0.416 * WIDTH), 'height': round((202 / 750) * HEIGHT),
                          'titleText': 'All heroes', 'heroes': HEROES,
                          'blockWidth': 72, 'blockHeight': 72}
objAboutGame = {
        'x1': WIDTH / 2 - buttonStartGameWidth / 2, 'y1': round((470 / 750) * HEIGHT),
        'x2': round(0.961 * WIDTH), 'y2': round((700 / 750) * HEIGHT),
        'titleText': 'About game'
    }
menuWidgetAllHeroes = AllHeroesWindow(screen, font, objAllHeroesWidget)
menuWidgetAboutGame = AboutGameWindow(screen, font, objAboutGame)
menuWidgetElector = ElectorWindow(screen, font, menuWidgetAllHeroes, WIDTH, HEIGHT)
menuWidgetAboutHero = AboutHeroWindow(screen, font, menuWidgetElector, WIDTH, HEIGHT)
menuWidgetScreenSize = ScreenSizeWindow(screen, font, WIDTH, HEIGHT)
