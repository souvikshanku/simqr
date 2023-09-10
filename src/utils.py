# This probably needs a little bit of refactoring. Not my cleanest code :(

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
            grid[start[0], start[1] + i] = 0
    if start[1] == end[1]:
        for i in range(end[0] - start[0]):
            grid[start[0] + i, start[1]] = 0
    
    return grid

def draw_timing_patterns(grid):
    t1 = [(6, 8 + i) for i in range(5)]

    for idx, t in enumerate(t1):
        grid[t] = 0 if grid[t1[idx - 1]] else 1

    t2 = [(8 + i, 6) for i in range(5)]
    for idx, t in enumerate(t2):
        grid[t] = 0 if grid[t2[idx -1]] else 1

    return grid

def fill_format_info(grid, info):
    info = [int(i) for i in info]

    for i in range(1, 8):
        grid[-i, 8] = info[i]

    for i in range(8):
        grid[8, 13 + i] = info[7 + i]

    for i in range(6):
        grid[8, i] = info[i]
    
    grid[8, 7] = info[i + 1]
    grid[8, 8] = info[i + 2]
    grid[7, 8] = info[i + 3]

    for i in range(6):
        grid[i, 8] = info[- i - 1]


    return grid

def fill_up_odd(grid, msg_even):
    c = 0
    start = 20
    end = -1
    step = -1
    for j in range(20, 5, -2):
        for i in range(start, end, step):
            if grid[i, j] == None:
                _mask = ((i + j) % 2 == 0)
                grid[i, j] = int(msg_even[c]) ^ _mask
                c += 1
        if start != 0:
            start = 0
            end = 21
            step = 1
        else:
            start = 20
            end = -1
            step = -1
    # can't really explain this
    start = 0
    end = 21
    step = 1
    for j in range(5, 0, -2):
        for i in range(start, end, step):
            if grid[i, j] == None:
                _mask = ((i + j) % 2 == 0)
                grid[i, j] = int(msg_even[c]) ^ _mask
                c += 1
        if start != 0:
            start = 0
            end = 21
            step = 1
        else:
            start = 20
            end = -1
            step = -1
    return grid

def fill_up_even(grid, msg_odd):
    c = 0
    start = 20
    end = -1
    step = -1
    for j in range(19, 6, -2):
        for i in range(start, end, step):
            if grid[i, j] == None:
                # grid[i, j] = int(msg_odd[c])
                _mask = ((i + j) % 2 == 0)
                grid[i, j] = int(msg_odd[c]) ^ _mask
                c += 1
        if start != 0:
            start = 0
            end = 21
            step = 1
        else:
            start = 20
            end = -1
            step = -1

    for j in range(4, -1, -2):
        for i in range(start, end, step):
            if grid[i, j] == None:
                # grid[i, j] = int(msg_odd[c])
                _mask = ((i + j) % 2 == 0)
                grid[i, j] = int(msg_odd[c]) ^ _mask

                c += 1
        if start != 0:
            start = 0
            end = 21
            step = 1
        else:
            start = 20
            end = -1
            step = -1

    return grid
