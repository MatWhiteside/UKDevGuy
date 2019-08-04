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
        # Control character movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Move the character forwards")
            elif event.key == pygame.K_s:
                print("Move the character backwards")
            elif event.key == pygame.K_a:
                print("Move the character left")
            elif event.key == pygame.K_d:
                print("Move the character right")

    # Content here

    # Update our display
    pygame.display.update()

# Uninitialize all pygame modules and quit the program
pygame.quit()
quit()
