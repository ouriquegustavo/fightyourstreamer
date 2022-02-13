import random
import main.entities as ents


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.entities = {}
        self.max_entities = 65536

    def gen_id(self):
        gid = random.randint(0, self.max_entities)
        while gid in self.entities:
            gid = random.randint(0, self.max_entities)
        return gid

    def create_entity(self, obj, *args, **kwargs):
        gid = self.gen_id()
        if isinstance(obj, str):
            obj = ents.from_to.get(obj)
        ent = obj(self.game, gid, *args, **kwargs)
        self.entities[gid] = ent
        return ent

    def delete_entity(self, gid, on_delete=True, *args, **kwargs):
        ent = self.entities.pop(gid)
        if hasattr(ent, 'on_delete') and ent.on_delete and on_delete:
            ent.on_delete(*args, **kwargs)
            
    def clear(self):
        keys = list(self.entities.keys())
        for k in keys:
            self.delete_entity(k, False)
        self.entities = {}

    def update(self):
        keys = list(self.entities.keys())
        for k in keys:
            ent = self.entities[k]
            if hasattr(ent, 'should_delete') and ent.should_delete:
                self.delete_entity(k)

        keys = list(self.entities.keys())
        for k in keys:
            ent = self.entities[k]
            if hasattr(ent, 'is_updating') and ent.is_updating:
                ent.update()
