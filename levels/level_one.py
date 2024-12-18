import pygame
from entities.player import Player
from entities.terrain import Terrain

def level_one(screen):
    clock = pygame.time.Clock()
    terrain_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Create terrain blocks
    for i in range(10):  # A line of blocks
        terrain_block = Terrain(x=i * 64, y=600)  # Adjust block positions as needed
        terrain_group.add(terrain_block)
        all_sprites.add(terrain_block)

    # Create the player
    player = Player(x=100, y=500)
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((135, 206, 235))  # Light blue background color

        # Update player and terrain
        player.update(terrain_group)
        all_sprites.draw(screen)

        # Update the display
        pygame.display.update()
        clock.tick(60)
