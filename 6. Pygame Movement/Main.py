import pygame
import sys

# Create width and height constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Player size
RECT_WIDTH = 100
RECT_HEIGHT = 100

# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("UKDevGuy movement tutorial")

# Get clock
clock = pygame.time.Clock()

# Start player in centre of screen
x_pos = WINDOW_WIDTH / 2 - RECT_WIDTH / 2
y_pos = WINDOW_HEIGHT / 2 - RECT_HEIGHT / 2

# Player velocity
x_vel = 0
y_vel = 0

game_running = True

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False
        # Process movement events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_vel += 5
            if event.key == pygame.K_LEFT:
                x_vel -= 5
            if event.key == pygame.K_UP:
                y_vel -= 5
            if event.key == pygame.K_DOWN:
                y_vel += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_vel -= 5
            if event.key == pygame.K_LEFT:
                x_vel += 5
            if event.key == pygame.K_UP:
                y_vel += 5
            if event.key == pygame.K_DOWN:
                y_vel -= 5

    # Clear window with white background
    game_window.fill((255, 255, 255))

    # Update rect position
    x_pos += x_vel
    y_pos += y_vel

    # Draw new rect on the screen
    rect = pygame.Rect(x_pos, y_pos, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(game_window, (255, 0, 0), rect)

    # Update our display
    pygame.display.update()

    # Limit FPS to 60
    clock.tick(60)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()








