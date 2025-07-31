import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable,drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots,updatable,drawable)
        
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000
        screen.fill("black")
        # player.draw(screen)
        # player.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)

        for i in asteroids:
            if i.check_collisions(player):
                print("Game Over!")
                sys.exit(1)

        pygame.display.flip()


if __name__ == "__main__":
    main()
