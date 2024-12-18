import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load animations
        self.animations = {
            "run": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Run (32x32).png"], frame_width=32, frame_height=32, num_frames=12, scale_factor=2),
            "jump": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Jump (32x32).png"], frame_width=32, frame_height=32, num_frames=1, scale_factor=2),
            "idle": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Idle (32x32).png"], frame_width=32, frame_height=32, num_frames=11, scale_factor=2),
        }

        # Set up initial animation
        self.current_animation = "idle"
        self.current_frame = 0
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_speed = 0.2
        self.animation_timer = 0

        # Movement and physics
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.5
        self.jump_power = 100
        self.is_jumping = False
        self.is_running = False

    def load_animation(self, pathlist, frame_width, frame_height, num_frames, scale_factor=2):
        """Load animation frames from a sprite sheet and scale them."""
        sprite_sheet = pygame.image.load(os.path.join(*pathlist)).convert_alpha()
        frames = []
        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            scaled_frame = pygame.transform.scale(frame, (frame_width * scale_factor, frame_height * scale_factor))
            frames.append(scaled_frame)
        return frames

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0  # Reset horizontal velocity
        self.is_running = False  # Default to not running unless moving

        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
            self.is_running = True
        if keys[pygame.K_d]:
            self.velocity.x = self.speed
            self.is_running = True
        if keys[pygame.K_w] and not self.is_jumping:
            self.velocity.y = self.jump_power
            self.is_jumping = True

    def apply_gravity(self):
        self.velocity.y += self.gravity
        if self.rect.bottom >= 720:  # Assuming the ground is at the bottom of the screen
            self.rect.bottom = 720
            self.velocity.y = 0
            self.is_jumping = False

    def animate(self):
        # Determine the current animation based on the player's state
        if self.is_jumping:
            self.current_animation = "jump"
        elif self.is_running:
            self.current_animation = "run"
        else:
            self.current_animation = "idle"

        # Update the animation frame
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
        self.image = self.animations[self.current_animation][self.current_frame]

    def update(self):
        self.handle_keys()
        self.apply_gravity()
        self.animate()
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
