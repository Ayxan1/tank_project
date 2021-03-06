import sys
import pygame
from settings import Settings
from tank import Tank
from enemy_tank import EnemyTank
from enemy_bullet import EnemyBullet
from enemy_dedector import EnemyDedector
import game_functions as gf
from pygame.sprite import Group

import threading
def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    tw_settings = Settings()
    screen = pygame.display.set_mode((tw_settings.screen_width, tw_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a tank.
    tank = Tank(screen)

    enemy_tank = EnemyTank(screen)

    enemy_dedector = EnemyDedector(screen, enemy_tank)

    # Make a group to store bullets in.
    bullets = Group()
    enemy_bullets = Group()

    ###########################################################
    # Threads for each function.
    t1 = threading.Thread(target=tank.update, args=())
    t2 = threading.Thread(target=enemy_tank.update, args=())
    ###########################################################


    while True:
        print('________active threads_____________ ', str(threading.activeCount()))
        gf.check_events(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets)

        tank.update()
        enemy_tank.update()
        enemy_tank.update_auto_movement(tank)

        gf.update_bullets_for_collision(enemy_tank, bullets, enemy_bullets)

        # Dedecting of player tank.
        gf.check_dedector_collision_with_player_tank(enemy_dedector, tank, enemy_tank, tw_settings, enemy_bullets)

        bullets.update()
        enemy_bullets.update()
        gf.update_screen(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets, enemy_dedector)
run_game()
