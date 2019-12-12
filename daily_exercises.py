# by ariana daney
# last modified december 12, 2019
# unit 10 daily exercises

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Daily Exercises")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (0, 255, 0), ((325, 150), (275, 285), (125, 285), (75, 150), (200, 50)), 0)
pygame.draw.circle(main_surface, (0, 0, 255), (330, 100), 17, 0)
pygame.draw.rect(main_surface, (255, 0, 0), (250, 183, 90, 45), 0)
pygame.draw.ellipse(main_surface, (255, 0, 0), (335, 270, 35, 75), 1)
# makes the letter "z"
pygame.draw.line(main_surface, (0, 0, 255), (125, 110), (180, 110), 3)
pygame.draw.line(main_surface, (0, 0, 255), (180, 110), (125, 160), 2)
pygame.draw.line(main_surface, (0, 0, 255), (125, 160), (180, 160), 3)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


