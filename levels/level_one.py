import pygame
from levels.level_two import level_two
from levels.level_loader import load_level_from_2d_list  


def level_one(screen):
    clock = pygame.time.Clock()

    # Level data represented as a 2D list
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
        "T.........................T",  # Row 9
        "T.........................T",  # Row 10
        "T........TTT..............T",  # Row 11
        "T..P......................T",  # Row 12
        "T......................E..T",  # Row 13
        "TTTTTTTTTTTTTTTTTTTTTTTTTTT",  # Row 14
    ]
    # Convert level data into game entities
    terrain_group, end_point_group, all_sprites, player = load_level_from_2d_list(level_data)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((135, 206, 235))  # Light blue background color

        # Update player and check for level transition
        player.update(terrain_group)
        if pygame.sprite.spritecollideany(player, end_point_group):
            level_two(screen)  # Transition to level_two

        # Draw all entities
        all_sprites.draw(screen)

        # Update the display
        pygame.display.update()
        clock.tick(60)
