import random

from dataConsts import *
import pygame.mixer_music
from main_game_level import *
import sys

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
    global sleeper_status, sleeper_status_for_loading, sleeper_time
    sleeper_loading = 1
    sleeper_status = False

    new_time = sleeper_time
    while True:
        sleeper_time -= 60
        if sleeper_time <= 0:
            break
        clock.tick(1)

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


def main_game(server_player, net, play_main):
    global images_round_starting, images_round_ending

    def update_server_player_pos():
        server_player.x = WIDTH // 2
        server_player.y = HEIGHT // 2

    def server_player_settings():
        server_player.name = player_main.name
        server_player.power = player_main.power
        server_player.maxHp = player_main.maxHp
        server_player.hp = player_main.maxHp
        server_player.width = player_main.width * 1920 / WIDTH
        server_player.height = player_main.height * 1080 / HEIGHT
        server_player.simpleAttack = False
        server_player.ready = True
        if player_main.name == 'Hero1':
            server_player.e_time_speed_to_low = player_main.e_time_speed_to_low
        elif player_main.name == 'Hero3':
            server_player.SHIELD_HP = player_main.SHIELD_HP

    maps = [map1, map2, map3, map4, map5]
    # random.shuffle(maps)
    i = -1
    interface.prepare_for_main()

    while server_player.wins < 3 and server_player.loses < 3:
        i += 1
        network = copy(net)
        player_main = copy(play_main)
        player_enemy = network.send(server_player)
        run = True
        player_main.hp = player_main.maxHp
        update_server_player_pos()
        server_player_settings()
        player_enemy = network.send(server_player)
        sleep(0.5)
        player_enemy = network.send(server_player)
        level = LevelG(maps[i], screen, player_main, player_enemy, network, server_player, interface)
        level.player_sprite.block_moving = False
        if server_player.loses >= 3:
            server_player.win = False
            break

        for j in range(0, 55, 5):
            screen.blit(images_round_starting[int(j / 10)], (0, 0))
            pygame.display.update()

        while run:
            screen.fill((0, 0, 0))
            level.run()

            if not level.player_enemy.ready:
                server_player.wins += 1
                run = False
            if not level.round:
                run = False
                server_player.loses += 1

            draw_cursor(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    server_player.ready = False
                    server_player.wins = 0
                    server_player.loses = 0
                    network.send(server_player)
                    pygame.quit()
                    sys.exit()
            clock.tick(FPS)

        for j in range(0, 55, 5):
            screen.blit(images_round_ending[int(j / 10)], (0, 0))
            pygame.display.update()

        if server_player.wins >= 3:
            server_player.win = True
    game_end(server_player, net)


def game_end(server_player, network):
    f2 = pygame.font.SysFont('serif', 48)
    if server_player.wins > 2:
        text = f2.render(victory_texts[random.randint(0, 2)], True, (0, 255, 0))
    else:
        text = f2.render(defeat_texts[random.randint(0, 2)], True, (0, 255, 0))
    run = True
    server_player.ready = False
    waiting_time = waiting_after_ending_game
    while run:
        waiting_time -= 1
        screen.fill((0, 0, 0))
        screen.blit(text, (30, 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                server_player.ready = False
                server_player.wins = 0
                server_player.loses = 0
                network.send(server_player)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    server_player.ready = False
                    server_player.wins = 0
                    server_player.loses = 0
                    network.send(server_player)
        if waiting_time <= 0:
            run = False
        clock.tick(FPS)

    main_menu(server_player, network)


def map_preparation(player, network, player_settings):
    global sleeper_status_for_loading, sleeper_time
    run = True
    player.x = WIDTH // 4
    player.y = round(HEIGHT * (2 / 3))
    level = Level(level1_map, screen, player_settings, interface, sleeper_time)
    start_new_thread(sleeper, ())

    def portalParkourMap(sc, player_parkour):
        try:
            player_to_copy += 1
        except:
            player_to_copy = 0

        if player_to_copy == 0:
            player_save = copy(player_parkour)
            player_saved = True
            player_to_copy += 1
        p = False
        runParkourMap = True
        level_p = LevelParkour(level_parkour_map, screen, player_settings)
        count = 0
        finished = False
        while runParkourMap:
            level.sleeper_time = sleeper_time

            sc.fill((255, 255, 255))
            bgMapPreparation.draw()
            level_p.run()
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        p = True
                    level_p.check_fall = False
                if level_p.portalParkour:
                    finished = True
            if sleeper_status:
                runParkourMap = False
            count += 1
            if level_p.check_fall:
                p = True
            player_settings['keys'] = level_p.keys_taken
            level_p.events_check()
            if finished:
                level.portalParkour = False
                break
            if p:
                runParkourMap = False
            clock.tick(FPS)
        if p:
            if player_saved:
                portalParkourMap(sc, player_save)
            else:
                portalParkourMap(sc, player_parkour)

    while run:
        level.sleeper_time = sleeper_time

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
            sleeper_status_for_loading = False

        draw_cursor(screen)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.ready = False
                player.wins = 0
                player.loses = 0
                network.send(player)
                pygame.quit()
                sys.exit()
        if level.portalParkour:
            pygame.mixer.music.stop()
            portalParkourMap(screen, level.player)
        if level.rerun_level:
            level.rerun_player()
            level.rerun_level = False
            continue
        clock.tick(FPS)


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
        HEROES, interface, images_round_starting, images_round_ending
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

    images_round_ending = []
    for i in range(1, 7):
        images_round_ending.append(pygame.transform.scale(pygame.image.load(f'static/game_round/round_bg{i}.png'),
                                                          (WIDTH, HEIGHT)))
    images_round_starting = []
    for i in range(7, 13):
        images_round_starting.append(pygame.transform.scale(pygame.image.load(f'static/game_round/round_bg{i}.png'),
                                                            (WIDTH, HEIGHT)))


def main_menu(server_player=False, net=False):
    global sleeper_time, new_time
    sleeper_time = new_time
    run = True
    if not server_player:
        pygame.init()
        network = Network()
        player = network.getP()
        player.ready = False
    else:
        network = net
        player = server_player
        player.ready = False
        player.name = None
        player.wins = 0
        player.loses = 0
        network.send(player)
        sleep(0.2)
        network.send(player)
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
                player.ready = False
                player.wins = 0
                player.loses = 0
                network.send(player)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                menuWidgetElector.change_image(('key', event))
                if event.key == K_ESCAPE:
                    run = False
                    player.ready = False
                    player.wins = 0
                    player.loses = 0
                    network.send(player)
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
        clock.tick(FPS)


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
                player.wins = 0
                player.loses = 0
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
        clock.tick(FPS)
