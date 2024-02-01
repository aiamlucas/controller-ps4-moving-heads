# File: controller_input.py
import evdev
from evdev import InputDevice, ecodes
import threading

# Constants for axis range adjustment
AXIS_MAX = 32767    # Adjust this value based on your joystick's actual range
AXIS_MIN = -32768   # Adjust this value based on your joystick's actual range
CENTER_ZONE = 5000   # Zone around the center to be considered as 'no movement'

# Variables to hold the current X and Y values
current_x = 127
current_y = 127

def scale_stick_value(value):
    # Scale the joystick input range (AXIS_MIN to AXIS_MAX) to (0 to 255)
    return int((value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 255)

def get_ps4_controller():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'Generic X-Box pad' in device.name:
            return device
    return None

def process_controller_inputs(device):
    global current_x, current_y
    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_X:  # Left stick X-axis
                new_x = scale_stick_value(event.value)
                if abs(event.value) < CENTER_ZONE:  # If the stick is near the center, don't change the value
                    continue
                if new_x > current_x and event.value > 0:  # If moving the stick upwards and it's above the current value
                    current_x = new_x
                elif new_x < current_x and event.value < 0:  # If moving the stick downwards and it's below the current value
                    current_x = new_x
                # Clamp the value between 0 and 255
                current_x = max(0, min(current_x, 255))
                
            elif event.code == ecodes.ABS_Y:  # Left stick Y-axis
                new_y = scale_stick_value(event.value)
                if abs(event.value) < CENTER_ZONE:  # If the stick is near the center, don't change the value
                    continue
                if new_y > current_y and event.value > 0:  # If moving the stick upwards and it's above the current value
                    current_y = new_y
                elif new_y < current_y and event.value < 0:  # If moving the stick downwards and it's below the current value
                    current_y = new_y
                # Clamp the value between 0 and 255
                current_y = max(0, min(current_y, 255))
                
            # D-pad left/right
            elif event.code == ecodes.ABS_HAT0X:  
                if event.value == 1:  # D-pad right increases the value
                    current_x = min(current_x + 2, 255)
                elif event.value == -1:  # D-pad left decreases the value
                    current_x = max(current_x - 2, 0)

            # D-pad up/down
            elif event.code == ecodes.ABS_HAT0Y:  # D-pad Y-axis
                if event.value == 1:  # D-pad down increases the value
                    current_y = min(current_y + 2, 255)
                elif event.value == -1:  # D-pad up decreases the value
                    current_y = max(current_y - 2, 0)

def start_controller_thread():
    ps4_controller = get_ps4_controller()
    if ps4_controller is not None:
        threading.Thread(target=process_controller_inputs, args=(ps4_controller,), daemon=True).start()
    else:
        print("Controller not found. Please ensure it's connected.")

def get_current_x():
    return current_x

def get_current_y():
    return current_y
