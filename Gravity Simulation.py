import pygame
import sys

# Constants
WIDTH, HEIGHT = 640, 480
GRAVITY = 1.0  # Adjustable gravity force
FRICTION = 0.3  # Adjustable friction multiplier

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.movex = 2  # Adjustable initial velocity
        self.movey = 2

    def gravity(self):
        self.movey += GRAVITY

        if self.rect.y > HEIGHT - self.rect.height and self.movey >= 0:
            self.movey = 0
            self.rect.y = HEIGHT - self.rect.height

    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

        # Apply friction
        self.movex *= FRICTION
        self.movey *= FRICTION

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Simulation")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.gravity()
        all_sprites.update()

        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(70)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()