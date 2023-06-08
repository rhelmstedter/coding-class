import pygame
import numpy as np
import random

# Set up the dimensions of the grid
grid_size = (80, 60)
cell_size = 10
width, height = grid_size[0] * cell_size, grid_size[1] * cell_size

# Initialize the Pygame window
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Create the grid
grid = np.zeros(grid_size)

# Randomize the initial state of the grid
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        grid[i, j] = random.choice([0, 1])

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a copy of the grid for the next generation
    new_grid = np.copy(grid)

    # Update the grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Count the number of live neighbors
            neighbors = (
                grid[(i - 1) % grid_size[0], (j - 1) % grid_size[1]]
                + grid[(i - 1) % grid_size[0], j]
                + grid[(i - 1) % grid_size[0], (j + 1) % grid_size[1]]
                + grid[i, (j - 1) % grid_size[1]]
                + grid[i, (j + 1) % grid_size[1]]
                + grid[(i + 1) % grid_size[0], (j - 1) % grid_size[1]]
                + grid[(i + 1) % grid_size[0], j]
                + grid[(i + 1) % grid_size[0], (j + 1) % grid_size[1]]
            )

            # Apply the rules of the Game of Life
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    # Update the grid
    grid = np.copy(new_grid)

    # Clear the window
    window.fill(BLACK)

    # Draw the grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(
                    window, WHITE, (i * cell_size, j * cell_size, cell_size, cell_size)
                )

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
