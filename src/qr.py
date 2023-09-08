import numpy as np
import matplotlib.pyplot as plt


def fill_square_border(grid, corner1, corner2, value=1):
    """
      A +--+--+--+--+  D
        |           | 
        +           +
        |           |
      B +--+--+--+--+  C
    """
    size = corner2[0] - corner1[0]
    # side AD
    for i in range(size + 1):
        grid[corner1[0], corner1[1] + i] = value
    # side BC
    for i in range(size):
        grid[corner2[0], corner2[1] - i] = value
    # side AB
    for i in range(size + 1):
        grid[corner1[0] + i, corner1[1]] = value
    # side CD
    for i in range(size):
        grid[corner2[0] - i , corner2[1]] = value

    return grid

def fill_squares(grid, corner1, size):
    for i in range(size):
        for j in range(size):
            grid[corner1[0] + i, corner1[1] + j] = 1
    
    return grid

grid = np.array([0] * 441).reshape([21, 21])

grid = fill_square_border(grid, (0, 0), (6, 6), 1)
grid = fill_square_border(grid, (14, 0), (20, 6), 1)
grid = fill_square_border(grid, (0, 14), (6, 20), 1)

grid = fill_squares(grid, (2, 2), 3)
grid = fill_squares(grid, (16, 2), 3)
grid = fill_squares(grid, (2, 16), 3)