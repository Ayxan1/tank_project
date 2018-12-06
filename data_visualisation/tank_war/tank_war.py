import sys
import pygame
from pygame.sprite import Group
import pygame.font


from settings import Settings
from tank import Tank
from enemy_tank import EnemyTank
from enemy_bullet import EnemyBullet
from enemy_dedector import EnemyDedector
from scoreboard import Scoreboard
import game_functions as gf
from data_saver import PlayerData




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

    # ScoreBoard.
    score = Scoreboard(screen, enemy_tank, tank)

    player1 = PlayerData()



    while True:

        """
        if enemy_tank.enemy_health == 0 or tank.player_health == 0:
            if enemy_tank.enemy_health == 0:
                return 'You WOOOOONNNN'
            return 'Enemy Wooonnnn'
        """



        gf.check_events(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets, player1)
        tank.update()
        enemy_tank.update()
        enemy_tank.update_auto_movement(tank)
        gf.update_bullets_for_collision(enemy_tank, bullets, enemy_bullets, score, tank)

        gf.update_enemy_bullets_for_collision(enemy_tank, bullets, enemy_bullets, tank, score)

        # Dedecting of player tank.
        gf.check_dedector_collision_with_player_tank(enemy_dedector, tank, enemy_tank, tw_settings, enemy_bullets)

        gf.check_collision_between_two_tanks(enemy_tank, tank)


        bullets.update()
        enemy_bullets.update()


        gf.update_screen(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets, enemy_dedector)
        score.show_score()

        # Saving player info.
        player1.save_tank_coordinates(tank)



run_game()
