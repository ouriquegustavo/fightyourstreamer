import pygame

class EWarrior():
    def __init__(self, game, gid, x, y):
        self.kind = 'e_warrior'
        self.game = game
        self.gid = gid
        self.x = x
        self.y = y
        self.dx = 30
        self.dy = 30
        
        self.zorder = 0
        
        self.colour = (0,155, 0, 255)
        
        self.sprite = pygame.Surface((self.dx,self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        
        self.is_updating = True
        self.is_drawing = True
        
    def draw(self):
        x = self.x-self.dx/2 - self.game.camera.x + self.game.display.w/2
        y = self.y-self.dy/2 - self.game.camera.y + self.game.display.h/2
        self.game.display.blit(self.sprite, (x, y))
        
    def check_for_collision(self):
        colliders = [
            v for v in self.game.entity_manager.entities.values()
            if v.kind in ('collider', 'e_warrior')
        ]
        for v in colliders:
            dxi = self.x+self.dx/2 - v.xi
            dxf = self.x-self.dx/2 - v.xf
            dyi = self.y+self.dy/2 - v.yi
            dyf = self.y-self.dy/2 - v.yf
            if (
                dxf < 0 and
                dxi > 0 and
                dyf < 0 and
                dyi > 0 
            ):
                mindx = abs(dxi) < abs(dxf) and dxi or dxf
                mindy = abs(dyi) < abs(dyf) and dyi or dyf
                if abs(mindx) < abs(mindy):
                    self.x -= mindx
                else:
                    self.y -= mindy
        
    def update(self):
        self.x -= 1
        self.check_for_collision()
