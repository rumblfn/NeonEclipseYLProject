import pygame

map = [
    '                               ',
    '           P                   ',
    '                               ',
    '                  ####         ',
    '                  ########     ',
    '                    ####       ',
    '   #####                       ',
    '   #####        ##             ',
    ' ########       #####          ',
    ' ########        ####          ',
    '  #####                        ',
    '  #####               S        ',
    '   ##                ###       ',
    '                     ###       ',
    '                               ',
    '            ######             ',
    '             ###########       ',
    '        S    #########         ',
    '       ##########              ',
]

map1 = [
    '                               ',
    '           P                   ',
    '                               ',
    '                  ####         ',
    '                  ########     ',
    '                    ####       ',
    '   #####                       ',
    '   #####        ##             ',
    ' ########       #####          ',
    ' ########        ####          ',
    '  #####                        ',
    '  #####               S        ',
    '   ##                ###       ',
    '                     ###       ',
    '                               ',
    '            ######             ',
    '             ###########       ',
    '        S    #########         ',
    '       ##########              ',
]

map2 = [
    '#################################',
    '#################################',
    '###G               P         ####',
    '###G                         ####',
    '##       ####  ###   #####  #####',
    '##         ##  ###   #####  #####',
    '###G                          ###',
    '###G                          ###',
    '##             ###   #######  ###',
    '##     ####    ###   #######  ###',
    '###      ##                   ###',
    '###G                          ###',
    '#####        #####   #####  #####',
    '#####          ###   #####  #####',
    '#####G                      #####',
    '#####GS                     #####',
    '#######      ######    ##########',
    '#######      ######S   ##########',
    '#################################',
]

map3 = [
    '         ###          ##       ',
    '         ###          ##       ',
    '                               ',
    '#                              ',
    '###      P                     ',
    '                 ###           ',
    '                  ##           ',
    '                   #           ',
    '    ###                   ##   ',
    '    ###        ##         ##   ',
    '               #######  ####   ',
    '                 #####  #####  ',
    '                  ##      ###  ',
    '     ##           ##           ',
    '#######                        ',
    '###########               #####',
    '###########            S  #####',
    '###############################',
    '###############################',
]

map5 = [
    '                          #####',
    '           P              #####',
    '                            ###',
    '                            ###',
    '#####                     #####',
    '#####                     #####',
    '###              ###           ',
    '                  ##           ',
    '                  ##      #####',
    '           ###            #####',
    '            ##                 ',
    '            ##                 ',
    '     ###                       ',
    '      ##                       ',
    '      ##                       ',
    '###########               #####',
    '###########            S  #####',
    '###############################',
    '###############################',
]

map4 = [
    '######                   ######',
    '######     P             ######',
    '######                   ######',
    '###       ##       ##       ###',
    '###       ####   ####       ###',
    '###                         ###',
    '                               ',
    '        ###############        ',
    '        ###############        ',
    '          ###########          ',
    '          ###########          ',
    '              ###              ',
    '              ###              ',
    '          ##  ###  ##          ',
    '   S      ##       ##      S   ',
    '#####                     #####',
    '#####                     #####',
    '###############################',
    '###############################',
]

try:
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    tile_size = HEIGHT // len(map)
    screen_width = len(map[0]) * tile_size
    screen_height = len(map) * tile_size
except:
    pass
