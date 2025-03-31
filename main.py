import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    asteroid_Field = AsteroidField()

    Shot.containers = (shots,updatable,drawable)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        screen.fill((0,0,0))

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print(f"Collision detected! Player at {player.position}, Asteroid at {asteroid.position}")
                print("Game Over!")
                exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()