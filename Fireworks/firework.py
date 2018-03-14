import pygame
import random
import Particle
import settings as st

class Firework:
    def __init__(self):
        self.gravity = pygame.math.Vector2(0, 0.2)
        self.color = st.getRandomColor()
        self.firework = Particle.Particle(random.randint(1, st.WIDTH), st.HEIGHT, True, self.color)
        self.exploded = False
        self.particles = []

    def done(self):
        if self.exploded and self.particles.__len__() == 0:
            return True
        else:
            return False

    def update(self):
        if not self.exploded:
            self.firework.applyForce(self.gravity)
            self.firework.update()
            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()

        for i in range(self.particles.__len__() - 1, - 1, -1):
            self.particles[i].applyForce(self.gravity)
            self.particles[i].update()
            if self.particles[i].done():
                del self.particles[i:i + 1]


    def explode(self):
        for i in range(1, 100):
            p = Particle.Particle(self.firework.pos.x, self.firework.pos.y, False, self.color)
            self.particles.append(p);

    def show(self, window):
        if not self.exploded:
            self.firework.show(window)
        for i in self.particles:
            i.show(window)