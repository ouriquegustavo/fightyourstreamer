from main.display import Display
from main.clock import Clock

class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.tps = 60
        
    def run(self):
        self.clock = Clock(self, self.tps)
        self.display = Display(self, self.width, self.height)
        
        self.display.start()
        
        while True:
            self.clock.tick()
            self.display.update()
            print('tomate')
