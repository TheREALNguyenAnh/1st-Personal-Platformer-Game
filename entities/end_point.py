import pygame
import os

class EndPoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "Items", "Checkpoints",  "End", "End (Idle).png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))  # Scale to match tile size
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass  # Placeholder if you need specific updates for the endpoint
