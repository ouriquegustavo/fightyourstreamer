from main.maps.map_main import MapMain

class MapLoader:
    def __init__(self, game):
        self.game = game
        
        self.map = None
        
        self.map_dict = {
            'main': MapMain
        }
    
    def load(self, map_name):
        self.destroy()
        self.map = self.map_dict[map_name](self.game)
        return self.map
        
    def destroy(self):
        self.game.entity_manager.clear()
        if self.map:
            del self.map
