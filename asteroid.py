from logger import log_event
from random import uniform
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def split(self, asteroid):
        asteroid.kill()
        if asteroid.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        new_asteroid1_velocity = self.velocity.rotate(angle)
        new_asteroid2_velocity = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid1.velocity = new_asteroid1_velocity * 1.2
        new_asteroid2.velocity = new_asteroid2_velocity * 1.2

