import numpy as np
import matplotlib.pyplot as plt

from encode.reed_solomon import encode, encode_format_info
from utils import (
    draw_timing_patterns,
    fill_format_info,
    fill_separators,
    fill_squares,
    fill_square_border,
    fill_up_even,
    fill_up_odd,
)


def draw(message):
    grid = np.array([None] * 441).reshape([21, 21])

    grid = fill_square_border(grid, (0, 0), (6, 6), 1)
    grid = fill_square_border(grid, (14, 0), (20, 6), 1)
    grid = fill_square_border(grid, (0, 14), (6, 20), 1)

    grid = fill_square_border(grid, (1, 1), (5, 5), 0)
    grid = fill_square_border(grid, (15, 1), (19, 5), 0)
    grid = fill_square_border(grid, (1, 15), (5, 19), 0)

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

    grid[13, 8] = 1  # Dark Module

    grid = fill_format_info(grid, encode_format_info(message))

    enc_msg = encode(message)
    msg_even = [enc_msg[m] for m in range(len(enc_msg)) if m % 2 == 0]
    msg_odd = [enc_msg[m] for m in range(len(enc_msg)) if m % 2 != 0]

    grid = fill_up_odd(grid, msg_even)
    grid = fill_up_even(grid, msg_odd)

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.imshow(grid.astype(int), cmap="Greys")
    plt.show()
