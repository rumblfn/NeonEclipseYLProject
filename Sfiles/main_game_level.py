from copy import copy
from tiles import Tile
from main_map_settings import *
from enemyClass import Enemy
from hero1Enemy import Enemy_hero1
from hero3Enemy import Enemy_hero3
from _thread import start_new_thread
from player import speed_to_low
from spring import Spring
from ball_gun import Ball_gun
from balls import Ball
from trap import Trap


class LevelG:
    def __init__(self, level_data, surface, player_main, player_enemy, network, server_player, interface):
        self.round = True

        self.display_surface = surface
        self.level_data = level_data
        self.player_sprite = player_main
        self.player_enemy = player_enemy
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        self.server_player = server_player
        self.player_col = 0
        self.pos_x = 0
        self.network = network
        self.interface = interface
        self.tile_size = 64

        self.myself_dmg = 0

        self.enemy = pygame.sprite.GroupSingle()
        if self.player_enemy.name == 'Hero1':
            self.enemy_hero1_bullets = pygame.sprite.Group()
            enemy = Enemy_hero1(self.player_enemy)
        elif self.player_enemy.name == 'Hero3':
            enemy = Enemy_hero3(self.player_enemy)
        else:
            enemy = Enemy(self.player_enemy)

        self.enemy.add(enemy)
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.interface.update_screen_size(self.width, self.height)
        self.tiles = pygame.sprite.Group()
        self.springs = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.ball_guns = pygame.sprite.Group()
        self.gun_balls = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        tile_size = self.height / len(self.level_data)
        self.width = len(self.level_data[0]) * tile_size
        self.player_sprite.update_size(self.width, self.height)
        self.tile_size = tile_size = int(tile_size)
        self.player_sprite.initialize_server_player(self.server_player)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player_sprite.server_player.x = x
                    self.player_sprite.server_player.y = y
                    self.player_sprite.x = x
                    self.player_sprite.y = y
                    self.player.add(self.player_sprite)
                elif cell == 'S':
                    spring = Spring((x + tile_size // 2, y + tile_size), tile_size)
                    self.springs.add(spring)
                elif cell == 'G':
                    ball_gun = Ball_gun((x, y), tile_size)
                    self.ball_guns.add(ball_gun)
                elif cell == 'T':
                    trap = Trap((x + tile_size // 2, y), tile_size)  #midtop
                    self.traps.add(trap)
                elif cell != ' ':
                    tile = Tile((col_index, row_index), tile_size, cell, self.level_data, self.player_col)
                    self.tiles.add(tile)

    def horizontal_movement_collisions(self, player):
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

    def vertical_movement_collisions(self, player):
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.01

    def update_enemy(self):
        self.player_sprite.update_server()
        if self.player_sprite.resistance_potion_timer_ACTIVE:
            self.server_player.damage_given *= self.player_sprite.resistance_potion_no_save
            self.player_sprite.hp += self.myself_dmg * self.player_sprite.resistance_potion_no_save
        else:
            self.player_sprite.hp += self.myself_dmg
        player_enemy = self.network.send(self.player_sprite.server_player)

        self.player_enemy = player_enemy
        self.server_player.E = False
        self.server_player.damage_given = 0
        self.myself_dmg = 0

        self.enemy.sprite.rect.x = (player_enemy.x / 1920) * self.width
        self.enemy.sprite.rect.y = (player_enemy.y / 1080) * self.height

        if self.player_sprite.name != 'Hero3':
            self.myself_dmg -= player_enemy.damage_given
        else:
            if self.player_sprite.SHIELD_ACTIVE:
                self.player_sprite.SHIELD_HP -= player_enemy.damage_given
                if self.player_sprite.SHIELD_HP < 0:
                    self.player_sprite.hp += self.player_sprite.SHIELD_HP
            else:
                self.myself_dmg -= player_enemy.damage_given

        self.player_sprite.rect.x += player_enemy.diff_x
        self.enemy.sprite.update_values(player_enemy)

        self.enemy.sprite.get_input()

        if player_enemy.name == 'Hero1':
            if player_enemy.type_of_attack == 1:
                self.enemy.sprite.change_bullet_image()
            else:
                self.enemy.sprite.change_bullet_image_simple()
            if player_enemy.simpleAttack:
                self.enemy_hero1_bullets.add(self.enemy.sprite.create_bullet((
                    player_enemy.mouse_pos_x * self.width / 1920,
                    player_enemy.mouse_pos_y * self.height / 1080)))

            for sprite in self.enemy_hero1_bullets.sprites():
                if sprite.rect.colliderect(self.player_sprite.rect):
                    sprite.kill()
                for tile in self.tiles.sprites():
                    if tile.rect.collidepoint(sprite.rect.center):
                        sprite.kill()
                sprite.move()

            self.enemy.sprite.attacksE.draw(self.display_surface)
            for sprite in self.enemy.sprite.attacksE.sprites():
                sprite.rect.midbottom = self.enemy.sprite.rect.midbottom
                sprite.run_attackE()
                if sprite.rect.colliderect(self.player_sprite.rect):
                    if sprite.rect.x < self.player_sprite.rect.x:
                        self.player_sprite.rect.left = sprite.rect.right
                    else:
                        self.player_sprite.rect.right = sprite.rect.left
                    start_new_thread(speed_to_low, (self.player_sprite, self.enemy.sprite.e_time_speed_to_low))

            self.enemy_hero1_bullets.draw(self.display_surface)

        if player_enemy.name == 'Hero3':
            self.player_sprite.block_moving = player_enemy.Q_STUN

    def bullets_settings(self):
        if self.player_sprite.type_of_attack == 0:
            for sprite in self.player_sprite.bullets.sprites():
                if self.enemy.sprite.rect.collidepoint(sprite.rect.center):
                    self.server_player.damage_given += self.player_sprite.power
                    sprite.kill()
                for tile in self.tiles.sprites():
                    if tile.rect.collidepoint(sprite.rect.center):
                        sprite.kill()
                sprite.move()
        else:
            for sprite in self.player_sprite.bullets.sprites():
                if self.enemy.sprite.rect.collidepoint(sprite.rect.center):
                    self.server_player.damage_given += self.player_sprite.power
                    self.player_sprite.poisoning = True
                    sprite.kill()
                for tile in self.tiles.sprites():
                    if tile.rect.collidepoint(sprite.rect.center):
                        sprite.kill()
                sprite.move()

    def ESettings(self):
        for sprite in self.player_sprite.attacksE:
            sprite.rect.midbottom = self.player_sprite.rect.midbottom
            sprite.run_attackE()

    def springs_collisions(self):
        self.player_sprite.spring_jump_bool = False
        for sprite in self.springs.sprites():
            if sprite.spring_hit:
                sprite.change_spring()
            if sprite.image == sprite.surf1:
                if sprite.rect.colliderect(self.player_sprite.rect):
                    sprite.image = sprite.surf2
                    sprite.rect.y -= sprite.size // 4
                    sprite.spring_hit = True
                    self.player_sprite.spring_jump_bool = True
                if sprite.rect.colliderect(self.enemy.sprite.rect):
                    sprite.image = sprite.surf2
                    sprite.spring_hit = True
                    sprite.rect.y -= sprite.size // 4

    def balls_ball_gun(self):
        for sprite in self.ball_guns.sprites():
            if sprite.timer == 0:
                ball = Ball(sprite.rect.center, self.tile_size)
                self.gun_balls.add(ball)
        for sprite in self.gun_balls.sprites():
            for tile in self.tiles.sprites():
                if sprite.rect.colliderect(tile.rect):
                    sprite.kill()
            if sprite.rect.colliderect(self.player_sprite.rect):
                self.player_sprite.hp -= 7
                sprite.kill()
            if sprite.rect.colliderect(self.enemy.sprite.rect):
                self.server_player.damage_given += 7
                sprite.kill()

    def traps_collides(self):
        for sprite in self.traps.sprites():
            if not sprite.ACTIVE:
                if sprite.rect.colliderect(self.player_sprite.rect):
                    sprite.ACTIVE = True
                    if sprite.timer >= 30:
                        self.player_sprite.hp -= 5
                if sprite.rect.colliderect(self.enemy.sprite):
                    sprite.ACTIVE = True
                    if sprite.timer >= 30:
                        self.server_player.damage_given += 5
            if sprite.timer >= 60:
                self.tiles.add(sprite)
            if sprite.READY:
                trap_copy = copy(sprite)
                sprite.kill()
                self.traps.add(trap_copy)

    def run(self):
        if self.player_sprite.hp <= 0 and self.round or self.player_sprite.rect.y > self.height * 2:
            self.player_sprite.hp = 0
            self.player_sprite.rect.x = self.width / 2
            self.player_sprite.rect.y = self.height / 2
            self.server_player.ready = False
            self.round = False

        self.tiles.draw(self.display_surface)
        self.springs.draw(self.display_surface)
        self.ball_guns.update()
        self.ball_guns.draw(self.display_surface)
        self.gun_balls.update()
        self.gun_balls.draw(self.display_surface)
        self.traps.draw(self.display_surface)
        self.traps.update()
        self.traps_collides()
        self.balls_ball_gun()

        self.horizontal_movement_collisions(self.player.sprite)
        self.vertical_movement_collisions(self.player.sprite)
        self.springs_collisions()

        self.enemy.draw(self.display_surface)
        self.update_enemy()

        self.interface.check_inv_change_key()
        self.interface.draw_inventory()

        self.player.update()
        self.player.draw(self.display_surface)

        if self.player_sprite.name == 'Hero1':
            self.player_sprite.bullets.draw(self.display_surface)
            self.player_sprite.attacksE.draw(self.display_surface)
            self.ESettings()
            self.bullets_settings()
            if self.player_sprite.poisoning:
                self.player_sprite.poisoning_time += 1
                if self.player_sprite.poisoning_time % 60 == 0:
                    self.server_player.damage_given += self.player_sprite.power * 0.1
                if self.player_sprite.poisoning_time >= self.player_sprite.poisoning_time_max:
                    self.player_sprite.poisoning = False
                    self.player_sprite.poisoning_time = 0
            self.interface.draw_attacks_timers(self.player_sprite.shoot_bool, self.player_sprite.shoot_bool_max,
                                               self.player_sprite.attacksEBool, self.player_sprite.attacksEBool_max,
                                               self.player_sprite.Q_SLEEPER, self.player_sprite.Q_SLEEPER_MAX)
        elif self.player_sprite.name == 'Hero3':
            self.server_player.diff_x = 0
            if self.player_sprite.AA_ACTIVE and self.player_sprite.CURRENT_SPRITE_AA == 2:
                if self.player_sprite.rect.colliderect(self.enemy.sprite.rect):
                    if self.player_sprite.aa_repulsion:
                        if self.player_sprite.SIDE == 'right':
                            self.server_player.diff_x = 130
                        else:
                            self.server_player.diff_x = -130
                    self.server_player.damage_given += self.player_sprite.power
                if self.player_sprite.Q_ACTIVE:
                    self.player_sprite.Q_END = True
                    self.server_player.Q_STUN = True
                    self.player_sprite.Q_STUN_TIMER = 0
            if self.player_sprite.Q_STUN_TIMER >= 120:
                self.server_player.Q_STUN = False
            self.interface.draw_attacks_timers(self.player_sprite.AA_TIMER, self.player_sprite.AA_TIMER_MAX,
                                               self.player_sprite.E_TIMER, self.player_sprite.E_TIMER_MAX,
                                               self.player_sprite.Q_ACTIVE_TIMER, self.player_sprite.Q_ACTIVE_TIMER_MAX)

        self.interface.draw(self.player_sprite.hp, self.player_sprite.maxHp, self.player_sprite.power)
        self.interface.draw_enemy_health(self.enemy.sprite.hp, self.enemy.sprite.maxHp)
        self.interface.draw_game_progress(str(self.server_player.wins), str(self.server_player.loses))
        self.interface.draw_names(self.enemy.sprite.rect.midtop, self.player_sprite.rect.midtop)

