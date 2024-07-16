import random
from Grid import Grid
import pygame

def gen_random_grid(rows, cols):
    var = [[0 for x in range(rows)] for y in range(cols)] 
    for i in range(rows):
        for j in range(cols):
            rand = random.randint(0,1)
            if rand == 1:
                var[j][i] = True
            else:
                var[j][i] = False
    return var

cool = gen_random_grid(500,500)

GREEN = (0,255,0)

# GUI Stuff
pygame.init()
surface = pygame.display.set_mode((500,500))
cool_grid = Grid(cool, surface)

cool_grid.draw_board()

running = True
while running:
    cool_grid.run_conway_rules()
    cool_grid.draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

