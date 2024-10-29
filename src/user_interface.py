import tkinter as tk
from tkinter import scrolledtext

# Define a global variable to hold the organizer function
organizer_function = None

def set_organizer_function(func):
    global organizer_function
    organizer_function = func

def execute_organizer(entry_path):
    if organizer_function is None:
        raise ValueError("Organizer function is not set.")
    path = entry_path.get()
    output = organizer_function(path)
    output_text.delete(1.0, tk.END)  # Clear previous output
    for line in output:
        output_text.insert(tk.END, line)

# Create the main window
window = tk.Tk()
window.title("File Organizer")

# Create input entry for path
label_path = tk.Label(window, text="Enter Path:")
label_path.pack()
entry_path = tk.Entry(window)
entry_path.pack()

# Create a button to execute the organizer feature
button = tk.Button(window, text="Execute Organizer", command=lambda: execute_organizer(entry_path))
button.pack()

# Create text area for output
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
output_text.pack()
