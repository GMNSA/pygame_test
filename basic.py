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

        keys = pygame.key.get_pressed()   # press key

        if keys[pygame.K_LEFT]:
            x -= speed
            print("Left -5 x = %s" % x)
        elif keys[pygame.K_RIGHT]:
            x += speed
            print("Right +5 x = %s" % x)
        elif keys[pygame.K_UP]:
            y -= speed
            print("Up -5 y = %s" % y)
        elif keys[pygame.K_DOWN]:
            y += speed
            print("Down +5 y = %s" % y)

        # fill the window with black
        win.fill((0, 0, 0))
        # draw blue square
        pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
