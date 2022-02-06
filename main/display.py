import pygame

class Display:
    def __init__(self, game, width, height):
        self.game = game
        self.h = height
        self.w = width
        
    def start(self):
        self.display = pygame.display.set_mode(
            (self.w, self.h), pygame.DOUBLEBUF
        )
        
    def blit(self,*args, **kwargs):
        self.display.blit(*args, **kwargs)
        
    def update(self):
        self.display.fill((0,0,255))

        pygame.display.flip()
