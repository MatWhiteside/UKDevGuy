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
    # Create and draw a 5-sided, filled polygon
    points = [(150, 150), (200, 120), (210, 150), (260, 140), (210, 250)]
    pygame.draw.polygon(game_window, (0,0,0), points)
    # Create and draw a 4-sided, empty polygon
    points = [(350, 350), (400, 320), (460, 340), (410, 450)]
    pygame.draw.polygon(game_window, (0,0,255), points, 4)
    
    # Update our display
    pygame.display.update()
    

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()








