import pygame
import sys
import random

# Create width and height constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("UKDevGuy tutorial")

# Set previous point to none
previous_point = None

# Make the game window white
game_window.fill((255,255,255))

""" Function to create a randomly generate colour.
    Returns a 3-tuple of numbers between 0-255. """
def random_colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

""" Function that deals with drawing lines when a left mouse
    click has been made """
def process_click(event):
    global previous_point
    # Get the position clicked on the screen
    click_pos = event.pos
    # If the first point has been set, draw a line from the
    # previous point to current position
    if previous_point != None:
        pygame.draw.line(game_window, random_colour(), previous_point, click_pos, 5)
    # Update previous_point with the click that was just made
    previous_point = click_pos

# Game loop
game_running = True
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False
        # Detect when the delete key is pressed, clear
        # the screen and set previous_point to None
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DELETE:
                game_window.fill((255,255,255))
                previous_point = None
                
        # On left mouse button clicked, draw a line from previous_point to
        # click position if previous_point not equal to `None`. Update
        # previous_point with the click that was just made
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            process_click(event)
            
    # Update our display
    pygame.display.update()
    

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()
