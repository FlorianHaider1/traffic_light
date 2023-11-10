# Traffic Light Sequence Simulator: Objective: Simulate a traffic light system 
# where each light sequence is represented as a tuple (color, duration).
# Tasks: Create a list of light sequences (e.g., ("green", 60), ("yellow", 10), ("red", 50)). 
# Use pattern matching to simulate the traffic light operation, printing which light is on and for how long. 
# Include safety checks to ensure the sequence always goes green -> yellow -> red.
import time
import tkinter as tk

color = "green", "yellow", "red"
time_elapse = 6, 2, 4
lights = tuple(zip(color, time_elapse))

def loop(sequence, root, label):
    for color, duration in sequence:
        update_label(label, color, duration)
        root.update()
        time.sleep(duration)

def update_label(label, color, duration):
    label.config(text = color, background = color, foreground = color)
    label.master.title(f"Display letter: {color} for {duration} in seconds"

def main():
    root = tk.Tk()
    label = tk.Label(root, font=("Arial", 40)
    label.pack(expand=True, fill="both")
    colors_and_durations = lights
    loop(colors_and_durations, root, label)
    root.mainloop()



main()




