# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: November 4th, 2026
# | Last update..: November 5th, 2026
# | WhatIs.......: Celular Automaton 2D - Class
# +-----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# convolve2d: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
# NumPy 2D Convolution: A Practical Guide: https://medium.com/@heyamit10/numpy-2d-convolution-a-practical-guide-958d97edf0d6

# Moore neighborhood: https://en.wikipedia.org/wiki/Moore_neighborhood
# Cellular Automata: Life from Simple Rules: https://www.youtube.com/watch?v=wbPgoZ2d0Nw&t=1s
# Conway's Game of Life rules: B3/S23 with examples: https://www.gameoflifelab.com/articles/conways-game-of-life-rules

# Life-like cellular automaton: https://en.wikipedia.org/wiki/Life-like_cellular_automaton
# B3/S23
# * If a cell is dead, and has 3 neighbors, then the cell is born in the next tick
# * If a cell is alive, and has 2 or 3 neighbors, then the cell survives to the next tick
# * Otherwise, a cell becomes empty in the next tick.

# ------------------------- Libraries -------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# ------------------------- Constraints -------------------------
GENERATIONS = 25
SPEED = 0.1

CANVAS = 50
PROBABILITIES = [0.8, 0.2]

# Vecindad de Moore
MAIN_STATES = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

# --------------------------- Functions ----------------------------
def update_canvas(current_grid):
  # Contar vecinos (convolve2d)
  num_neighbors = convolve2d(current_grid, MAIN_STATES, mode="same", boundary="wrap")

  # Game of Life rules (B3/S23)
  birth = (current_grid == 0) & (num_neighbors == 3)
  survive = (current_grid == 1) & ((num_neighbors == 2) | (num_neighbors == 3))

  return (birth | survive).astype(int)

# --------------------------- Code ----------------------------
canvas = np.random.choice([0, 1], size=(CANVAS, CANVAS), p=PROBABILITIES)

fig, ax = plt.subplots()
img = ax.imshow(canvas, cmap="binary")

# Animación
for i in range(GENERATIONS):
  canvas = update_canvas(canvas)
  img.set_data(canvas)
  plt.pause(SPEED)

plt.show()
