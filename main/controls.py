import pygame

class Controls:
    def __init__(self, game):
        self.game = game
        self.m = {
            'up': pygame.K_s,
            'down': pygame.K_w,
            'left': pygame.K_a,
            'right': pygame.K_d,
            'attack': pygame.K_e,
        }
    
        self.c = {k: 0 for k in self.m}
        
        self.h = {k: 0 for k in self.m}
        
    def get_keys(self):
        keys = pygame.key.get_pressed()
        for k, v in self.m.items():
            self.c[k] = keys[v]
            self.h[k] = self.c[k] * (self.h[k] + 1)
            
