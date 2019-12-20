import pygame
import unit10project


class Target:
    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.score = 0

    def target_circle(self, p):
        c = p[0]
        a = p[1]
        b = p[2]
        pygame.draw.circle(self.main_surface, c, (250, 250), a, b)

    def get_score(self, position):
        target_color = self.main_surface.get_at(position)
        if target_color == (unit10project.WHITE, 255):
            self.update_score(1)
        elif target_color == (unit10project.BLACK, 255):
            self.update_score(3)
        elif target_color == (unit10project.BLUE, 255):
            self.update_score(5)
        elif target_color == (unit10project.RED, 255):
            self.update_score(7)
        elif target_color == (unit10project.YELLOW, 255):
            self.update_score(9)







