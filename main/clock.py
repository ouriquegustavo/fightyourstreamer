import pygame

class Clock:
    def __init__(self, game, tps):
        self.game = game
        self.tps = tps
        
        self.clock = pygame.time.Clock()
        
    def tick(self, tps=None):
        if tps:
            self.tps=tps
        self.clock.tick(self.tps)
        
