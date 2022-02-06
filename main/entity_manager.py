import random
import main.entities as ents

class EntityManager:
    def __init__(self, game):
        self.game = game
        self.entities = {}
        self.max_entities = 65536
        
    def gen_id(self):
        id_ = random.randint(0,self.max_entities)
        while id_ in self.entities:
            id_ = random.randint(0,self.max_entities)
        return id_
        
    def create_entity(self, obj, *args, **kwargs):
        id_ = self.gen_id()
        if isinstance(obj, str):
            obj = ents.from_to.get(obj)
        ent = obj(self.game, id_, *args, **kwargs)
        self.entities[id_] = ent
        return ent
    
    def delete_entity(self, id_, *args, **kwargs):
        ent = self.entities.pop(id_)
        if hasattr(ent, 'on_delete') and ent.on_delete:
            ent.on_delete(*args, **kwargs)
            
            
    def update(self):
        keys = list(self.entities.keys())
        for k in keys:
            ent = self.entities[k]
            if hasattr(ent, 'is_updating') and ent.is_updating:
                ent.update()
                
            if hasattr(ent, 'should_delete') and ent.should_delete:
                self.delete_entity(ent)
