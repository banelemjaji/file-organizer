import os
import tkinter as tk
from tkinter import scrolledtext, filedialog
from tkinter import ttk

from src.organizer import organise_files

# Define a global variable to hold the organizer function
organizer_function = None

def set_organizer_function(func):
    global organizer_function
    organizer_function = func

def execute_organizer(entry_path):
    if organizer_function is None:
        raise ValueError("Organizer function is not set.")
    
    path = entry_path.get()
    if not os.path.isdir(path):
        output_text.insert(tk.END, "Invalid path.\n")
        return

    # Disable the button during execution
    button_execute.config(state=tk.DISABLED)
    progress_bar.start()  # Start the progress bar animation

    output = organizer_function(path)
    
    # Stop the progress bar after completion
    progress_bar.stop()
    button_execute.config(state=tk.NORMAL)  # Re-enable the button after execution

    output_text.delete(1.0, tk.END)  # Clear previous output
    for line in output:
        output_text.insert(tk.END, line)

def browse_folder(entry_path):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)  # Clear existing path
        entry_path.insert(tk.END, folder_selected)  # Set the selected path

# Create the main window
window = tk.Tk()
window.title("File Organizer")
window.geometry("600x400")  # Set a fixed window size
window.configure(bg='#f0f0f0')

# Apply a custom ttk theme for a more modern look
style = ttk.Style(window)
style.configure('TButton', font=('Arial', 10, 'bold'), padding=6)
style.configure('TLabel', font=('Arial', 10), background='#f0f0f0')
style.configure('TEntry', font=('Arial', 10), padding=6)
style.configure('TScrolledText', font=('Arial', 10), padding=6)

# Create input entry for path
label_path = ttk.Label(window, text="Enter Path:")
label_path.pack(pady=(20, 5))
entry_path = ttk.Entry(window, width=50)
entry_path.pack(pady=5)

# Create a button to browse and select folder
browse_button = ttk.Button(window, text="Browse", command=lambda: browse_folder(entry_path))
browse_button.pack(pady=5)

# Create a button to execute the organizer feature
button_execute = ttk.Button(window, text="Execute Organizer", command=lambda: execute_organizer(entry_path))
button_execute.pack(pady=15)

# Add a progress bar for feedback during file processing
# progress_bar = ttk.Progressbar(window, mode='indeterminate', length=200)
# progress_bar.pack(pady=10)

# Create text area for output
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10, bd=2)
output_text.pack(pady=10)

# Run the application
if __name__ == "__main__":
    set_organizer_function(organise_files)
    window.mainloop()
