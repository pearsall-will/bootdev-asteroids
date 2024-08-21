import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (self.velocity * 1.2).rotate(random.uniform(20,50))
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (self.velocity * 1.2).rotate(-random.uniform(20,50))
      