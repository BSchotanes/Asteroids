import pygame
from circleshape import CircleShape
from constants import *

# Base class for game objects
class Shot(CircleShape):
    def __init__(self, x, y):
       super().__init__(x,y,SHOT_RADIUS)
       self.velocity = pygame.Vector2(0,0) 

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,SHOT_RADIUS)

    def update(self, dt):
        self.position +=  self.velocity * dt
