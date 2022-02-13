from main.maps.map_base import MapBase

class MapMain(MapBase):
    def __init__(self, game):
        super().__init__(game)

        self.create_entity(
            'wall', -1366, -1366 + 30, -768 / 2, 768 / 2
        )
        self.create_entity(
            'wall', 1366 - 30, 1366, -768 / 2, 768 / 2
        )
        self.create_entity(
            'wall', -1366, 1366, -768 / 2, -768 / 2 + 30
        )
        self.create_entity(
            'wall', -1366, 1366, 768 / 2 - 30, 768 / 2
        )
