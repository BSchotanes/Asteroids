import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.player_shoot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.player_shoot_cooldown -= dt
        
    def shoot(self):
        if self.player_shoot_cooldown <= 0:

            temp_Shot = Shot(self.position.x,self.position.y)

            temp_velocity = pygame.Vector2(0,1).rotate(self.rotation)
            temp_velocity *= PLAYER_SHOT_SPEED

            temp_Shot.velocity = temp_velocity
            self.player_shoot_cooldown += 0.3