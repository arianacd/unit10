# by ariana daney
# last modified december 17
# unit 10 final project option 3

import pygame, sys
from pygame.locals import *

pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)


def target_circle():
    pygame.draw.circle(main_surface, (0, 0, 0), (250, 250), 250, 2)
    pygame.draw.circle(main_surface, (255, 255, 255), (250, 250), 220, 24)


target_circle()

pygame.display.set_caption("Target")
main_surface.fill((255, 255, 255))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
