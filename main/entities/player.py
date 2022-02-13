from main.entities.entity import Entity
import pygame


class Player(Entity):
    @property
    def xi(self):
        return self.x - self.dx / 2

    @property
    def xf(self):
        return self.x + self.dx / 2

    @property
    def yi(self):
        return self.y - self.dy / 2

    @property
    def yf(self):
        return self.y + self.dy / 2

    def __init__(self, game, gid, x, y):
        super().__init__(game, gid)
        self.kind = 'player'
        self.x = x
        self.y = y
        self.dx = 30
        self.dy = 30

        self.zorder = 0
        self.collision_mask.add(2)

        self.colour = (200, 0, 0, 255)

        self.sprite = pygame.Surface((self.dx, self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)

        self.is_updating = True
        self.is_drawing = True

        self.attack_delay = 20
        self.attack_current = 0

    def draw(self):
        x = self.x - self.dx / 2 - self.game.camera.x + self.game.display.w / 2
        y = self.y - self.dy / 2 - self.game.camera.y + self.game.display.h / 2
        self.game.display.blit(self.sprite, (x, y))

    def update(self):
        self.x += 5 * (
            self.game.controls.c['right'] - self.game.controls.c['left']
        )
        self.y += 5 * (
            self.game.controls.c['up'] - self.game.controls.c['down']
        )

        if self.attack_current > 0:
            self.attack_current -= 1

        if self.game.controls.c['attack'] and self.attack_current <= 0:
            self.attack_current = self.attack_delay
            self.game.entity_manager.create_entity(
                'projectile', self.x, self.y, 5, 0
            )

        collisions = self.check_for_collision()
        collision = (
            collisions
            and sorted(collisions.values(), key=self.min_dr, reverse=True)[0]
        )
        if collision:
            self.x += collision['dx']
            self.y += collision['dy']
