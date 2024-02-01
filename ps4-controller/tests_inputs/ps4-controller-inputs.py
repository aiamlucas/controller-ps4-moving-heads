import evdev
from evdev import InputDevice, categorize, ecodes

# Constants for axis range adjustment
AXIS_MAX = 32767    # Adjust this value based on your joystick's actual range
AXIS_MIN = -32768   # Adjust this value based on your joystick's actual range
CENTER_ZONE = 5000   # Zone around the center to be considered as 'no movement'

# Variables to hold the current X and Y values
current_x = 127
current_y = 127  # Added variable for Y-axis

def scale_stick_value(value):
    # Scale the joystick input range (AXIS_MIN to AXIS_MAX) to (0 to 255)
    return int((value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 255)

# Function to get the PS4 controller device
def get_ps4_controller():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'Generic X-Box pad' in device.name:  # Updated to the name recognized by your system
            return device
    return None

# Function to process controller inputs
def process_controller_inputs(device):
    global current_x, current_y  # Refer to the global variable for Y-axis as well
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
                print(f'X-axis value: {current_x}')
                
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
                print(f'Y-axis value: {current_y}')
                
            # D-pad left/right
            elif event.code == ecodes.ABS_HAT0X:  
                if event.value == 1:  # D-pad right increases the value
                    current_x = min(current_x + 1, 255)
                elif event.value == -1:  # D-pad left decreases the value
                    current_x = max(current_x - 1, 0)
                print(f'X-axis value: {current_x}')

            # D-pad up/down
            elif event.code == ecodes.ABS_HAT0Y:  # D-pad Y-axis
                if event.value == 1:  # D-pad down increases the value
                    current_y = min(current_y + 1, 255)
                elif event.value == -1:  # D-pad up decreases the value
                    current_y = max(current_y - 1, 0)
                print(f'Y-axis value: {current_y}')

# Main function
def main():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)  # This line prints all devices, you can comment it out after verifying the controller name

    ps4_controller = get_ps4_controller()
    if ps4_controller is not None:
        print(f"Found controller: {ps4_controller.name}")
        process_controller_inputs(ps4_controller)
    else:
        print("Controller not found. Please ensure it's connected.")

if __name__ == "__main__":
    main()

'''
import evdev
from evdev import InputDevice, categorize, ecodes

# Constants for axis range adjustment
AXIS_MAX = 32767    # Adjust this value based on your joystick's actual range
AXIS_MIN = -32768   # Adjust this value based on your joystick's actual range
CENTER_ZONE = 5000   # Zone around the center to be considered as 'no movement'

# Variables to hold the current X and Y values
current_x = 127

def scale_stick_value(value):
    # Scale the joystick input range (AXIS_MIN to AXIS_MAX) to (0 to 255)
    return int((value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 255)

# Function to get the PS4 controller device
def get_ps4_controller():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'Generic X-Box pad' in device.name:  # Updated to the name recognized by your system
            return device
    return None

# Function to process controller inputs
def process_controller_inputs(device):
    global current_x  # Refer to the global variable
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
                print(f'X-axis value: {current_x}')
                
            # D-pad left/right
            elif event.code == ecodes.ABS_HAT0X:  
                if event.value == 1:  # D-pad right increases the value
                    current_x = min(current_x + 1, 255)
                elif event.value == -1:  # D-pad left decreases the value
                    current_x = max(current_x - 1, 0)
                print(f'X-axis value: {current_x}')

# Main function
def main():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)  # This line prints all devices, you can comment it out after verifying the controller name

    ps4_controller = get_ps4_controller()
    if ps4_controller is not None:
        print(f"Found controller: {ps4_controller.name}")
        process_controller_inputs(ps4_controller)
    else:
        print("Controller not found. Please ensure it's connected.")

if __name__ == "__main__":
    main()
'''


'''
# Only whith arroy key

import evdev
from evdev import InputDevice, categorize, ecodes

# Constants for axis range adjustment
AXIS_MAX = 32767    # Adjust this value based on your joystick's actual range
AXIS_MIN = -32768   # Adjust this value based on your joystick's actual range
CENTER_ZONE = 5000   # Zone around the center to be considered as 'no movement'

# Variables to hold the current X and Y values
current_x = 127

def scale_stick_value(value):
    # Scale the joystick input range (AXIS_MIN to AXIS_MAX) to (0 to 255)
    return int((value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 255)

# Function to get the PS4 controller device
def get_ps4_controller():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'Generic X-Box pad' in device.name:  # Updated to the name recognized by your system
            return device
    return None

# Function to process controller inputs
def process_controller_inputs(device):
    global current_x  # Refer to the global variable
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
                print(f'X-axis value: {current_x}')

# Main function
def main():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)  # This line prints all devices, you can comment it out after verifying the controller name

    ps4_controller = get_ps4_controller()
    if ps4_controller is not None:
        print(f"Found controller: {ps4_controller.name}")
        process_controller_inputs(ps4_controller)
    else:
        print("Controller not found. Please ensure it's connected.")

if __name__ == "__main__":
    main()

'''

'''
# Having the arrow as absolut parameter (middle == 127)

import evdev
from evdev import InputDevice, categorize, ecodes

# Constants for axis range adjustment
AXIS_MAX = 32767    # Adjust this value based on your joystick's actual range
AXIS_MIN = -32768   # Adjust this value based on your joystick's actual range

def scale_stick_value(value):
    # Scale the joystick input range (AXIS_MIN to AXIS_MAX) to (0 to 255)
    return int((value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 255)

# Function to get the PS4 controller device
def get_ps4_controller():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'Generic X-Box pad' in device.name:  # Updated to the name recognized by your system
            return device
    return None

# Function to process controller inputs
def process_controller_inputs(device):
    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_X:  # Left stick X-axis
                x_value = scale_stick_value(event.value)
                print(f'X-axis value: {x_value}')
            elif event.code == ecodes.ABS_Y:  # Left stick Y-axis
                y_value = scale_stick_value(event.value)
                #print(f'Y-axis value: {y_value}')

# Main function
def main():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)  # This line prints all devices, you can comment it out after verifying the controller name

    ps4_controller = get_ps4_controller()
    if ps4_controller is not None:
        print(f"Found controller: {ps4_controller.name}")
        process_controller_inputs(ps4_controller)
    else:
        print("Controller not found. Please ensure it's connected.")

if __name__ == "__main__":
    main()
'''