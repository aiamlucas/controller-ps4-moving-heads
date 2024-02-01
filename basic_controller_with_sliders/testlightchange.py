import tkinter as tk
from tkinter import Scale
import serial
import threading

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

def on_slider_change(val, channel):
    value = int(float(val))
    send_command(channel, value)

# Initialize the main window
root = tk.Tk()
root.title("DMX Channel Controller")

arduino = connect_to_arduino()

# Create and place sliders
for channel in range(1, 12):
    slider = Scale(root, from_=0, to=255, orient=tk.VERTICAL, length=300,
                   resolution=1, label=f"Channel {channel}",
                   command=lambda val, ch=channel: on_slider_change(val, ch))
    slider.grid(row=0, column=channel-1, padx=10, pady=10)

root.mainloop()