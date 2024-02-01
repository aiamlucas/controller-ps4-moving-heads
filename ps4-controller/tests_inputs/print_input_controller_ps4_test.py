
import evdev
from evdev import InputDevice, categorize, ecodes

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
        if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
            print(categorize(event), event.type, event.code, event.value)

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