import pygame
import random

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sierpinski Curve Chaos Game")
clock = pygame.time.Clock()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the vertices of a triangle
v1 = (400, 100)
v2 = (100, 500)
v3 = (700, 500)

# Draw the triangle on the screen
pygame.draw.polygon(screen, WHITE, [v1,v2,v3])

# Choose a random point inside the triangle as the initial point
x = random.randint(100,700)
y = random.randint(100,500)

# Loop until the user clicks the close button or presses ESC key
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    # Choose one of the vertices randomly
    r = random.randint(1,3)
    if r == 1:
        vx = v1[0]
        vy = v1[1]
    elif r == 2:
        vx = v2[0]
        vy = v2[1]
    else:
        vx = v3[0]
        vy = v3[1]

    # Find the midpoint between the current point and the chosen vertex
    x = (x + vx) // 2
    y = (y + vy) // 2

    # Draw a pixel at that point with a random color
    c = random.choice([RED,GREEN,BLUE])
    screen.set_at((x,y),c)

    # Update the display
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(600)

# Quit pygame and close the window
pygame.quit()