import random

import pygame
from pygame.locals import *

from const import *

velocity = 1
clock = pygame.time.Clock()

matrix = [[0 for _ in range(WINDOW_WIDTH)] for _ in range(WINDOW_HEIGHT)]


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Sand Simulation')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Event loop
    while True:
        clock.tick(60)

        # Blit everything to the screen
        screen.blit(background, (0, 0))

        # update sand
        for y in range(WINDOW_HEIGHT - 2, -1, -1):
            new_y = y + velocity
            for x in range(WINDOW_WIDTH):
                if matrix[y][x] == 1:
                    if new_y < WINDOW_HEIGHT - 1 and matrix[new_y + 1][x] == 0:
                        matrix[y][x] = 0
                        matrix[new_y + 1][x] = 1
                    elif new_y < WINDOW_HEIGHT - 1 and x > 0 and matrix[new_y + 1][x - 1] == 0:
                        matrix[y][x] = 0
                        matrix[new_y + 1][x - 1] = 1
                    elif new_y < WINDOW_HEIGHT - 1 and x < WINDOW_WIDTH - 1 and matrix[new_y + 1][x + 1] == 0:
                        matrix[y][x] = 0
                        matrix[new_y + 1][x + 1] = 1

        # Display sand
        for y in range(WINDOW_HEIGHT):
            for x in range(WINDOW_WIDTH):
                if matrix[y][x] == 1:
                    # color the sand based on the height between blue and green
                    r = 0
                    g = 255 - y * 255 // WINDOW_HEIGHT
                    b = y * 255 // WINDOW_HEIGHT

                    pygame.draw.rect(screen,
                                     (r, g, b),
                                     (x * OBJECT_SIZE, y * OBJECT_SIZE, OBJECT_SIZE, OBJECT_SIZE))

        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == MOUSEBUTTONDOWN:
                # get the position of the mouse
                pos = pygame.mouse.get_pos()
                x, y = pos
                x = x // OBJECT_SIZE
                y = y // OBJECT_SIZE

                # if the position is not inside the window, skip
                if x < 30 or x >= WINDOW_WIDTH - 30 or y < 30 or y >= WINDOW_HEIGHT - 30:
                    continue
                # set between 0 and 50 random sand around the mouse in a circle shape with radius 30
                for _ in range(200):
                    new_x = x + random.randint(-30, 30)
                    new_y = y + random.randint(-30, 30)
                    if new_x < 0 or new_x >= WINDOW_WIDTH or new_y < 0 or new_y >= WINDOW_HEIGHT:
                        continue
                    chance = random.randint(0, 100)
                    if chance < 50:
                        matrix[new_y][new_x] = 1

        pygame.display.flip()


if __name__ == '__main__':
    main()
