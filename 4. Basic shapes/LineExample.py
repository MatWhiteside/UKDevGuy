import pygame
import sys

# Create width and height constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("UKDevGuy tutorial")

game_running = True

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    # Content here
    # Clear screen
    game_window.fill((255,255,255))
    # Draw a line
    pygame.draw.line(game_window, (255,0,0), (100, 100), (300, 200), 5)
    # Update our display
    pygame.display.update()
    

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()








