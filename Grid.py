import pygame

BLACK = (0,0,0)

class Grid:
    def __init__(self, grid, surf, color):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.surf = surf
        self.color = color

    def __str__(self):
        var = ""
        for row in self.grid:
            var += "\n"
            for element in row:
                if element:
                    var += " 1"
                else:
                    var += " 0"
        var += f"\n\nRows: {self.rows}\nColumns: {self.cols}"
        return var
    
    def draw_board(self):
        xPos = 0
        yPos = 0
        for i in range(self.rows):
            yPos+=10
            xPos = 0
            for j in range(self.cols):
                cell = pygame.Rect(xPos, yPos, 10, 10)
                if(self.grid[i][j]):
                    pygame.draw.rect(self.surf, self.color, cell)
                else:
                    pygame.draw.rect(self.surf, BLACK, cell)
                xPos+=10

    def run_conway_rules(self):
        next_grid = [[0 for x in range(self.rows*10)] for y in range(self.cols*10)] 
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        boundX = r+i
                        boundY = c+j

                        if boundX >= 0 and boundX < self.rows and boundY >=0 and boundY < self.cols:
                            if self.grid[boundX][boundY]:
                                live_neighbors += 1
                if(self.grid[r][c]):
                    if live_neighbors<2 or live_neighbors>3:
                        next_grid[r][c] = False
                    else:
                        next_grid[r][c] = True
                else:
                    if live_neighbors == 3:
                        next_grid[r][c] = True
                    else:
                        next_grid[r][c] = False
        self.grid = next_grid