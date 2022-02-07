from main.entities.entity import Entity
import pygame 

class Wall(Entity):
    @property
    def x(self):
        return (self.xi+self.xf)/2
        
    @property
    def y(self):
        return (self.yi+self.yf)/2
        
    @property
    def dx(self):
        return (self.xf-self.xi)
        
    @property
    def dy(self):
        return (self.yf-self.yi)
        
    def __init__(self, game, gid, xi, xf, yi, yf):
        super().__init__(game, gid)
        self.kind = 'wall'
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        
        self.collision_mask.add(1)
        self.collision_mask.add(2)
        
        self.zorder = 1
        
        self.colour = (0,0,0,255)

        self.sprite = pygame.Surface((self.dx,self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        
        self.is_drawing = True
        
    def draw(self):
        x = self.xi - self.game.camera.x + self.game.display.w/2
        y = self.yi - self.game.camera.y + self.game.display.h/2
        self.game.display.blit(self.sprite, (x, y))
        
