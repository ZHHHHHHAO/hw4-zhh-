import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# give a function for game by ChatGPT
def initialize_grid(size):
    grid = np.zeros((size, size), dtype=bool)
    # how the game works
    pattern = np.array([[False, False, True],[True, False, True],[False, True, True]], dtype=bool)
    x, y = (size - pattern.shape[0]) // 2, (size - pattern.shape[1]) // 2
    grid[x:x + pattern.shape[0], y:y + pattern.shape[1]] = pattern
    return grid

# how many times
k = 100

# make the game no bountary by ChatGPT
def evolve(grid):
    size = grid.shape[0]
    new_grid = grid.copy()
    for i in range(size):
        for j in range(size):
            # chack the neighbor by google
            neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            live_neighbors = sum(grid[x % size, y % size] for x, y in neighbors)
            if grid[i, j]:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = False  # die
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = True  # relife
    return new_grid

# initialize the table
grid_size = 25
grid = initialize_grid(grid_size)

# function for animation
def update(frame):
    im.set_data(grid)
    grid[:] = evolve(grid)
# crate the animation
fig = plt.figure()
im = plt.imshow(grid, cmap = 'binary', interpolation = 'none')
ani = animation.FuncAnimation(fig, update, frames = k, repeat = False)

# gif code by ChatGPT
ani.save('game_of_life.gif', writer = 'pillow', fps = 10, savefig_kwargs = {'facecolor': 'red', 'edgecolor': 'black'})

# picrure code by Chat GPT
plt.imshow(grid, cmap = 'binary', interpolation = 'none')
plt.savefig('game_of_life.png', facecolor = 'red')