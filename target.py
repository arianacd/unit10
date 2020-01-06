import pygame

WHITE = (255, 255, 254)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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
        if target_color == (255, 255, 254, 255):
            self.update_score(1)
        elif target_color == (0, 0, 0, 255):
            self.update_score(3)
        elif target_color == (0, 0, 255, 255):
            self.update_score(5)
        elif target_color == (255, 0, 0, 255):
            self.update_score(7)
        elif target_color == (255, 255, 0, 255):
            self.update_score(9)

    def update_score(self, score):
        self.main_surface.fill((255, 255, 255))
        circles = [(BLACK, 151, 2), (WHITE, 150, 30), (BLACK, 120, 30), (BLUE, 90, 30), (RED, 60, 30), (YELLOW, 30, 0)]
        for x in circles:
            self.target_circle(x)
        self.score += score
        mouse_font = pygame.font.SysFont("Helvetica", 32)
        mouse_label = mouse_font.render(str(self.score), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))
        pygame.display.update()


