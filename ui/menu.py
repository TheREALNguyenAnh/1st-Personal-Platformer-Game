import pygame
from ui.button import Button
from levels.level_one import level_one
import sys

# Function to get the font for text
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Main menu function
def main_menu(SCREEN):
    # Set the background
    BG = pygame.image.load("assets/menuBACKGROUND.png")

    # Clear the screen and draw the background
    SCREEN.blit(BG, (0, 0))

    # Get mouse position (if needed for buttons)
    mouseMenuPOS = pygame.mouse.get_pos()

    # Render the main menu text
    menuTEXT = get_font(75).render("Game Project", True, "#b68f40")
    menuSHAPE = menuTEXT.get_rect(center=(640, 100))

    PLAY_BUTTON = Button(image=pygame.image.load("assets/EmptyButton.png"), pos=(640, 250), text_input="PLAY GAME", font=get_font(75), base_color= "#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/EmptyButton.png"), pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color="#d6fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/EmptyButton.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
    # Draw the text on the screen
    SCREEN.blit(menuTEXT, menuSHAPE)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(mouseMenuPOS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(mouseMenuPOS):
                level_one(SCREEN)
            if OPTIONS_BUTTON.checkForInput(mouseMenuPOS):
                print("Options button clicked!")  # Replace with options screen
            elif QUIT_BUTTON.checkForInput(mouseMenuPOS):
                pygame.quit()
                sys.exit()
    
    # Update the display
    pygame.display.update()
