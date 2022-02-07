class Entity:
    def __init__(self, game, gid):
        self.kind = 'entity'
        self.game = game
        self.gid = gid
        self.tags = set()
        self.collision_mask = set()
        self.collision_type = 'rect'
        self.is_updating = False
        self.is_drawing = False
        self.should_delete = False
        self.zorder = 0
        
    def draw(self):
        pass
    
    def update(self):
        pass
        
    def check_for_collision(self):
        collision = {}
    
        colliders = [
            v for v in self.game.entity_manager.entities.values()
            if (
                v.gid != self.gid and
                any(i in v.collision_mask for i in self.collision_mask)
            )
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
                    dx = -mindx
                    dy = 0
                else:
                    dx = 0
                    dy = -mindy
                    
                collision[v.gid] = {
                    'gid': v.gid, 'dx': dx, 'dy': dy, 'dr': dx*dx+dy*dy
                }
                
        return collision
        
    def min_dr(self, v):
        return v['dr']
