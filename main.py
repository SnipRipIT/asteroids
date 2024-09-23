import pygame
import constants as c
import circleshape as cs
import player as p

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    p.Player.containers = (updatable, drawable)
    player = p.Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        dt = clock.tick(60) / 1000
        screen.fill("black")
        pygame.display.flip()

        for entity in updatable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(screen)
            


if __name__ == "__main__":
    main()