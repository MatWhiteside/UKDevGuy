import pygame

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
    game_window.fill((255,255,255))

    # Update our display
    pygame.display.update()
    

# Uninitialize all pygame modules and quit the program
pygame.quit()
quit()








