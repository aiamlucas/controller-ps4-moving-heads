# DMX Light Control via Gamepad

This project allows you to control DMX lights using a gamepad. The system 
reads inputs from the gamepad, processes them, and then sends the 
appropriate commands to the DMX controller to adjust the lighting.

## Structure

### 1. `controller_input.py`

This script handles the input from your gamepad. It reads the X and Y-axis 
values of the left stick and the D-pad, processes these inputs, and 
provides functions to access the current values of these inputs.

Key Features:
- Reads gamepad input in a separate thread to avoid blocking the main 
program.
- Scales the 16-bit input from the gamepad to an 8-bit range (0-255) for 
compatibility with DMX channel values.
- Provides `get_current_x()` and `get_current_y()` functions to access the 
processed X and Y values respectively.

### 2. `dmx_control.py`

This script establishes a connection with the Arduino (acting as a DMX 
controller) and sends commands based on the input received from the 
gamepad.

Key Features:
- Establishes a serial connection with the Arduino.
- Sends DMX commands to the Arduino to control the lights.
- Integrates with `controller_input.py` to use the gamepad input for DMX 
control.

## Setup and Usage

### Prerequisites

- `evdev` library installed for reading gamepad inputs.
- `pySerial` library installed for serial communication with the Arduino.
- A gamepad connected to your system.
- An Arduino set up as a DMX controller.

