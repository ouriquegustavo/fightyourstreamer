import threading

class Viewers:
    def __init__(self, game):
        self.game = game
        self.viewers = {}
        self.clicks = {}
        
    def start(self):
        self.is_running = True
        self.thread = threading.Thread(
            target = self.viewers_thread,
            args = (),
            daemon = True
        )
        self.thread.start()
    
    def stop(self):
        self.is_running = False
        
    def clear(self):
        self.clicks = {}
        
    def viewers_thread(self):
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
