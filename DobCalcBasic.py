import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stepper Motor and Pulley System")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pulley and stepper motor parameters
center = (WIDTH // 2, HEIGHT // 2)
radius = 50
stepper_angle = 0
stepper_speed = 2  # degrees per frame

# Reduction ratios
ratios = [9, 4.5, 4.5, 6]
cumulative_ratios = [9, 40.5, 182.25, 1093.5]

# Calculate pulley positions
pulley_positions = [
    (center[0] - 300, center[1]),
    (center[0] - 150, center[1]),
    (center[0], center[1]),
    (center[0] + 150, center[1]),
    (center[0] + 300, center[1])
]

# Initialize cumulative angles for each pulley
pulley_angles = [0, 0, 0, 0]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Update stepper motor angle
    stepper_angle += stepper_speed
    stepper_angle %= 360

    # Draw stepper motor
    pygame.draw.circle(screen, BLACK, pulley_positions[0], radius)
    stepper_end = (
        pulley_positions[0][0] + radius * math.cos(math.radians(stepper_angle)),
        pulley_positions[0][1] + radius * math.sin(math.radians(stepper_angle))
    )
    pygame.draw.line(screen, RED, pulley_positions[0], stepper_end, 2)

    # Update pulley angles based on cumulative reduction ratios
    for i in range(4):
        pulley_angles[i] += stepper_speed / cumulative_ratios[i]
        pulley_angles[i] %= 360  # Keep the angle within 0-360 degrees

    # Draw pulleys with correct angles
    for i in range(4):
        pygame.draw.circle(screen, BLACK, pulley_positions[i + 1], radius)
        pulley_end = (
            pulley_positions[i + 1][0] + radius * math.cos(math.radians(pulley_angles[i])),
            pulley_positions[i + 1][1] + radius * math.sin(math.radians(pulley_angles[i]))
        )
        pygame.draw.line(screen, RED, pulley_positions[i + 1], pulley_end, 2)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
