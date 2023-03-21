import pygame
import math

def draw_sierpinski_curve(surface, level, x, y, length, angle, scale=1.0):
    if level > 0:
        # Recursive case: divide the curve into three and draw each part
        new_length = length * scale / 2
        draw_sierpinski_curve(surface, level - 1, x, y, new_length, angle, scale)  # left segment
        x = x + new_length * math.cos(math.radians(angle))
        y = y - new_length * math.sin(math.radians(angle))
        angle = angle - 60
        draw_sierpinski_curve(surface, level - 1, x, y, new_length, angle, scale)  # right segment
        x = x + new_length * math.cos(math.radians(angle))
        y = y - new_length * math.sin(math.radians(angle))
        angle = angle + 120
        draw_sierpinski_curve(surface, level - 1, x, y, new_length, angle, scale)  # middle segment
    else:
        # Base case: draw a single line
        x2 = x + length * scale * math.cos(math.radians(angle))
        y2 = y - length * scale * math.sin(math.radians(angle))
        pygame.draw.line(surface, (255, 255, 255), (x, y), (x2, y2))

def animate_sierpinski_curve(surface, start_level, max_level, width, height, length, angle, fps=60, level_speed=0.5):
    clock = pygame.time.Clock()
    current_level = start_level
    scale = 1.0
    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
        
        if not paused:
            surface.fill((0, 0, 0))
            x = (width - length * scale) // 2 # calculate x position to center curve horizontally
            y = (height + length * scale * math.sqrt(3) / 2) // 2 # calculate y position to center curve vertically
            draw_sierpinski_curve(surface, current_level, x, y, length, angle, scale)
            current_level += level_speed
            if current_level > max_level:
                current_level = start_level
            scale = 1.0 - (current_level - start_level) / (max_level - start_level) # decrease scale as level increases
            pygame.display.flip()
            
        clock.tick(fps)

pygame.init()

# Set up the Pygame window
window_size = (1000, 1000)
window = pygame.display.set_mode(window_size)

# Set up the animation parameters
start_level = 1
max_level = 5000
x, y = 600, -100
length = 1000
angle = 0
fps = 30
level_speed = 0.1

# Animate the Sierpinski curve
animate_sierpinski_curve(window, start_level, max_level, x, y, length, angle, fps, level_speed)

pygame.quit()
