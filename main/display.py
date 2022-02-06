import pygame

class Display:
    def __init__(self, game, width, height):
        self.game = game
        self.h = height
        self.w = width
        self.start()
        
    def start(self):
        self.display = pygame.display.set_mode(
            (self.w, self.h), pygame.DOUBLEBUF
        )
        
    def blit(self,*args, **kwargs):
        self.display.blit(*args, **kwargs)
        
    def update(self):
        self.display.fill((0,0,255))
        
        keys = list(self.game.entity_manager.entities)
        for k in keys:
            ent = self.game.entity_manager.entities[k]
            if hasattr(ent, 'is_drawing') and ent.is_drawing:
                ent.draw()

        pygame.display.flip()
