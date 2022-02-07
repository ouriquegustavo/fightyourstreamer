import pygame
from main.display import Display
from main.clock import Clock
from main.entity_manager import EntityManager
from main.viewers import Viewers
from main.camera import Camera
from main.controls import Controls
from main.font import Font

class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.tps = 60
        
    def run(self):
        self.is_running = True
    
        self.clock = Clock(self, self.tps)
        self.display = Display(self, self.width, self.height)
        self.entity_manager = EntityManager(self)
        self.camera = Camera(self)
        self.controls = Controls(self)
        self.viewers = Viewers(self)
        self.font = Font(self)
        
        self.entity_manager.create_entity('wall', -1366/2, -1366/2+30, -768/2, 768/2)
        self.entity_manager.create_entity('wall', 1366/2-30, 1366/2, -768/2, 768/2)
        self.entity_manager.create_entity('wall', -1366/2, 1366/2, -768/2, -768/2+30)
        self.entity_manager.create_entity('wall', -1366/2, 1366/2, 768/2-30, 768/2)
        
        self.entity_manager.create_entity('player', -300, 0)
        
        self.viewers.start()
        
        while self.is_running:
            self.clock.tick()
            
            self.events = pygame.event.get()
            for event in self.events:
                if (
                    event.type == pygame.QUIT or
                    (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)
                ):
                    self.is_running = False
            
            for k, v in self.viewers.clicks.items():
                self.entity_manager.create_entity('warrior', v['x'], v['y'])
            self.viewers.clicks.clear()
            
            self.controls.get_keys()
            
            self.entity_manager.update()
            self.display.update()
