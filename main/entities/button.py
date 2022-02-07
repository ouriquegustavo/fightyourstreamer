from main.entities.entity import Entity
import pygame

class Button:
    def __init__(self, game, gid, x, y, dx, dy):
        super().__init__(game, gid)
        self.kind = 'button'
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
        self.zorder = 0
        
        self.sprite = pygame.Surface((self.dx, self.dy))
        self.sprite.fill((255,0,0,255))
        
        self.is_updating = True
        self.is_drawing = True
        
    def draw(self):
        self.game.display.blit(self.sprite, (self.x-self.dx/2, self.y-self.dy/2))
