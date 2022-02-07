from main.entities.entity import Entity
import pygame


class Projectile(Entity):
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

    def __init__(self, game, gid, x, y, vx, vy):
        super().__init__(game, gid)
        self.kind = 'projectile'
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 5
        self.vx = vx
        self.vy = vy

        self.zorder = 0
        self.collision_mask.add(3)
        self.collision_mask.add(1)
        
        self.colour = (255,0, 155, 255)
        
        self.sprite = pygame.Surface((self.dx,self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        
        self.is_updating = True
        self.is_drawing = True
        
    def draw(self):
        x = self.x-self.dx/2 - self.game.camera.x + self.game.display.w/2
        y = self.y-self.dy/2 - self.game.camera.y + self.game.display.h/2
        self.game.display.blit(self.sprite, (x, y))
        
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        collisions = self.check_for_collision()
        col = (
            collisions and
            sorted(collisions.values(), key=self.min_dr, reverse=True)[0]
        )
        if col:
            self.should_delete = True
            ent = self.game.entity_manager.entities[col['gid']]
            if ent.kind == 'warrior':
                ent.should_delete = True
