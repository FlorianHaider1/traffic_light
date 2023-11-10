# Traffic Light Sequence Simulator: Objective: Simulate a traffic light system 
# where each light sequence is represented as a tuple (color, duration).
# Tasks: Create a list of light sequences (e.g., ("green", 60), ("yellow", 10), ("red", 50)). 
# Use pattern matching to simulate the traffic light operation, printing which light is on and for how long. 
# Include safety checks to ensure the sequence always goes green -> yellow -> red.
import time
import tkinter as tk

cycle = 1
color = "green", "yellow", "red"
time_elapse = 4, 2, 3
lights = tuple(zip(color, time_elapse))

def loop(sequence, root, label):
    for color, duration in sequence:
        for remaining in range(duration, 0, -1):
            update_label(label, color, remaining)
            root.update()
            time.sleep(1)

def update_label(label, color, remaining):
    label.config(text = f"{color} {remaining}", background = color, foreground = "black")
    label.master.title("Traffic Light")


def main():
    root = tk.Tk()
    label = tk.Label(root, font=("Arial", 40))
    label.pack(expand=True, fill="both")
    colors_and_durations = lights
    loop(colors_and_durations, root, label)
    root.destroy()


while cycle < 4:
    main()
    cycle += 1




