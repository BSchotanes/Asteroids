import pygame
import random
from circleshape import CircleShape
from constants import *

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,2.0)

    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()

        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        temp_random_angle = random.uniform(20,50)
            
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #create asteroid 1
        random_angle_1 = self.velocity.rotate(temp_random_angle)
        new_asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_1.velocity = random_angle_1*1.2
            
        #create asteroid 2
        random_angle_2 = self.velocity.rotate(-temp_random_angle)
        new_asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_2.velocity = random_angle_2*1.2