import pygame


class Target:
    def __init__(self, main_surface):
        self.main_surface = main_surface

    def target_circle(self, p):
        c = p[0]
        a = p[1]
        b = p[2]
        pygame.draw.circle(self.main_surface, c, (250, 250), a, b)
