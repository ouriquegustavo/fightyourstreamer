import pygame

class Button:
    def __init__(self, game, id_, x, y, dx, dy):
        self.game = game
        self.id_ = id_
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
        self.sprite = pygame.Surface((dx,dy))
        self.sprite.fill((255,0,0,255))
        
        self.is_updating = True
        self.is_drawing = True
        
    def draw(self):
        self.game.display.blit(self.sprite, (self.x-self.dx/2, self.y-self.dy/2))
