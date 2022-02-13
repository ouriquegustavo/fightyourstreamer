class MapBase:
    def __init__(self, game):
        self.game = game
        self.game.entity_manager.clear()
        
    def create_entity(self, obj, *args, **kwargs):
        return self.game.entity_manager.create_entity(obj, *args, **kwargs)
