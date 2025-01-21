import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load animations
        self.animations = {
            "run": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Run (32x32).png"], frame_width=32, frame_height=32, num_frames=12),
            "jump": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Jump (32x32).png"], frame_width=32, frame_height=32, num_frames=1),
            "idle": self.load_animation(["assets", "Main Characters", "Ninja Frog", "Idle (32x32).png"], frame_width=32, frame_height=32, num_frames=11),
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
        self.jump_power = -15  # Use negative for upward jump
        self.is_jumping = False
        self.is_running = False

        # Facing direction
        self.facing_right = True

    def load_animation(self, pathlist, frame_width, frame_height, num_frames, scale_factor=1.5):
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
            self.facing_right = False
        if keys[pygame.K_d]:
            self.velocity.x = self.speed
            self.is_running = True
            self.facing_right = True
        if keys[pygame.K_w] and not self.is_jumping:
            self.velocity.y = self.jump_power
            self.is_jumping = True

    def apply_gravity(self):
        self.velocity.y += self.gravity

    def handle_collision(self, terrain_group):
        """Handle collisions with terrain."""
        # Check horizontal collisions
        self.rect.x += self.velocity.x
        for block in terrain_group:
            if self.rect.colliderect(block.rect):
                if self.velocity.x > 0:  # Moving right
                    self.rect.right = block.rect.left
                elif self.velocity.x < 0:  # Moving left
                    self.rect.left = block.rect.right
                self.velocity.x = 0

        # Check vertical collisions
        self.rect.y += self.velocity.y
        for block in terrain_group:
            if self.rect.colliderect(block.rect):
                if self.velocity.y > 0:  # Falling
                    self.rect.bottom = block.rect.top
                    self.velocity.y = 0
                    self.is_jumping = False
                elif self.velocity.y < 0:  # Jumping
                    self.rect.top = block.rect.bottom
                    self.velocity.y = 0

    def animate(self):
        # Determine the current animation based on the player's state
        previous_animation = self.current_animation

        if self.is_jumping:
            self.current_animation = "jump"
        elif self.is_running:
            self.current_animation = "run"
        else:
            self.current_animation = "idle"

        # Reset frame index if the animation changes
        if self.current_animation != previous_animation:
            self.current_frame = 0

        # Update the animation frame
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])

        # Get the current frame and flip it if necessary
        self.image = self.animations[self.current_animation][self.current_frame]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            
    def update(self, terrain_group):
        self.handle_keys()
        self.apply_gravity()
        self.handle_collision(terrain_group)
        self.animate()