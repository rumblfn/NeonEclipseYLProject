from dataConsts import *
import pygame.mixer_music
from main_game_level import *
import sys
import datetime

import pygame.mixer_music
from pygame.locals import *
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
    global sleeper_status, sleeper_status_for_loading
    sleeper_time = 3
    sleeper_loading = 1
    sleeper_status = False

    sleep(sleeper_time - sleeper_loading)
    sleeper_status_for_loading = True

    sleep(sleeper_loading)
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
                    waitingForConnection(player, network, hero)
    sc.blit(surf, (x_lef_top, y_left_top))


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    pygame.display.update()


def main_game(server_player, network, player_main):
    def update_server_player_pos():
        server_player.x = WIDTH // 2
        server_player.y = HEIGHT // 2

    def server_player_settings():
        server_player.name = player_main.name
        server_player.power = player_main.power
        server_player.maxHp = player_main.maxHp
        server_player.hp = player_main.hp
        server_player.width = player_main.width
        server_player.height = player_main.height
        if player_main.name == 'Hero1':
            server_player.e_time_speed_to_low = player_main.e_time_speed_to_low

    run = True
    update_server_player_pos()
    server_player_settings()
    player_enemy = network.send(server_player)
    sleep(0.5)
    player_enemy = network.send(server_player)

    level = LevelG(map, screen, player_main, player_enemy, network, server_player, interface)
    level.player_sprite.block_moving = False

    while run:
        screen.fill((0, 0, 0))

        level.run()
        draw_cursor(screen)

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
    level = Level(level1_map, screen, player_settings, interface)
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
            count += 1
            if to_print:
                info_text_parkour()
                if count == 150:
                    to_print = False
            if level_p.check_fall:
                portalParkourMap(sc, player_parkour, False)
            level_p.events_check()
            clock.tick(60)

    while run:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('music/preparation_map.mp3')
            pygame.mixer.music.play()
        if sleeper_status:
            pygame.mixer.music.stop()
            main_game(player, network, level.player_sprite)
        bgMapPreparation.draw()
        level.run()

        if sleeper_status_for_loading:
            level.player_sprite.block_moving = True

        draw_cursor(screen)

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
        HEROES, interface
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
    interface = Interface(w, h, screen)
    WIDTH, HEIGHT = w, h
    if bool(menuWidgetSlider.vol_changed):
        if menuWidgetSlider.vol_changed == 1:
            pygame.mixer.music.set_volume(menuWidgetSlider.vol_changed - 1)
        else:
            pygame.mixer.music.set_volume(menuWidgetSlider.vol_changed / 100)
        menuWidgetSlider.vol_changed = None


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
                menuWidgetSlider.check_click_onslider()
                menuWidgetSlider.check_sound_off()

        w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
        if w != WIDTH or h != HEIGHT:
            if w == h == 1000:
                w, h = WI, HE
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            change_objects(w, h)
        if bool(menuWidgetSlider.vol_changed):
            if menuWidgetSlider.vol_changed == 1:
                pygame.mixer.music.set_volume(menuWidgetSlider.vol_changed - 1)
            else:
                pygame.mixer.music.set_volume(menuWidgetSlider.vol_changed / 100)
            menuWidgetSlider.vol_changed = None
        clock.tick(60)


def waitingForConnection(player, network, player_settings):
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
            map_preparation(player, network, player_settings)
        clock.tick(60)


if __name__ == '__main__':
    main_menu()
