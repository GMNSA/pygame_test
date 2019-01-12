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
    y = 430
    width = 40
    height = 60
    speed = 5

    is_jump = False
    jump_count = 10

    run = True

    while run:
        pygame.time.delay(30)   # sleep (0.03) sec

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()   # press key

        if keys[pygame.K_LEFT] and x > 5:
            x -= speed
            print("Left -5 x = %s" % x)
        elif keys[pygame.K_RIGHT] and x < (500 - width - 5):
            x += speed
            print("Right +5 x = %s" % x)
        elif not is_jump:
            if keys[pygame.K_UP] and y > 5:
                y -= speed
                print("Up -5 y = %s" % y)
            elif keys[pygame.K_DOWN] and y < (500 - height - 10):
                y += speed
                print("Down +5 y = %s" % y)
            elif keys[pygame.K_SPACE]:
                is_jump = True
        elif is_jump:
            if jump_count >= -10:
                if jump_count < 0:
                    y += (jump_count ** 2) / 2
                else:
                    y -= (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10
        else:
            print("What is wrong!!!")

        # fill the window with black
        win.fill((0, 0, 0))
        # draw blue square
        pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
