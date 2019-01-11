# -*- coding:utf-8 -*-
# AUTHOR:   _who
# FILE:     basic.py
# ROLE:     TODO (some explanation)
# CREATED:  2019-01-11 22:00:07


import pygame


def main():

    pygame.init()
    win = pygame.display.set_mode((500, 500))   # display size 500 x 500

    pygame.display.set_caption("TEST Game")

    x = 50
    y = 50
    width = 40
    height = 60
    speed = 5

    run = True

    while run:
        pygame.time.delay(100)   # sleep (0.1) sec

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()
