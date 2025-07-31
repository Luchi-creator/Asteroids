from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"brown",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_direction_one = self.velocity.rotate(angle)
            new_direction_two = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid_two = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid_one.velocity = new_direction_one * 1.2
            asteroid_two.velocity = new_direction_two * 1.2