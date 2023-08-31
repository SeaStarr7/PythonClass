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
window_width = 1000
window_height = 800

# Create the Pygame window
window = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("My Pygame Window")
x = 40
y = 40
width = 100
height = 100
vel = 5


# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x  -= vel
    if keys[pygame.K_DOWN] and y < window_height - height:
        y += vel
    if keys[pygame.K_RIGHT] and x < window_width - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
        
        
    # Clear the window
    window.fill((255, 255, 255))  # Fill the window with white color

    

    # Draw shapes here!
    pygame.draw.polygon(window, (255, 171, 0), [(400, 200), (500, 300), (200, 550)])
    pygame.draw.rect(window, (0, 119, 255), (x, y, width, height))










    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()