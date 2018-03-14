import pygame, random, math
import settings as st


class Particle:
    def __init__(self, x, y, firework, color):
        self.pos = pygame.math.Vector2(x, y)
        self.firework = firework
        self.lifespan = 0.5
        self.color = color;
        if self.firework:
            self.vel = pygame.math.Vector2(0, -random.randint(14, 20))
        else:
            self.vel = pygame.math.Vector2(random.randint(-4, 4), random.randint(-4, 4))
            self.vel *= random.randint(2, 6)

        self.acc = pygame.math.Vector2(0, 0)

    def applyForce(self, force):
        self.acc += force

    def update(self):
        if not self.firework:
            self.vel *= 0.9

        self.vel += self.acc

        self.pos += self.vel

        self.acc *= 0

    def done(self):
        return self.lifespan > 2.5

    def show(self, window):
        if self.firework:
            pygame.draw.circle(window, self.color, (int(self.pos.x), int(self.pos.y)), 3)
        elif self.lifespan <= 2.5:
            pygame.draw.circle(window, self.color, (int(self.pos.x), int(self.pos.y)), round(2.5 - self.lifespan))
            self.lifespan += 0.025

