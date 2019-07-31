import pygame
import sys

# Create width and height constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("Text example")

# TrueType fonts
font1 = pygame.font.Font('Roboto-Bold.ttf', 60)
text1 = font1.render('Roboto | Size: 60 | Bold', True, (0, 0, 0))

font2 = pygame.font.Font('Lacquer-Regular.ttf', 36)
text2 = font2.render('Lacquer | Size: 36 | Colour: Red | Background: none', True, (255, 0, 0))

# System fonts
font3 = pygame.font.SysFont('Bauhaus 93', 36)
text3 = font3.render('Bauhaus 93 | Size: 36 | Colour: White | Background: Blue', True, (255, 255, 255), (0, 0, 255))

font4 = pygame.font.SysFont('Lucida Handwriting', 36, italic=True)
text4 = font4.render('Lucida Handwriting | Size: 36 | Italic', True, (0, 0, 0))

font5 = pygame.font.SysFont('OCR A Extended', 18, True, True)
text5 = font5.render('OCR A Extended | Size: 18 | Bold | Italic | Colour: Green | Background: Purple', True, (0, 255, 0), (100, 100, 255))

font6 = pygame.font.SysFont('Parchment', 60)
text6 = font6.render('Parchment | Size: 60 ', True, (0, 0, 0))

clock = pygame.time.Clock()

game_running = True

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    # Fill the window with white
    game_window.fill((255, 255, 255))

    # Draw text
    game_window.blit(text1, (0, 0))
    game_window.blit(text2, (0, 100))
    game_window.blit(text3, (0, 200))
    game_window.blit(text4, (0, 300))
    game_window.blit(text5, (0, 400))
    game_window.blit(text6, (0, 500))

    # Update our display
    pygame.display.update()

    clock.tick(60)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()
