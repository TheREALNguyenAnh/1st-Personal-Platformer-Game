import pygame
from levels.level_loader import load_level_from_2d_list  # Import the level loader

def level_two(screen):
    clock = pygame.time.Clock()

    # Level data for level_two
    level_data = [
        "TTTTTTTTTTTTTTTTTTTTTTTTTTT",  # Row 0
        "T.........................T",  # Row 1
        "T.........................T",  # Row 2
        "T.........................T",  # Row 3
        "T.........................T",  # Row 4
        "T.........................T",  # Row 5
        "T.........................T",  # Row 6
        "T.........................T",  # Row 7
        "T.........................T",  # Row 8
        "T........TTT..............T",  # Row 9
        "T........TTT..............T",  # Row 10
        "T........TTT..............T",  # Row 11
        "T.........................T",  # Row 12
        "T.................P......ET",  # Row 13
        "TTTTTTTTTTTTTTTTTTTTTTTTTTT",  # Row 14
    ]
    # Load the level using the shared function
    terrain_group, end_point_group, all_sprites, player = load_level_from_2d_list(level_data)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((100, 149, 237))  # Cornflower blue background

        # Update player and check for level transition
        player.update(terrain_group)
        if pygame.sprite.spritecollideany(player, end_point_group):
            print("End of level two!")  # Placeholder action for reaching the endpoint

        # Draw all entities
        all_sprites.draw(screen)

        # Update the display
        pygame.display.update()
        clock.tick(60)
