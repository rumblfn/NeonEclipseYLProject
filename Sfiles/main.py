import sys

import pygame.mixer_music
from pygame.locals import *
from dataConsts import *
from network import Network
from time import sleep
from _thread import start_new_thread
from level import Level
from level_parkour import LevelParkour
from map_preparation_settings import *
from map_parkour_settings import *


def draw_cursor(sc):
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        sc.blit(imageCursorClicked, (mx - 2, my - 2))
    else:
        sc.blit(imageCursorNormal, (mx, my))


def sleeper():
    global sleeper_status
    sleeper_status = False
    sleep(420)
    sleeper_status = True


def draw_button(sc, image, pos_y_diff, player, network):
    global play_music
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
                    player.ready = True
                    pygame.mixer.music.stop()
                    waitingForConnection(hero, player, network, hero)
    sc.blit(surf, (x_lef_top, y_left_top))


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    pygame.display.update()


def main_game(server_player, network, player_main):
    run = True
    while run:
        player2 = network.send(server_player)
        redrawWindow(screen, server_player, player2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                server_player.ready = False
                network.send(server_player)
                pygame.quit()
                sys.exit()
        clock.tick(60)


def map_preparation(player, network, player_settings):
    run = True
    player.x = WIDTH // 4
    player.y = round(HEIGHT * (2 / 3))
    player.vel = 8
    level = Level(level1_map, screen, player_settings)
    start_new_thread(sleeper, ())

    def portalParkourMap(sc, player_parkour, to_print):

        def info_text_parkour():
            text = 'Press Esc to return to the spawn point'
            newFont = pygame.font.SysFont('SFCompact', 75)
            txt_surf = newFont.render(text, False, (255, 183, 0))
            sc.blit(txt_surf, (WIDTH // 5, HEIGHT // 2 - 35))

        runParkourMap = True
        level_p = LevelParkour(level_parkour_map, screen, player_settings)
        count = 0
        while runParkourMap:
            sc.fill((255, 255, 255))
            bgMapPreparation.draw()
            level_p.run()
            count += 1
            if to_print:
                info_text_parkour()
                if count == 150:
                    to_print = False
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        portalParkourMap(sc, player_parkour, False)
                    level_p.check_fall = False
                if level_p.portalParkour:
                    map_preparation(player, network, player_settings)
            if sleeper_status:
                runParkourMap = False
            if level_p.check_fall:
                portalParkourMap(sc, player_parkour, False)
            if level_p.gold_taken:
                level_p.take_gold()
                level_p.gold_taken = False
            if level_p.arrow_works:
                level_p.raise_player()
                level_p.arrow_works = False
            if level_p.in_web:
                level_p.web_work(True)
            if not level_p.in_web:
                level_p.web_work(False)
            clock.tick(60)

    while run:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('music/preparation_map.mp3')
            pygame.mixer.music.play()
        if sleeper_status:
            pygame.mixer.music.stop()
            main_game(player, network, level.player_sprite)
        # screen.fill('#fefec2')  # '#fefec2'
        bgMapPreparation.draw()
        # player.move()
        level.run()
        # player.draw(screen)
        draw_cursor(screen)
        if pygame.mouse.get_pressed()[0]:
            if level.player.sprite.shoot_bool >= 1 and level.player.sprite.name == 'Hero1':
                level.bullets.add(level.player.sprite.create_bullet())

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.ready = False
                network.send(player)
                pygame.quit()
                sys.exit()
        if level.portalParkour:
            pygame.mixer.music.stop()
            portalParkourMap(screen, level.player, True)
        clock.tick(60)


def change_objects(w, h):
    global objAllHeroesWidget, \
        objAboutGame, \
        menuWidgetAllHeroes, \
        menuWidgetAboutGame, \
        menuWidgetElector, \
        menuWidgetAboutHero, \
        menuWidgetScreenSize, \
        menuWidgetSlider, \
        WIDTH, HEIGHT, \
        HEROES
    objAllHeroesWidget = {'x1': round(0.545 * w), 'y1': round((87 / 750) * h),
                          'x2': round(0.872 * w), 'y2': round((289 / 750) * h),
                          'width': round(0.327 * w), 'height': round((202 / 750) * h),
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
    menuWidgetAboutHero = AboutHeroWindow(screen, font, menuWidgetAllHeroes, w, h)
    menuWidgetScreenSize = ScreenSizeWindow(screen, font, w, h)
    menuWidgetSlider = SliderWindow(screen, w, h)
    WIDTH, HEIGHT = w, h


def main_menu():
    pygame.init()
    run = True
    network = Network()
    player = network.getP()
    player.ready = False
    while run:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('music/menu.mp3')
            pygame.mixer.music.play()
            pygame.mixer_music.set_volume(0)
        screen.fill((0, 0, 0))
        bgMenu.draw_with_mouse_pos(WIDTH, HEIGHT)
        draw_button(screen, imageButtonStartGame, 0, player, network)
        screen.blit(surfTitle, (50, 35))
        menuWidgetAllHeroes.draw_widget()
        menuWidgetAboutGame.draw_widget()
        menuWidgetElector.draw_widget()
        menuWidgetAboutHero.draw_widget()
        menuWidgetScreenSize.draw_widget()
        menuWidgetSlider.draw_widget()
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
            change_objects(w, h)
        clock.tick(60)


def waitingForConnection(character, player, network, player_settings):
    run = True
    waitingText = font.render('Waiting for a connection', False, (0, 255, 0))
    top_menu_text_pos_x = 10

    # nez_image = pygame.image.load('static/nezuko-pixel-art.jpeg')

    while run:
        player2 = network.send(player)
        screen.fill((0, 0, 0))
        # screen.blit(nez_image, (0, 0))
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
            map_preparation(player, network, player_settings)
        clock.tick(60)


if __name__ == '__main__':
    main_menu()