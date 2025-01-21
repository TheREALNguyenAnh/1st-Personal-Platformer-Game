import pygame
from entities.terrain import Terrain
from entities.end_point import EndPoint
from entities.player import Player

def load_level_from_2d_list(level_data):
    """Loads a level from a 2D list."""
    terrain_group = pygame.sprite.Group()
    end_point_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player = None

    tile_size = 48  # Size of each terrain block
    for row_index, row in enumerate(level_data):
        for col_index, cell in enumerate(row):
            x, y = col_index * tile_size, row_index * tile_size

            if cell == 'T':  # Terrain block
                terrain_block = Terrain(x, y)
                terrain_group.add(terrain_block)
                all_sprites.add(terrain_block)

            elif cell == 'E':  # EndPoint
                end_point = EndPoint(x, y)
                end_point_group.add(end_point)
                all_sprites.add(end_point)

            elif cell == 'P' and player is None:  # Player spawn
                player = Player(x, y)
                all_sprites.add(player)

    return terrain_group, end_point_group, all_sprites, player
