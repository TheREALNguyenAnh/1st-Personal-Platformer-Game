import pygame
import os

class Terrain(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load the terrain sprite sheet
        sprite_sheet = pygame.image.load(os.path.join("assets", "Terrain", "Terrain (16x16).png")).convert_alpha()
        
        # Extract the specific tile (third column, first row)
        tile_width, tile_height = 48, 48
        column, row = 2, 0  # 0-based indexing
        self.image = sprite_sheet.subsurface(pygame.Rect(column * tile_width, row * tile_height, tile_width, tile_height))
        
        # Scale up the tile to make it more prominent if needed
        scale_factor = 1  # Adjust the scale factor as required
        self.image = pygame.transform.scale(self.image, (tile_width * scale_factor, tile_height * scale_factor))
        
        # Set the position of the block
        self.rect = self.image.get_rect(topleft=(x, y))
