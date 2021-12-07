import sys
from pygame.locals import *
from dataConsts import *


def draw_cursor(sc):
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        sc.blit(imageCursorClicked, (mx - 2, my - 2))
    else:
        sc.blit(imageCursorNormal, (mx, my))


def draw_button(sc, image, pos_y_diff):
    surf = pygame.Surface((buttonHostSizeWidth, buttonHostSizeHeight))
    surf.blit(image, (0, 0))
    x_lef_top = WIDTH / 2 - buttonHostSizeWidth / 2
    y_left_top = HEIGHT / 2 - buttonHostSizeHeight / 2 - pos_y_diff
    button = pygame.Rect(x_lef_top, y_left_top, buttonHostSizeWidth, buttonHostSizeHeight)
    mx, my = pygame.mouse.get_pos()
    if button.collidepoint((mx, my)):
        if pygame.mouse.get_pressed()[0]:
            for hero in menuWidgetAllHeroes.heroes:
                if hero['selected']:
                    waitingForConnection(hero)
    sc.blit(surf, (x_lef_top, y_left_top))


def main_menu():
    run = True

    while run:
        screen.fill((0, 0, 0))
        draw_button(screen, imageButtonStartHost, 30)
        draw_button(screen, imageButtonJoinHost, -30)
        screen.blit(surfTitle, (50, 35))
        menuWidgetAllHeroes.draw_widget()
        menuWidgetAboutGame.draw_widget()
        menuWidgetElector.draw_widget()
        menuWidgetAboutHero.draw_widget()
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
        clock.tick(60)


def waitingForConnection(character):
    global font
    run = True
    waitingText = font.render('Waiting for a connection', False, (0, 255, 0))
    top_menu_text_pos_x = 10

    while run:
        screen.fill((0, 0, 0))
        screen.blit(waitingText, (top_menu_text_pos_x, top_menu_text_pos_x))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        clock.tick(60)


if __name__ == '__main__':
    main_menu()
