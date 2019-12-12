# by ariana daney
# last modified december 12, 2019
# unit 10, recreating a picture

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Night Sky")
main_surface.fill((16, 78, 139))
pygame.draw.circle(main_surface, (204, 204, 204), (90, 110), 40, 0)

pygame.draw.circle(main_surface, (204, 204, 204), (342, 57), 3, 0)





while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
