# 
# In this assignment we're going to use a python library called pygame to draw! 
# I've added some started code below to help you out. Use the draw functions from the pygame
# library to code your art! You can find all of it in the link below.
# https://www.pygame.org/docs/ref/draw.html
# 
# -------------------------------------------------------------------------------------------



import pygame

# Initialize Pygame
pygame.init()

# Set up the window dimensions
window_width = 800
window_height = 600

# Create the Pygame window
window = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("My Pygame Window")

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((255, 255, 255))  # Fill the window with white color

    # Draw shapes here!
    pygame.draw.rect(window, (255, 255, 0), (40, 40, 40, 40))









    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()