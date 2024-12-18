import pygame
import os
import sys
from ui.menu import main_menu
#from levels.level_one import level_one

# Initialize Pygame
pygame.init()

# Set Window Icon
# icon_path = os.path.join("assets", "logo32x32.png")
# icon = pygame.image.load(icon_path)
# ygame.display.set_icon(icon)

# Set the screen dimensions and caption
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Puzzle Platformer")

# Define desired frames per second (FPS)
FPS = 120  # You can adjust this value to increase/decrease frame rate

def main():
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    # Main game loop
    while True:
        
        #currentTimeInGame = gameTimer.getCurrentTime()
        #print(f"Elapsed Time: {currentTimeInGame:.2f} seconds")
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Uncomment the menu if you want to use it
        main_menu(SCREEN)
        #level_one(SCREEN)

        pygame.display.update()  # Update the display

        # Cap the frame rate
        clock.tick(FPS)  # This will set the frame rate to the specified FPS

if __name__ == "__main__":
    main()
