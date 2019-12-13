# by Ariana Daney
# last modified december 13, 2019
# unit 10, recreating a picture

import pygame, sys
from pygame.locals import *
import random

pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)


def make_star():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pygame.draw.circle(main_surface, (204, 204, 204), (x, y), 3, 0)


def buildings(p):
    x = p[0]
    y = p[1]
    pygame.draw.rect(main_surface, (0, 0, 0), (x, y, 70, 500), 0)


def window(p):
    x = p[0]
    y = p[1]
    pygame.draw.rect(main_surface, (255, 215, 0), (x, y, 8, 8), 0)


def main():
    pygame.display.set_caption("Night Sky")
    main_surface.fill((16, 78, 139))
    pygame.draw.circle(main_surface, (204, 204, 204), (90, 110), 40, 0)
    for x in range(20):
        make_star()
    building_point = [(0, 350), (30, 270), (100, 400), (150, 320), (200, 250), (260, 450), (310, 400),
                      (360, 270), (420, 370), (470, 200)]
    for x in building_point:
        buildings(x)
    pygame.draw.ellipse(main_surface, (110, 110, 110), (125, 280, 200, 450), 20)
    window_points = [(45, 320), (70, 340), (45, 460), (70, 460), (410, 380), (370, 290)]
    for y in window_points:
        window(y)


main()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

