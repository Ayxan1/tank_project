import pygame
import json
class PlayerData():

    def __init__(self):
        # Creating coordinate database (json file) for data visualisation.
        self.x_filename = 'coordinate_x.json'
        self.y_filename = 'coordinate_y.json'
        self.tank_x_coordinates = []
        self.tank_y_coordinates = []


    def save_tank_coordinates(self, tank):
        self.tank_x_coordinates.append(tank.rect.centerx)
        self.tank_y_coordinates.append((800 - tank.rect.centery))


    def save_player_data_in_file(self):
        with open(self.x_filename, 'a') as file_object:
            json.dump(self.tank_x_coordinates, file_object)
        with open(self.y_filename, 'a') as file_object:
            json.dump(self.tank_y_coordinates, file_object)
