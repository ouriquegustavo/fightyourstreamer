import pygame 

class Collider:
    def __init__(self, game, gid, xi, yi, xf, yf):
        self.kind = 'collider'
        self.game = game
        self.gid = gid
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.dx = self.xf-self.xi
        self.dy = self.yf-self.yi
        
        self.zorder = 1
        
        self.colour = (0,0,0,255)

        self.sprite = pygame.Surface((self.dx,self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        
        self.is_drawing = True
        
    def draw(self):
        x = self.xi - self.game.camera.x + self.game.display.w/2
        y = self.yi - self.game.camera.y + self.game.display.h/2
        print(x, y)
        self.game.display.blit(self.sprite, (x, y))
        
