import sys
from pygame.locals import *
from dataConsts import *
from network import Network
from time import sleep
from _thread import start_new_thread
from map_preparation_settings import *
from tiles import Tile
from level import Level
from map_preparation_settings import *


def draw_cursor(sc):
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        sc.blit(imageCursorClicked, (mx - 2, my - 2))
    else:
        sc.blit(imageCursorNormal, (mx, my))


def sleeper():
    global sleeper_status
    sleeper_status = False
    sleep(300)
    sleeper_status = True


def draw_button(sc, image, pos_y_diff, player, network):
    surf = pygame.Surface((buttonStartGameWidth, buttonStartGameHeight))
    surf.blit(image, (0, 0))
    x_lef_top = WIDTH / 2 - buttonStartGameWidth / 2
    y_left_top = HEIGHT / 2 - buttonStartGameHeight / 2 - pos_y_diff
    button = pygame.Rect(x_lef_top, y_left_top, buttonStartGameWidth, buttonStartGameHeight)
    mx, my = pygame.mouse.get_pos()
    if button.collidepoint((mx, my)):
        if pygame.mouse.get_pressed()[0]:
            for hero in menuWidgetAllHeroes.heroes:
                if hero['selected']:
                    print(hero)
                    player.name = hero['name']
                    player.attack_power = hero['attack power']
                    player.maxHp = hero['maxHp']
                    # player.image = hero['imagePreview']
                    player.width = hero['width']
                    player.height = hero['height']
                    player.ready = True
                    waitingForConnection(hero, player, network)
    sc.blit(surf, (x_lef_top, y_left_top))


def main_game(player, network):
    run = True
    while run:
        player.move()
        player2 = network.send(player)
        redrawWindow(screen, player, player2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.ready = False
                network.send(player)
                pygame.quit()
                sys.exit()
        clock.tick(60)


def map_preparation(player, network):
    run = True
    player.x = WIDTH // 4
    player.y = round(HEIGHT * (2 / 3))
    player.vel = 8

    level = Level(level1_map, screen)
    start_new_thread(sleeper, ())
    while run:
        # screen.fill((245, 238, 230))
        screen.fill((10, 17, 25))
        screen.blit(background_map_preparation, (0, 0))
        # player.move()
        level.run()
        # player.draw(screen)
        draw_cursor(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.ready = False
                network.send(player)
                pygame.quit()
                sys.exit()
        if sleeper_status:
            main_game(player, network)
        clock.tick(60)


def f(w, h):
    global objAllHeroesWidget, \
        objAboutGame, \
        menuWidgetAllHeroes, \
        menuWidgetAboutGame, \
        menuWidgetElector, \
        menuWidgetAboutHero, \
        menuWidgetScreenSize, \
        WIDTH, HEIGHT
    objAllHeroesWidget = {'x1': round(0.545 * w), 'y1': round((87 / 750) * h),
                          'x2': round(0.961 * w), 'y2': round((289 / 750) * h),
                          'width': round(0.416 * w), 'height': round((202 / 750) * h),
                          'titleText': 'All heroes', 'heroes': HEROES,
                          'blockWidth': 72, 'blockHeight': 72}
    objAboutGame = {
        'x1': w / 2 - buttonStartGameWidth / 2, 'y1': round((470 / 750) * h),
        'x2': round(0.961 * w), 'y2': round((700 / 750) * h),
        'titleText': 'About game'
    }
    menuWidgetAllHeroes = AllHeroesWindow(screen, font, objAllHeroesWidget)
    menuWidgetAboutGame = AboutGameWindow(screen, font, objAboutGame)
    menuWidgetElector = ElectorWindow(screen, font, menuWidgetAllHeroes, w, h)
    menuWidgetAboutHero = AboutHeroWindow(screen, font, menuWidgetElector, w, h)
    menuWidgetScreenSize = ScreenSizeWindow(screen, font, w, h)
    WIDTH, HEIGHT = w, h


def main_menu():
    run = True
    network = Network()
    player = network.getP()
    player.ready = False
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    while run:
        screen.fill((0, 0, 0))
        draw_button(screen, imageButtonStartGame, 0, player, network)
        screen.blit(surfTitle, (50, 35))
        menuWidgetAllHeroes.draw_widget()
        menuWidgetAboutGame.draw_widget()
        menuWidgetElector.draw_widget()
        menuWidgetAboutHero.draw_widget()
        menuWidgetScreenSize.draw_widget()
        draw_cursor(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                menuWidgetElector.change_image(('key', event))
                if event.key == K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menuWidgetElector.change_image(('mouse', event))
                menuWidgetScreenSize.change_size()

        w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
        if w != WIDTH or h != HEIGHT:
            if w == h == 1000:
                w, h = WI, HE
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            f(w, h)
        clock.tick(60)


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def waitingForConnection(character, player, network):
    run = True
    waitingText = font.render('Waiting for a connection', False, (0, 255, 0))
    top_menu_text_pos_x = 10

    while run:
        player2 = network.send(player)
        screen.fill((0, 0, 0))
        screen.blit(waitingText, (top_menu_text_pos_x, top_menu_text_pos_x))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.ready = False
                network.send(player)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    player.ready = False
                    network.send(player)
                    run = False
        if player2.ready:
            map_preparation(player, network)
        clock.tick(60)


if __name__ == '__main__':
    main_menu()
