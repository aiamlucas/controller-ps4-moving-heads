# File: dmx_control.py
import tkinter as tk
import serial
import threading
import controller_input  # Import the controller input script
import time

# Establish a connection to the Arduino
def connect_to_arduino():
    ports = ['/dev/ttyACM0', '/dev/ttyACM1']
    for port in ports:
        try:
            return serial.Serial(port, 9600, timeout=1)
        except serial.SerialException:
            continue
    raise Exception("Unable to find Arduino.")

def send_command(channel, value):
    command = f"C{channel},{value}\n"
    arduino.write(command.encode())

# Function to update DMX values based on controller input
def update_dmx_from_controller():
    while True:
        x_value = controller_input.get_current_x()
        y_value = controller_input.get_current_y()
        send_command(1, x_value)  # Channel 1 is the x-axis
        send_command(3, y_value)  # Channel 3 is the y-axis
        time.sleep(0.1)

# Initialize the main window
root = tk.Tk()
root.title("DMX Channel Controller")

arduino = connect_to_arduino()
controller_input.start_controller_thread()

# Start the thread to update DMX from the controller
threading.Thread(target=update_dmx_from_controller, daemon=True).start()

root.mainloop()
