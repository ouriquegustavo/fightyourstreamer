from main.display import Display
from main.clock import Clock
from main.entity_manager import EntityManager
from main.entities import Button

class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.tps = 60
        
    def run(self):
        self.clock = Clock(self, self.tps)
        self.display = Display(self, self.width, self.height)
        self.entity_manager = EntityManager(self)
        
        self.entity_manager.create_entity('button', 100, 100, 10, 10)
        
        while True:
            self.clock.tick()
            self.display.update()
            print('tomate')
