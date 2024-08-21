# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Base pygame stuff
    pygame.init() 
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill((0,0,0))

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Objects
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    af = AsteroidField()

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)

        # Update
        [sprite.update(dt) for sprite in updatable]
        # Collisions
        # Player
        for asteroid in asteroids:
            if player.collided(asteroid):
                print("Game Over!")
                exit(1)
        # bullets and asteroids
        [(asteroid.split(),shot.kill()) for asteroid in asteroids for shot in shots if shot.collided(asteroid)]
        # Render
        [sprite.draw(screen) for sprite in drawable]
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__=='__main__':
    main()
