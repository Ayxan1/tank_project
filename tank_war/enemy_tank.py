import pygame
import math
import sys
from enemy_bullet import EnemyBullet

class EnemyTank():

    def __init__(self, screen):
         """Initialize the tank and set its starting position."""
         self.screen = screen

         # Load the ship image and get its rect.
         self.image = pygame.image.load('images/enemy.png').convert_alpha()
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()



         # Start each new ship at the bottom center of the screen.
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.top + 385

         # Movement flag.
         self.moving_right = False
         self.moving_left = False
         self.moving_forward = False
         self.moving_backward = False

         # Anlge of rotaion rotate tank -90 before game begining.
         self.angle = 0

         # Turn on/off rotation blitting. Recent images of rotated tank.
         self.on = 0
         self.recent_image = ''
         self.recent_rect = ''

         # Activate moving.
         self.activate = True

         # Collisions.
         # forward collisions.
         self.right_wall_collision = False
         self.left_wall_collision = False
         self.top_wall_collision = False
         self.bottom_wall_collision = False

         # backward collisions.
         self.back_right_wall_collision = False
         self.back_left_wall_collision = False
         self.back_top_wall_collision = False
         self.back_bottom_wall_collision = False


         # Health of enemy tank.
         self.enemy_health = 10

         self.allowed_enemy_bullets = 30



    def check_screen_limits(self, angle):
        angle = self.angle
        if self.angle <= 0:
            angle = -1 * self.angle
        else:
            angle = 360 - angle

        if self.rect.centerx > (self.screen_rect.right - 85) :
            if abs(angle) > 180 and abs(angle) < 360:
                self.back_right_wall_collision = True
            else:
                self.right_wall_collision = True


        if self.rect.centery > (self.screen_rect.bottom - 85) :
            if (abs(angle) < 90 and abs(angle) >= 0) or (abs(angle) > 270 and abs(angle) < 360):
                self.back_bottom_wall_collision = True
            else:
                self.bottom_wall_collision = True


        if self.rect.centerx < (self.screen_rect.left + 85) :
            if abs(angle) > 0 and abs(angle) < 180:
                self.back_left_wall_collision = True
            else:
                self.left_wall_collision = True

        if self.rect.centery < (self.screen_rect.top + 85) :
            if abs(angle) > 90 and abs(angle) < 270:
                self.back_top_wall_collision = True
            else:
                self.top_wall_collision = True

    def check_free_angle_for_moving_forward(self):
        angle = self.angle
        if self.angle <= 0:
            angle = -1 * self.angle
        else:
            angle = 360 - angle
        if self.right_wall_collision == True:
            if abs(angle) > 180 and abs(angle) < 360:
                self.right_wall_collision = False
        if self.top_wall_collision == True:
            if abs(angle) > 90 and abs(angle) < 270:
                self.top_wall_collision = False
        if self.left_wall_collision == True:
            if abs(angle) > 0 and abs(angle) < 180:
                self.left_wall_collision = False
        if self.bottom_wall_collision == True:
            if (abs(angle) < 90 and abs(angle) > 0) or (abs(angle) > 270 and abs(angle) < 360):
                self.bottom_wall_collision = False


    def check_free_angle_for_moving_backward(self):
        angle = self.angle
        if self.angle <= 0:
            angle = -1 * self.angle
        else:
            angle = 360 - angle

        if self.back_right_wall_collision == True:
            if abs(angle) > 0 and abs(angle) < 180:
                self.back_right_wall_collision = False
        if self.back_bottom_wall_collision == True:
            if abs(angle) > 90 and abs(angle) < 270:
                self.back_bottom_wall_collision = False

        if self.back_left_wall_collision == True:
            if abs(angle) > 270 and abs(angle) < 360:
                self.back_left_wall_collision = False


        if self.back_top_wall_collision == True:
            if (abs(angle) < 90 and abs(angle) > 0) or (abs(angle) > 270 and abs(angle) < 360):
                self.back_top_wall_collision = False

    def update(self):
        if self.moving_right:

            self.angle -= 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)
            self.check_free_angle_for_moving_forward()
            self.check_free_angle_for_moving_backward()

            self.on = 1
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)
        if self.moving_left:

            self.angle += 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)

            self.check_free_angle_for_moving_forward()
            self.check_free_angle_for_moving_backward()

            self.on = 1
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)

        if self.moving_forward:
            angle_90 = 1
            speed_factor_y = 1.5
            speed_factor_x = 1.8

            if (self.angle > -100 and self.angle < -80) or (self.angle > 260 and self.angle < 280) or (self.angle > -280 and self.angle < -260) or (self.angle > 80 and self.angle < 100) :
                speed_factor_x = 1

            if self.angle > 360 or self.angle < -360:
                if self.angle > 360:
                    self.angle = self.angle - 360
                else:
                    self.angle = self.angle + 360

            if self.angle == 90 or self.angle == -90 or self.angle == 270 or self.angle == -270:
                angle_90 = 0
                if self.angle == 90 or self.angle == -270:
                    difference_between_x_y = -3
                    if self.right_wall_collision == False and self.left_wall_collision == False and self.top_wall_collision == False and self.bottom_wall_collision == False:
                        self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                else:
                    difference_between_x_y = 3
                    if self.right_wall_collision == False and self.left_wall_collision == False and self.top_wall_collision == False and self.bottom_wall_collision == False:
                        self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                self.back_right_wall_collision = False
                self.back_left_wall_collision = False
                self.back_top_wall_collision = False
                self.back_bottom_wall_collision = False
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)



            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    if self.right_wall_collision == False and self.left_wall_collision == False and self.top_wall_collision == False and self.bottom_wall_collision == False:
                        self.rect.centery -= speed_factor_y * angle_90
                        self.check_screen_limits(self.angle)
                else:
                    if self.right_wall_collision == False and self.left_wall_collision == False and self.top_wall_collision == False and self.bottom_wall_collision == False:
                        self.rect.centery += speed_factor_y * angle_90
                        self.check_screen_limits(self.angle)
                self.back_right_wall_collision = False
                self.back_left_wall_collision = False
                self.back_top_wall_collision = False
                self.back_bottom_wall_collision = False
            else:
                # Assigning is for preventing dublicate calling self.angle variable.
                rotation_angle = self.angle
                if self.right_wall_collision == False and self.left_wall_collision == False and self.top_wall_collision == False and self.bottom_wall_collision == False:
                    if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                        self.rect.centery -= speed_factor_y * angle_90
                        self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                        self.rect.centery += speed_factor_y * angle_90
                        self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                        self.rect.centery += speed_factor_y * angle_90
                        self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                        self.rect.centery -= speed_factor_y * angle_90
                        self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    self.back_right_wall_collision = False
                    self.back_left_wall_collision = False
                    self.back_top_wall_collision = False
                    self.back_bottom_wall_collision = False


        if self.moving_backward:
            angle_90 = 1
            speed_factor_y = 2.5
            speed_factor_x = 2.8

            if (self.angle > -100 and self.angle < -80) or (self.angle > 260 and self.angle < 280) or (self.angle > -280 and self.angle < -260) or (self.angle > 80 and self.angle < 100) :
                speed_factor_x = 1

            if self.angle > 360 or self.angle < -360:
                if self.angle > 360:
                    self.angle = self.angle - 360
                else:
                    self.angle = self.angle + 360


            if self.angle == 90 or self.angle == -90 or self.angle == 270 or self.angle == -270:
                angle_90 = 0
                if self.angle == 90 or self.angle == -270:
                    difference_between_x_y = -3
                    if self.back_right_wall_collision == False and self.back_left_wall_collision == False and self.back_top_wall_collision == False and self.back_bottom_wall_collision == False:
                        self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                else:
                    difference_between_x_y = 3
                    if self.back_right_wall_collision == False and self.back_left_wall_collision == False and self.back_top_wall_collision == False and self.back_bottom_wall_collision == False:
                        self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                self.right_wall_collision = False
                self.left_wall_collision = False
                self.top_wall_collision = False
                self.bottom_wall_collision = False
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)


            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    if self.back_right_wall_collision == False and self.back_left_wall_collision == False and self.back_top_wall_collision == False and self.back_bottom_wall_collision == False:
                        self.rect.centery += speed_factor_y * angle_90
                        self.check_screen_limits(self.angle)
                else:
                    if self.back_right_wall_collision == False and self.back_left_wall_collision == False and self.back_top_wall_collision == False and self.back_bottom_wall_collision == False:
                        self.rect.centery -= speed_factor_y * angle_90
                        self.check_screen_limits(self.angle)
                self.right_wall_collision = False
                self.left_wall_collision = False
                self.top_wall_collision = False
                self.bottom_wall_collision = False
            else:
                # Assigning is for preventing dublicate calling self.angle variable.
                if self.back_right_wall_collision == False and self.back_left_wall_collision == False and self.back_top_wall_collision == False and self.back_bottom_wall_collision == False:
                    rotation_angle = self.angle
                    if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                        self.rect.centery += speed_factor_y * angle_90
                        self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                        self.rect.centery -= speed_factor_y * angle_90
                        self.rect.centerx -= -1 * int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                        self.rect.centery -= speed_factor_y * angle_90
                        self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                        self.rect.centery += speed_factor_y * angle_90
                        self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))
                        self.check_screen_limits(self.angle)
                    self.right_wall_collision = False
                    self.left_wall_collision = False
                    self.top_wall_collision = False
                    self.bottom_wall_collision = False


    def update_auto_movement(self, tank):
        pass


    def rotate_for_given_angle(self, angle, tank, part, tw_settings, enemy_tank, enemy_bullets):
        angle_for_enemy_tank_movement = 0
        start_movement = 0
        if part == 1:
            if angle >= 0 and angle <= 90:
                angle_for_enemy_tank_movement = angle
                start_movement = 1
            elif angle > 180 and angle <= 270:
                angle_for_enemy_tank_movement = angle - 180
                start_movement = 1
        elif part == 2:
            if angle > 90 and angle <= 180:
                angle_for_enemy_tank_movement = angle
                start_movement = 1
            elif angle > 270 and angle <= 360:
                angle_for_enemy_tank_movement = angle - 180
                start_movement = 1
        elif part == 3:
            if angle > 180 and angle <= 270:
                angle_for_enemy_tank_movement = angle
                start_movement = 1
            elif angle > 0 and angle <= 90:
                angle_for_enemy_tank_movement = angle + 180
                start_movement = 1
        elif part == 4:
            if angle > 270 and angle <= 360:
                angle_for_enemy_tank_movement = angle
                start_movement = 1
            elif angle > 90 and angle <= 180:
                angle_for_enemy_tank_movement = angle + 180
                start_movement = 1

        if start_movement == 1:
            rotate_right = 1
            enemy_tank.moving_forward = False
            ############
            if len(enemy_bullets) < enemy_tank.allowed_enemy_bullets:
                new_bullet = EnemyBullet(tw_settings, self.screen, enemy_tank)
                enemy_bullets.add(new_bullet)
            ############
            while self.angle <= angle_for_enemy_tank_movement:
                rotate_right = 0
                self.angle += 2
                image = pygame.transform.rotozoom(self.image, self.angle, 1)
                self.check_free_angle_for_moving_forward()
                self.check_free_angle_for_moving_backward()
                self.on = 1
                self.recent_image = image
                self.recent_rect =  self.rect
                self.blitme(image, self.rect)

            if rotate_right == 1:
                while self.angle >= angle_for_enemy_tank_movement:
                    rotate_right = 0
                    self.angle -= 2
                    image = pygame.transform.rotozoom(self.image, self.angle, 1)
                    self.check_free_angle_for_moving_forward()
                    self.check_free_angle_for_moving_backward()
                    self.on = 1
                    self.recent_image = image
                    self.recent_rect =  self.rect
                    self.blitme(image, self.rect)

            enemy_tank.moving_forward = True




    def blitme(self, image='', rect=''):
        """Draw the ship at its current location."""

        if self.on == 0:
            # Rotating doesn't start and rotated image is not displayed.
            self.screen.blit(self.image, self.rect)
        else:
            # Rotating start and rotated image is displayed.
            self.on = 1
            self.screen.blit(self.recent_image, self.rect)
            pygame.display.flip()
