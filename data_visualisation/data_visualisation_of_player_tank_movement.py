import matplotlib.pyplot as plt
import json

x_filename = 'C:\\Users\\ayxan\\Documents\\current\\data_visualisation_python\\data_visualisation_on_tank_war\\tank_war\\coordinate_x.json'
y_filename = 'C:\\Users\\ayxan\\Documents\\current\\data_visualisation_python\\data_visualisation_on_tank_war\\tank_war\\coordinate_y.json'

with open(x_filename) as file_object:
    x_coordinates = json.load(file_object)

with open(y_filename) as file_object:
    y_coordinates = json.load(file_object)

plt.scatter(x_coordinates, y_coordinates, c=y_coordinates, cmap=plt.cm.Oranges, edgecolor='none', s=15)
plt.show()
