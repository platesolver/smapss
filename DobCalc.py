import pygame
import pygame_gui
import math

# Initialize Pygame and Pygame GUI
pygame.init()
pygame.display.set_caption("Stepper Motor and Pulley System")
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up GUI manager
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the radius of the pulleys
radius = 50

# Title
title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 10), (1180, 30)), 
                                          text="Stepper Motor and Pulley System Simulation", manager=manager)

# GUI elements
stepper_out_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 50), (250, 30)), text="Stepper GT2 Tooth Count", manager=manager)
stepper_out_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 50), (100, 30)), manager=manager)
stepper_out_input.set_text("20")

stage1_in_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 90), (250, 30)), text="Stage 1 GT2 Tooth Count (In)", manager=manager)
stage1_in_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 90), (100, 30)), manager=manager)
stage1_in_input.set_text("180")
stage1_out_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 130), (250, 30)), text="Stage 1 GT2 Tooth Count (Out)", manager=manager)
stage1_out_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 130), (100, 30)), manager=manager)
stage1_out_input.set_text("40")

stage2_in_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 170), (250, 30)), text="Stage 2 GT2 Tooth Count (In)", manager=manager)
stage2_in_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 170), (100, 30)), manager=manager)
stage2_in_input.set_text("180")
stage2_out_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 210), (250, 30)), text="Stage 2 GT2 Tooth Count (Out)", manager=manager)
stage2_out_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 210), (100, 30)), manager=manager)
stage2_out_input.set_text("40")

stage3_in_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 250), (250, 30)), text="Stage 3 GT2 Tooth Count (In)", manager=manager)
stage3_in_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 250), (100, 30)), manager=manager)
stage3_in_input.set_text("180")
stage3_out_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 290), (250, 30)), text="Stage 3 GT2 Tooth Count (Out)", manager=manager)
stage3_out_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 290), (100, 30)), manager=manager)
stage3_out_input.set_text("40")

telescope_in_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 330), (250, 30)), text="Telescope GT2 Tooth Count (In)", manager=manager)
telescope_in_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 330), (100, 30)), manager=manager)
telescope_in_input.set_text("240")

microstep_count_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 370), (250, 30)), text="Microstep Count", manager=manager)
microstep_count_dropdown = pygame_gui.elements.UIDropDownMenu(
    options_list=['0', '2', '4', '8', '16', '32', '64', '128', '256'],
    starting_option='0',
    relative_rect=pygame.Rect((270, 370), (100, 30)),
    manager=manager
)

stepper_step_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 410), (250, 30)), text="Stepper Steps per Revolution", manager=manager)
stepper_step_dropdown = pygame_gui.elements.UIDropDownMenu(
    options_list=['200', '400'],
    starting_option='200',
    relative_rect=pygame.Rect((270, 410), (100, 30)),
    manager=manager
)

speed_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 450), (250, 30)), text="Speed (steps per frame)", manager=manager)
speed_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((270, 450), (100, 30)), manager=manager)
speed_input.set_text("2")

reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 490), (150, 30)), text="Reset", manager=manager)

# Pulley positions
right_margin = WIDTH - 300
positions = [
    (right_margin, 100),  # Stepper
    (right_margin, 200),  # Stage 1
    (right_margin, 300),  # Stage 2
    (right_margin, 400),  # Stage 3
    (right_margin, 500)   # Telescope
]

# Labels for each stage
labels = ["Stepper", "Stage 1", "Stage 2", "Stage 3", "Telescope"]

# Initialize angles for each pulley
pulley_angles = [0, 0, 0, 0, 0]
pulley_rotations = [0, 0, 0, 0, 0]
stepper_angle = 0
stepper_steps = 0
stepper_rotations = 0
stepper_speed = 2  # steps per frame

# Initialize default values
default_values = {
    'stepper_out': 20,
    'stage1_in': 180,
    'stage1_out': 40,
    'stage2_in': 180,
    'stage2_out': 40,
    'stage3_in': 180,
    'stage3_out': 40,
    'telescope_in': 240,
    'microstep_count': 0,
    'stepper_step': 200,
    'stepper_speed': 2
}

# Initialize values
stepper_out = default_values['stepper_out']
stage1_in = default_values['stage1_in']
stage1_out = default_values['stage1_out']
stage2_in = default_values['stage2_in']
stage2_out = default_values['stage2_out']
stage3_in = default_values['stage3_in']
stage3_out = default_values['stage3_out']
telescope_in = default_values['telescope_in']
microstep_count = default_values['microstep_count']
stepper_step = default_values['stepper_step']

# Initialize rotation counts
rotation_counts = [0, 0, 0, 0, 0]
telescope_angle = 0
telescope_arcseconds = 0

# Main loop
running = True
clock = pygame.time.Clock()

def reset_values():
    global stepper_angle, stepper_steps, stepper_rotations, pulley_angles, pulley_rotations, rotation_counts, telescope_angle, telescope_arcseconds
    stepper_out_input.set_text(str(default_values['stepper_out']))
    stage1_in_input.set_text(str(default_values['stage1_in']))
    stage1_out_input.set_text(str(default_values['stage1_out']))
    stage2_in_input.set_text(str(default_values['stage2_in']))
    stage2_out_input.set_text(str(default_values['stage2_out']))
    stage3_in_input.set_text(str(default_values['stage3_in']))
    stage3_out_input.set_text(str(default_values['stage3_out']))
    telescope_in_input.set_text(str(default_values['telescope_in']))
    microstep_count_dropdown.selected_option = str(default_values['microstep_count'])
    stepper_step_dropdown.selected_option = str(default_values['stepper_step'])
    speed_input.set_text(str(default_values['stepper_speed']))
    stepper_angle = 0
    stepper_steps = 0
    stepper_rotations = 0
    pulley_angles = [0, 0, 0, 0, 0]
    pulley_rotations = [0, 0, 0, 0, 0]
    rotation_counts = [0, 0, 0, 0, 0]
    telescope_angle = 0
    telescope_arcseconds = 0

# Initial reset to set the default values
reset_values()

# List of text input elements for focus handling
text_inputs = [
    stepper_out_input, stage1_in_input, stage1_out_input,
    stage2_in_input, stage2_out_input,
    stage3_in_input, stage3_out_input,
    telescope_in_input, speed_input
]
current_focus_index = 0

# Function to calculate arcsecond resolution
def calculate_arcsecond_resolution(microsteps):
    resolutions = []
    for ms in microsteps:
        step_angle = 360 / (stepper_step * ms)
        telescope_resolution = step_angle / cumulative_ratios[-1] * 3600
        resolutions.append(f"{ms}x: {telescope_resolution:.6f} arcseconds")
    return resolutions

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            if event.mod & pygame.KMOD_SHIFT:
                current_focus_index = (current_focus_index - 1) % len(text_inputs)
            else:
                current_focus_index = (current_focus_index + 1) % len(text_inputs)
            text_inputs[current_focus_index].focus()
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == reset_button:
                reset_values()

        manager.process_events(event)

    manager.update(time_delta)
    screen.fill(WHITE)

    # Get updated values
    try:
        stepper_out = max(1, min(1440, int(stepper_out_input.get_text())))
        stage1_in = max(1, min(1440, int(stage1_in_input.get_text())))
        stage1_out = max(1, min(1440, int(stage1_out_input.get_text())))
        stage2_in = max(1, min(1440, int(stage2_in_input.get_text())))
        stage2_out = max(1, min(1440, int(stage2_out_input.get_text())))
        stage3_in = max(1, min(1440, int(stage3_in_input.get_text())))
        stage3_out = max(1, min(1440, int(stage3_out_input.get_text())))
        telescope_in = max(1, min(1440, int(telescope_in_input.get_text())))
        microstep_count = int(microstep_count_dropdown.selected_option)
        stepper_step = int(stepper_step_dropdown.selected_option)
        stepper_speed = max(1, min(360, int(speed_input.get_text())))
    except ValueError:
        pass

    # Calculate reduction ratios, ensuring no division by zero and handling 1:1 reduction
    try:
        ratios = [
            stage1_in / stepper_out if stepper_out != stage1_in else 1, 
            stage2_in / stage1_out if stage1_out != stage2_in else 1, 
            stage3_in / stage2_out if stage2_out != stage3_in else 1, 
            telescope_in / stage3_out if stage3_out != telescope_in else 1
        ]
        cumulative_ratios = [ratios[0]]
        for ratio in ratios[1:]:
            cumulative_ratios.append(cumulative_ratios[-1] * ratio)
    except ZeroDivisionError:
        cumulative_ratios = [1, 1, 1, 1]

    # Update stepper motor angle
    stepper_angle += stepper_speed * 360 / stepper_step
    stepper_steps += stepper_speed
    stepper_rotations = stepper_steps / stepper_step
    stepper_angle %= 360

    # Accumulate each pulley angle based on the previous pulley's angle and ratio
    pulley_angles[0] = stepper_angle
    for i in range(1, len(pulley_angles)):
        pulley_angles[i] += stepper_speed * 360 / (stepper_step * cumulative_ratios[i - 1])
        pulley_rotations[i] += stepper_speed / (stepper_step * cumulative_ratios[i - 1])
        pulley_angles[i] %= 360  # Keep the angle within 0-360 degrees
        rotation_counts[i] = pulley_rotations[i]

    # Calculate telescope angle and arcseconds
    telescope_angle = pulley_angles[-1]
    telescope_arcseconds = telescope_angle * 3600

    # Calculate arcsecond resolutions for different microsteps
    microsteps = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    arcsecond_resolutions = calculate_arcsecond_resolution(microsteps)

    # Draw stepper motor
    pygame.draw.circle(screen, BLACK, positions[0], radius)
    stepper_end = (
        positions[0][0] + radius * math.cos(math.radians(pulley_angles[0])),
        positions[0][1] + radius * math.sin(math.radians(pulley_angles[0]))
    )
    pygame.draw.line(screen, RED, positions[0], stepper_end, 2)
    font = pygame.font.Font(None, 36)
    text = font.render(labels[0], True, BLACK)
    screen.blit(text, (positions[0][0] + 60, positions[0][1] - 10))
    stepper_info = font.render(f"Steps: {stepper_steps:.2f}", True, BLACK)
    screen.blit(stepper_info, (positions[0][0] + 60, positions[0][1] + 10))
    stepper_rot_info = font.render(f"Rotations: {stepper_rotations:.2f}", True, BLACK)
    screen.blit(stepper_rot_info, (positions[0][0] + 60, positions[0][1] + 40))

    # Draw pulleys with correct angles and labels
    for i in range(1, len(pulley_angles)):
        pygame.draw.circle(screen, BLACK, positions[i], radius)
        pulley_end = (
            positions[i][0] + radius * math.cos(math.radians(pulley_angles[i])),
            positions[i][1] + radius * math.sin(math.radians(pulley_angles[i]))
        )
        pygame.draw.line(screen, RED, positions[i], pulley_end, 2)
        text = font.render(labels[i], True, BLACK)
        screen.blit(text, (positions[i][0] + 60, positions[i][1] - 10))
        rotation_info = font.render(f"Rotations: {rotation_counts[i]:.2f}", True, BLACK)
        screen.blit(rotation_info, (positions[i][0] + 60, positions[i][1] + 10))

    # Draw telescope info
    telescope_info = font.render(f"Angle: {telescope_angle:.2f}", True, BLACK)
    screen.blit(telescope_info, (positions[-1][0] + 60, positions[-1][1] + 40))
    telescope_arc_info = font.render(f"Arcseconds: {telescope_arcseconds:.2f}", True, BLACK)
    screen.blit(telescope_arc_info, (positions[-1][0] + 60, positions[-1][1] + 60))

    # Draw arcsecond resolution info in the middle of the window
    resolution_font = pygame.font.Font(None, 30)
    for idx, res in enumerate(arcsecond_resolutions):
        resolution_text = resolution_font.render(res, True, BLACK)
        screen.blit(resolution_text, (WIDTH // 2 - 100, 70 + idx * 30))

    manager.draw_ui(screen)

    # Update display
    pygame.display.flip()

pygame.quit()
