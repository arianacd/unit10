# by ariana daney
# last modified december 17
# unit 10 final project option 3

import pygame, sys
from pygame.locals import *
import target
pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Target")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
main_surface.fill(WHITE)
my_target = target.Target(main_surface)
circles = [(BLACK, 151, 2), (WHITE, 150, 30), (BLACK, 120, 30), (BLUE, 90, 30), (RED, 60, 30), (YELLOW, 30, 0)]
for x in circles:
    my_target.target_circle(x)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
