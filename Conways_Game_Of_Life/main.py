import pygame
import random

pygame.init()

# Pygame Config

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 240

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def gen(num):
    # Generate random x/y co-ordinate positions for each value in the range of random
    # positions
    # Set used to avoid duplication
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])

def draw_grid(positions):

    # Draw Cells
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) # unpack values defined in top_lift

    # Draw Rows
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    # Draw Columns
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def adjust_grid(positions):
    all_neighbours = set() # live cells from current instance
    new_positions = set() # fresh set to track new positions based on rules

    for position in positions:
        neighbours = get_neighbours(position)
        all_neighbours.update(neighbours)

        # filter function to search through neighbour position as x
        # this will be used to determine conditions
        neighbours = list(filter(lambda x: x in positions, neighbours))

        # by proxy, rule 1 and 3 will be covered by this, as the positions
        # will not be added to the new set
        # and therefore deleted
        if len(neighbours) in (2,3):
            new_positions.add(position) # rule 2 - survival

    for position in all_neighbours:
        neighbours = get_neighbours(position)
        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) == 3:
            new_positions.add(position) # rule 4 - reproduction

    return new_positions

def get_neighbours(pos):
    x, y = pos
    neighbours = []
    # check each row around a given cell for x/y increments of 1
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue # ignore current position

            neighbours.append((x + dx, y + dy))

    return neighbours


def main():
    running = True
    playing = False
    count = 0
    update_freq = 120

    positions = set()
    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():

            # Check for Quit Game
            if event.type == pygame.QUIT:
                running = False

            # Check for Mousedown Cell Creation
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = col, row

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            # Quality of Life Processes
            if event.type == pygame.KEYDOWN:

                # Pause / Play
                if event.key == pygame.K_SPACE:
                    playing = not playing

                # Clear the Board
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                # Random Board Generation
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2,24) * GRID_WIDTH) # Update range if wanting more / less cells

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()