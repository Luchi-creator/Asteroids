import pygame
from constants import *
from player import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
        
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

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

        pygame.display.flip()


if __name__ == "__main__":
    main()
