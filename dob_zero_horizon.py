import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_telescope(angle):
    fig, ax = plt.subplots()
    # Draw the base
    ax.add_patch(patches.Rectangle((0.4, 0.1), 0.2, 0.05, edgecolor='black', facecolor='black'))
    # Draw the stand
    ax.add_patch(patches.Rectangle((0.475, 0.15), 0.05, 0.3, edgecolor='gray', facecolor='gray'))
    # Draw the tube rotated at the given angle
    tube_length = 0.5
    tube_width = 0.05
    ax.add_patch(patches.Rectangle((0.475, 0.45), tube_width, tube_length, angle=angle, edgecolor='navy', facecolor='navy'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Example usage:
draw_telescope(0)  # Telescope pointing up
draw_telescope(90) # Telescope horizontal
