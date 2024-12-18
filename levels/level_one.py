import pygame
import sys
from entities.player import Player

def level_one(SCREEN):
    clock = pygame.time.Clock()
    FPS = 60

    # Create a group to manage all sprites
    all_sprites = pygame.sprite.Group()

    # Create a player instance
    player = Player(100, 600)
    all_sprites.add(player)

    # Main loop for level one
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update all sprites
        all_sprites.update()

        # Draw everything
        SCREEN.fill((135, 206, 235))  # Sky blue background
        all_sprites.draw(SCREEN)

        # Update display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(FPS)
