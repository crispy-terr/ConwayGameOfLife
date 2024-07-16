import random
from Grid import Grid
import pygame
import time

def gen_random_grid(rows, cols, dense_thresh):
    var = [[0 for x in range(rows)] for y in range(cols)] 
    for i in range(rows):
        for j in range(cols):
            rand = random.randint(0,100)
            if rand > dense_thresh:
                var[j][i] = True
            else:
                var[j][i] = False
    return var

# Configure
height = int(input("Height of grid: "))
width = int(input("Width of grid: "))
live_color_select = int(input("1: Red\n2: Green\n3: Blue\n4: RGB\nEnter: "))

if live_color_select == 1:
    live_color = (255, 0, 0)
elif live_color_select == 2:
    live_color = (0, 255, 0)
elif live_color_select == 3:
    live_color = (0, 0, 255)
else:
    r = int(input("Red: "))
    g = int(input("Green: "))
    b = int(input("Blue: "))
    live_color = (r, g, b)

density_select = int(input("Density:\n1: Low\n2: Moderate\n3: High\nEnter: "))

match density_select:
    case 1:
        density_threshold = 25
    case 3:
        density_threshold = 80
    case _:
        density_threshold = 40
    

cool = gen_random_grid(int(width/10),int(height/10), density_threshold)

print("\n  ******************************************\n  *                                        ")
print("  *  Settings:                             ")
print(f"  *  Hight: {height}                             ")
print(f"  *  Width: {width}                             ")
print(f"  *  Color: {live_color}                    ")
print(f"  *  Density: {density_threshold}                           ")
print("  *                                        ")
print("  ******************************************\n")

# Display
pygame.init()
surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Conway's Game of Life")
cool_grid = Grid(cool, surface, live_color)

cool_grid.draw_board()

running = True
while running:
    cool_grid.run_conway_rules()
    cool_grid.draw_board()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

