import pygame
from sys import exit
from math import sqrt, cos, sin
from random import random, randint

SIZE = W, H = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (59, 59, 59)
MAGENTA = (255, 0, 255)

scl = 6
angle = 137.5

rad = 3


def phyllotaxis(n, N, surf, offsetX, offsetY, c_scl):
    if n > N: return

    phi = n * angle
    r = round(scl * sqrt(n))

    x = round(r * cos(phi) + offsetX)
    y = round(r * sin(phi) + offsetY)

    c = n * c_scl * 255 / N
    col = (c, 0, c)

    pygame.draw.circle(surf, col, (x, y), rad, 3)


def run():
    pygame.init()
    pygame.display.set_caption("Phyllotaxis")
    bg = pygame.display.set_mode(SIZE)
    surface = pygame.display.set_mode(SIZE)
    surface.set_alpha(100)
    clock = pygame.time.Clock()

    bg.fill(WHITE)

    n = 0
    N = 0
    stX = -1
    stY = -1
    c_scl = -1

    while 1:
        
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if n != N:        
            phyllotaxis(n, N, surface, stX, stY, c_scl)
        else:
            stX = randint(0, W)
            stY = randint(0, H)
            N = randint(1, 300)
            c_scl = random()
            n = 0
            start = True

        n = n + 1

        pygame.display.update()


if __name__ == "__main__":
    run()
