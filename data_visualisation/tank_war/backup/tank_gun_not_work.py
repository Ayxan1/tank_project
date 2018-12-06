import pygame
import math

class Tank():

    def __init__(self, screen):
         """Initialize the tank and set its starting position."""
         self.screen = screen

         # Load the ship image and get its rect. tank_1_transp    back_gun.png
         self.image = pygame.image.load('images/back_gun.png')
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()


         # Start each new ship at the bottom center of the screen.
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom

         # Gun of tank.
         self.gun_image = pygame.image.load('images/little_gun1.png')
         self.gun_rect = self.gun_image.get_rect()
         self.gun_rect.centerx = self.rect.centerx


         # Movement flag.
         self.moving_right = False
         self.moving_left = False
         self.moving_forward = False
         self.moving_backward = False

         # Gun movement flag.
         self.gun_moving_left = False
         self.gun_moving_right = False



         # Anlge of tank rotaion.
         self.angle = 0

         # Anlge of gun rotaion.
         self.gun_angle = 0

         # Turn on/off rotation blitting. Recent images of rotated tank.
         self.on = 0
         self.recent_image = ''
         self.recent_rect = ''
         self.recent_image_without_gun = self.image
         self.original_image_without_gun = pygame.image.load('images/back_gun.png')
         self.original_tank_image = pygame.image.load('images/back_gun.png')
         self.original_gun_image = pygame.image.load('images/little_gun1.png')

         # Turn on/off rotation blitting. Recent images of rotated gun.
         self.gun_on = 0
         self.gun_recent_image = self.gun_image
         self.gun_recent_rect = ''


    def update(self):
        # Rotating of gun.
        if self.gun_moving_right:
            self.gun_angle -= 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.gun_image, self.gun_angle, 1)
            self.gun_on = 1
            self.original_gun_image = image
            self.gun_recent_image = image
            self.gun_recent_rect =  self.gun_rect
            self.gun_blitme(image, self.gun_rect)

        if self.gun_moving_left:
            self.gun_angle += 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.gun_image, self.gun_angle, 1)
            self.gun_on = 1
            self.original_gun_image = image
            self.gun_recent_image = image
            self.gun_recent_rect =  self.gun_rect
            self.gun_blitme(image, self.gun_rect)

        # Rotating of tank.
        if self.moving_right:
            self.angle -= 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)
            self.on = 1
            self.original_tank_image = image
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)

        if self.moving_left:
            self.angle += 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)
            self.on = 1
            self.original_tank_image = image
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)

        if self.moving_forward:
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
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                else:
                    difference_between_x_y = 3
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)



            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    self.rect.centery -= speed_factor_y * angle_90
                else:
                    self.rect.centery += speed_factor_y * angle_90
            else:
                # Assigning is for preventing dublicate calling self.angle variable.
                rotation_angle = self.angle

                if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))


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
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                else:
                    difference_between_x_y = 3
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)


            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    self.rect.centery += speed_factor_y * angle_90
                else:
                    self.rect.centery -= speed_factor_y * angle_90
            else:
                # Assigning is for preventing dublicate calling self.angle variable.
                rotation_angle = self.angle

                if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx -= -1 * int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))



    def blitme(self, image='', rect=''):
        """Draw the tank at its current location."""
        if self.on == 0:
            # Rotating doesn't start and rotated image is not displayed.
            self.screen.blit(self.image, self.rect)
        else:
            # Rotating start and rotated image is displayed.
            self.on = 1
            # self.screen.blit(self.original_tank_image, self.recent_rect)
            pygame.display.flip()



    def gun_blitme(self, image='', rect=''):
        """Draw the gun at its current location."""
        if self.gun_on == 0:
            # Rotating doesn't start and rotated image is not displayed.
            self.gun_recent_rect = self.gun_image.get_rect()
            self.gun_rect.centerx = self.rect.centerx
            self.gun_rect.centery = self.rect.centery
            # self.screen.blit(self.gun_image, self.gun_rect)
        else:
            # Rotating start and rotated image is displayed.
            self.gun_on = 1
            self.gun_recent_rect = self.gun_recent_image.get_rect()
            self.gun_recent_rect.centerx = self.rect.centerx
            self.gun_recent_rect.centery = self.rect.centery

            self.recent_image = self.original_tank_image

            # testing
            rect = self.original_tank_image.get_rect()
            self.screen.blit(self.original_tank_image, rect)
            # testing


            self.recent_image.blit(self.original_gun_image, [20, -2])
            # son  self.screen.blit(self.gun_recent_image, self.recent_rect)


            # @@@@@@@self.recent_image.blit(self.gun_recent_image, [20, -2])
            #self.screen.blit(self.gun_image, [self.rect.centerx-15, self.rect.centery-45])
            pygame.display.flip()
