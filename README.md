# Stepper Motor and Pulley System Simulation - SMAPSS 

(c) May 17th 2024 - Andrew Smalley AKADATA LIMITED



[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This repository contains both non-software content and software code. 

- The non-software content (e.g., documentation, designs) is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
- The software code is licensed under the GNU General Public License v3.0. See the [COPYING](COPYING) file for details.

## License

### Non-Software Content

This project’s non-software content is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.

### Software Code

The software code in this project is licensed under the GNU General Public License v3.0. See the [COPYING](COPYING) file for details.


### STL Files
- Original STL files came from onshape, are very useful and as such the STL files are not mine to copyright 


# Project Details

This project simulates a gearing pulley system for the altitude adjustment of a 12" Dobsonian telescope on its standard base. The simulation uses a NEMA stepper motor and three sets of custom 3D printed GT2 pulleys, with two gear ratios per section. The purpose of this simulation is to help visualize and understand the behavior of the pulley system and its effect on the telescope's movement.

Features

- Visual representation of the stepper motor and pulley system
- Adjustable parameters for GT2 pulley tooth counts
- Microstepping options for the stepper motor
- Real-time display of stepper motor steps, rotations, and telescope angle
- Calculation of arcsecond resolution for different microstepping modes

Screenshot
- See smps.jpg for a screenshot of the interface

Requirements

- Python 3.12 or later
- Pygame 2.4.1
- Pygame GUI 0.7.4

Installation

1. Clone the repository:
   git clone <repository-url>
   cd <repository-directory>

2. Install the required Python packages:
   pip install pygame pygame_gui

Usage

1. Run the simulation:
   python DobCalc.py

2. The simulation window will open, displaying the stepper motor and pulley system.

3. Use the input fields on the left side of the window to adjust the parameters:
   - Stepper GT2 Tooth Count: Number of teeth on the stepper motor pulley, start with an aluminum 20 tooth GT2 pulley
   - Stage 1 GT2 Tooth Count (In/Out): Number of teeth on the input/output pulleys for Stage 1. 30:160 default 5.33:1
   - Stage 2 GT2 Tooth Count (In/Out): Number of teeth on the input/output pulleys for Stage 2. 30:160 default 5.33:1
   - Stage 3 GT2 Tooth Count (In/Out): Number of teeth on the input/output pulleys for Stage 3. 30:160 default 5.33:1
   - Telescope GT2 Tooth Count (In): Number of teeth on the telescope pulley. 6:1 ratio from Stage 3
   - Microstep Count: Microstepping setting for the stepper motor.
   - Stepper Steps per Revolution: Number of steps per revolution for the stepper motor.
   - Speed (steps per frame): Speed of the stepper motor in steps per frame.

4. The simulation will update in real-time based on the input parameters. The display shows:
   - Steps and rotations for the stepper motor
   - Rotations for each pulley stage
   - Angle and arcseconds for the telescope

5. Arcsecond resolution for each microstepping mode is displayed in the middle of the window under the title.

6. Click the "Reset" button to reset the parameters to their default values.

STL Files

GT2_30T_160T_7mm.stl
  - This is a GT2 pulley with 160 input teeth and 30 output teeth (Note the spacing is bad and the 30T need raising 2-3mm to be correct) it is a 5.33:1 gear ratio
Increaser_30T_40T.stl
  - Cut off the lip on the 30T from the file above and slot this over, it will be a snug fit and change the input to 4:1

Other STL files that were created during testing, they may have better uses for varying arcsecond final movement resolution.
  - 20T180T_GT2_FinalPart.stl
  - 20to120T_compined_full.stl
  - 30T160T_7mm_V1_NICE_20T_NOT_30T.stl
  - 360T Increaser - 2GT Pulley Increaser Side(1).stl
  - 360T20TIPulley.stl
  - GT2_30T_160T_7mm.stl
  - Increaser20T180T.stl
  - Increaser_30T_40T.stl

GT2 Pulley belt requirements

At the moment this will work with 350mm - 400mm 6mm standard GT2 pulley belt, I suggest the use of fiberglass reinforced belts or steel reinforced for maximum strength.

Other parts, tensioners
  - At the moment the design is incomplete and here for the python code to emulate the accuracy of such a system. 
    Once the altitude mount is complete the Azimuth portion will be designed and implemented.

Telescope control system
  - For now, this will use OnStep or OnStepX with Teensy + TMC2209 although due to the accuracy of the current system only
    1x step resolves to 5.926 arcsecond resolution and is not enough to use with an imaging camera!! Use microsteps.
    32 microsteps resolve to 0.185 arcsecond resolution
    64 microsteps are required to reach 0.0925 arcsecond resolution,
    256 microsteps will reduce this to 0.023 arcseconds, this is more than enough for any camera and especially an F/5 Dob

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

