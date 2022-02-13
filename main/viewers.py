import threading
from pywitch import PyWitchHeat


class Viewers:
    def __init__(self, game):
        self.game = game
        self.warriors = 0
        self.warriors_max = 20
        self.users = {}
        self.clicks = {}
        self.channel = 'gleenus'
        self.is_updating = True

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(
            target=self.viewers_thread, args=(), daemon=True
        )
        self.thread.start()

    def stop(self):
        self.is_running = False

    def clear(self):
        self.clicks = {}

    def callback(self, data):
        if not self.is_updating or self.warriors > self.warriors_max:
            return
        display_name = data.get('display_name')
        if not display_name:
            return
        x = (data['x'] - 0.5) * self.game.display.w + self.game.camera.x
        y = (data['y'] - 0.5) * self.game.display.h + self.game.camera.y
        self.clicks[data['user_id']] = {
            'x': x,
            'y': y,
            'display_name': display_name,
        }
        self.warriors += 1
        
    def update(self):
        for k, v in self.clicks.items():
            gid = self.game.entity_manager.create_entity(
                'warrior', v['x'], v['y'], v['display_name']
            )
            self.game.entity_manager.entities[gid].is_updating = False
        self.clicks.clear()

    def viewers_thread(self):
        self.heat = PyWitchHeat(
            channel=self.channel,
            token=self.game.auth.token,
            callback=self.callback,
            users=self.users,
            verbose=True,
        )
        self.heat.start()
        """
        import pygame
        clock = pygame.time.Clock()
        while self.is_running:
            clock.tick(10)
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                tid = 'gleenus'
                pos = pygame.mouse.get_pos()
                dpos = {
                    'x': pos[0]-self.game.display.w/2,
                    'y': pos[1]-self.game.display.h/2
                }
                if not tid in self.viewers:
                    self.viewers[tid] = True
                self.clicks[tid] = dpos
        """
