import pygame


class Font:
    def __init__(self, game):
        self.game = game
        self.start()

    def start(self):
        pygame.font.init()
        self.obj = pygame.font.SysFont('Arial', 12)

    def render(self, text, colour=(255, 255, 255, 255), antialias=True):
        return self.obj.render(text, antialias, colour)
