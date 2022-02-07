from main.entities.entity import Entity
import pygame

class Warrior(Entity):
    @property
    def xi(self):
        return self.x-self.dx/2
        
    @property
    def xf(self):
        return self.x+self.dx/2
        
    @property
    def yi(self):
        return self.y-self.dy/2
        
    @property
    def yf(self):
        return self.y+self.dy/2

    def __init__(self, game, gid, x, y):
        super().__init__(game, gid)
        self.kind = 'warrior'
        self.x = x
        self.y = y
        self.dx = 30
        self.dy = 30

        self.zorder = 0
        self.collision_mask.add(1)
        self.collision_mask.add(3)
        
        self.colour = (0,155, 0, 255)
        
        self.sprite = pygame.Surface((self.dx,self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        self.name = self.game.font.render('Tomate')
        self.name_size = self.name.get_size()
        
        self.is_updating = True
        self.is_drawing = True
        
    def draw(self):
        x = self.x-self.dx/2 - self.game.camera.x + self.game.display.w/2
        y = self.y-self.dy/2 - self.game.camera.y + self.game.display.h/2
        self.game.display.blit(self.sprite, (x, y))
        self.game.display.blit(self.name, (x-self.name_size[0]/2+self.dx/2, y-20))
        
        
    def update(self):
        self.x -= 1

        collisions = self.check_for_collision()
        collision = (
            collisions and
            sorted(collisions.values(), key=self.min_dr, reverse=True)[0]
        )
        if collision:
            self.x += collision['dx']
            self.y += collision['dy']
