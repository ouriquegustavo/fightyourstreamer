import json
import pygame
from main.display import Display
from main.clock import Clock
from main.entity_manager import EntityManager
from main.viewers import Viewers
from main.camera import Camera
from main.controls import Controls
from main.font import Font
from main.auth import Auth
from main.map_loader import MapLoader


class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.tps = 60
        self.tick = 0

    def run(self):
        self.is_running = True
        self.auth = Auth(self)
        self.clock = Clock(self, self.tps)
        self.display = Display(self, self.width, self.height)
        self.entity_manager = EntityManager(self)
        self.camera = Camera(self)
        self.controls = Controls(self)
        self.viewers = Viewers(self)
        self.font = Font(self)
        self.map_loader = MapLoader(self)

        self.map_loader.load('main')

        self.camera.x = -1366/2
        self.camera.y = 0

        self.player = self.entity_manager.create_entity('player', -1000, 0)

        self.viewers.start()
        
        self.interval = 15

        while self.is_running:
            self.tick += 1
            self.clock.tick()

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_ESCAPE
                ):
                    self.is_running = False

            self.player.is_updating = True
            self.viewers.is_updating = True
                    
            if self.tick <= 60*60:
                self.player.is_updating = False
                
            if self.tick <= 1366/6:
                self.camera.x += 6
                
            if (
                self.tick > self.interval*self.tps and 
                self.tick <= self.interval*self.tps+1366/6
            ):
                self.camera.x -= 6
            if self.tick >= self.interval*self.tps+1366/6:
                self.player.is_updating = True
            
            if self.tick == int(self.interval*self.tps+1366/6):
                for k, v in self.entity_manager.entities.items():
                    if v.kind == 'warrior':
                        v.is_updating = True
                        
            if self.tick <= 1366/6 or self.tick >= self.interval*self.tps:
                self.viewers.is_updating = False

            self.controls.get_keys()
            
            self.viewers.update()
            self.entity_manager.update()
            self.display.update()
