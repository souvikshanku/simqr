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

def fill_separators(grid, start, end):
    if start[0] == end[0]:
        for i in range(end[1] - start[1]):
            grid[start[0], start[1] + i] = 2
    if start[1] == end[1]:
        for i in range(end[0] - start[0]):
            grid[start[0] + i, start[1]] = 2
    
    return grid

def draw_timing_patterns(grid):
    t1 = [(6, 8 + i) for i in range(5)]

    for idx, t in enumerate(t1):
        grid[t] = 0 if grid[t1[idx - 1]] else 1

    t2 = [(8 + i, 6) for i in range(5)]
    for idx, t in enumerate(t2):
        grid[t] = 0 if grid[t2[idx -1]] else 1

    return grid

grid = np.array([0] * 441).reshape([21, 21])

grid = fill_square_border(grid, (0, 0), (6, 6), 1)
grid = fill_square_border(grid, (14, 0), (20, 6), 1)
grid = fill_square_border(grid, (0, 14), (6, 20), 1)

grid = fill_squares(grid, (2, 2), 3)
grid = fill_squares(grid, (16, 2), 3)
grid = fill_squares(grid, (2, 16), 3)

grid = fill_separators(grid, (7, 0), (7, 8))
grid = fill_separators(grid, (0, 7), (7, 7))
grid = fill_separators(grid, (7, 13), (7, 21))
grid = fill_separators(grid, (0, 13), (7, 13))
grid = fill_separators(grid, (13, 0), (13, 8))
grid = fill_separators(grid, (13, 7), (21, 7))

grid = draw_timing_patterns(grid)

grid[13, 8] = 1
plt.imshow(grid)