import sys
import pygame
from bullet import Bullet
from enemy_bullet import EnemyBullet
from data_saver import PlayerData



def check_events(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets, player1):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save all player info in a file before closing game.
            player1.save_player_data_in_file()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                # Save all player info in a file before closing game.
                #     save_coordinates_in_file()
                # Quick exit.
                player1.save_player_data_in_file()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                 # Create a new bullet and add it to the bullets group.
                 if len(bullets) < tw_settings.bullets_allowed :
                     new_bullet = Bullet(tw_settings, screen, tank)
                     bullets.add(new_bullet)
            elif event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                tank.moving_right = True

                #  ------   manual enemy_tank controller enemy_tank.moving_right = True

            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                tank.moving_left = True

                #  ------   manual enemy_tank controller enemy_tank.moving_left = True
            elif event.key == pygame.K_UP:
                # Move the ship to the right.
                tank.moving_forward = True

                #  ------   manual enemy_tank controller enemy_tank.moving_forward = True
            elif event.key == pygame.K_DOWN:
                # Move the ship to the left.
                tank.moving_backward = True

                #  ------   manual enemy_tank controller enemy_tank.moving_backward = True



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                tank.moving_right = False

                #  ------   manual enemy_tank controller   .moving_right = False
            if event.key == pygame.K_LEFT:
                # Move the ship to the left.
                tank.moving_left = False

                #  ------   manual enemy_tank controller   .moving_left = False
            if event.key == pygame.K_UP:
                # Move the ship to the right.
                tank.moving_forward = False

                #  ------   manual enemy_tank controller   .moving_forward = False
            if event.key == pygame.K_DOWN:
                # Move the ship to the left.
                tank.moving_backward = False

                #  ------   manual enemy_tank controller   .moving_backward = False




def update_bullets_for_collision(enemy_tank, bullets, enemy_bullets, score, tank):

    if pygame.sprite.spritecollideany(enemy_tank, bullets) is not None:
        if enemy_tank.enemy_health > 0:
            enemy_tank.enemy_health -= 1
            for bullet in bullets.copy():
                bullets.remove(bullet)
            score.prep_score(enemy_tank, tank)



def update_enemy_bullets_for_collision(enemy_tank, bullets, enemy_bullets, tank, score):

    if pygame.sprite.spritecollideany(tank, enemy_bullets) is not None:
        if tank.player_health > 0:
            tank.player_health  -= 1
            for bullet in enemy_bullets.copy():
                enemy_bullets.remove(bullet)
            score.prep_score(enemy_tank, tank)




def check_dedector_collision_with_player_tank(enemy_dedector, tank, enemy_tank, tw_settings, enemy_bullets):
    # print('___________ EnemyTank angle ', enemy_tank.angle, '________ enemy_dedector angle ', enemy_dedector.dedector_angle)
    part = 0
    if (tank.rect.centerx < enemy_tank.rect.centerx) and (tank.rect.centery < enemy_tank.rect.centery):
        part = 1
        #print('player tank is in part 1')
    elif (tank.rect.centerx < enemy_tank.rect.centerx) and (tank.rect.centery > enemy_tank.rect.centery):
        part = 2
        #print('player tank is in part 2')
    elif (tank.rect.centerx > enemy_tank.rect.centerx) and (tank.rect.centery > enemy_tank.rect.centery):
        part = 3
        #print('player tank is in part 3')
    elif (tank.rect.centerx > enemy_tank.rect.centerx) and (tank.rect.centery < enemy_tank.rect.centery):
        part = 4
        #print('player tank is in part 4')

    if pygame.sprite.collide_rect(enemy_dedector, tank):
        # Checking if player tank is on the back of enemy_tank or not.
        dedector_angle = enemy_dedector.dedector_angle
        enemy_tank.rotate_for_given_angle(dedector_angle, tank, part, tw_settings, enemy_tank, enemy_bullets)


def check_collision_between_two_tanks(enemy_tank, tank):
    if pygame.sprite.collide_rect(enemy_tank, tank):
        enemy_tank.rect.centerx += 10
        enemy_tank.rect.centery += 10


def update_screen(tw_settings, screen, tank, enemy_tank, bullets, enemy_bullets, enemy_dedector):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    #    print('Enemy :  ', enemy_tank.enemy_health, '     Player :  ', tank.player_health)
    background_image = pygame.image.load("images/background.bmp").convert_alpha()



    #screen.fill((0, 0, 0))
    screen.blit(background_image, [0, 0])


    tank.blitme()
    enemy_tank.blitme()

    # dedector rotation
    enemy_dedector.rotate_dedector(enemy_tank)


    # Player bullets.
    for bullet in bullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx >= 1200 or bullet.rect.centery <= 0 or bullet.rect.centery >= 800:
            bullets.remove(bullet)

    for bullet in bullets.sprites():
        bullet.draw_bullet()


    # Enemy Bullets.
    for bullet in enemy_bullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx >= 1200 or bullet.rect.centery <= 0 or bullet.rect.centery >= 800:
            enemy_bullets.remove(bullet)

    for bullet in enemy_bullets.sprites():
        bullet.draw_bullet()


    # Make most recently drawn screen visible.
    pygame.display.flip()
