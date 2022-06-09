from runningCount import RunningCount
import cards
import pygame
import sys

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)


def update():
    pass


def draw():
    pass


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        draw()
        update()
        pygame.display.flip()


# call main
if __name__ == '__main__':
    main()
