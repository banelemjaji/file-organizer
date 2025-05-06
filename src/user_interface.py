import os
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from tkinter import ttk
from collections import Counter

from src.organizer import FileOrganizer

organizer = FileOrganizer()

def execute_organizer(entry_path):
    path = entry_path.get()
    output_text.delete(1.0, tk.END)  # Clear previous output
    status_label.config(text="Organizing...")
    window.update_idletasks()

    if not os.path.isdir(path):
        output_text.insert(tk.END, "Invalid path.\n")
        status_label.config(text="Invalid path.")
        messagebox.showerror("Error", "Invalid path provided.")
        return

    # Disable the button during execution
    button_execute.config(state=tk.DISABLED)

    try:
        output = organizer.organize(path)
        # Parse output for summary
        summary_counter = Counter()
        for line in output:
            if line.startswith("Moved"):
                # Example: Moved file.txt to Documents folder
                parts = line.split(' to ')
                if len(parts) == 2:
                    folder = parts[1].replace(' folder\n', '').replace(' folder', '').replace('\n', '').strip()
                    summary_counter[folder] += 1
        button_execute.config(state=tk.NORMAL)  # Re-enable the button after execution

        # Group moved files by destination folder for better readability
        moved_files = {}
        for line in output:
            if line.startswith("Moved"):
                # Example: Moved file.txt to Documents folder
                parts = line.split(' to ')
                if len(parts) == 2:
                    file_name = parts[0].replace('Moved ', '').strip()
                    folder = parts[1].replace(' folder\n', '').replace(' folder', '').replace('\n', '').strip()
                    moved_files.setdefault(folder, []).append(file_name)
        # Display grouped output
        for folder, files in moved_files.items():
            output_text.insert(tk.END, f"Files moved to {folder}:\n")
            for fname in files:
                output_text.insert(tk.END, f"  - {fname}\n")
            output_text.insert(tk.END, "\n")
        # Display errors and others
        for line in output:
            if not line.startswith("Moved"):
                output_text.insert(tk.END, line)
        if summary_counter:
            output_text.insert(tk.END, "\nSummary:\n")
            for folder, count in summary_counter.items():
                output_text.insert(tk.END, f"{folder}: {count} files moved\n")
        status_label.config(text="Complete!")
        messagebox.showinfo("Complete", "File organization complete!")
    except Exception as e:
        button_execute.config(state=tk.NORMAL)
        status_label.config(text="Error during organizing.")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_folder(entry_path):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)  # Clear existing path
        entry_path.insert(tk.END, folder_selected)  # Set the selected path

# Create the main window
window = tk.Tk()
window.title("File Organizer")
window.geometry("900x700")  # Set a larger window size
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


# Create text area for output
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=20, bd=2)
output_text.pack(pady=10)

# Add a frame for bottom controls (status + exit)
bottom_frame = ttk.Frame(window)
bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

# Add an Exit button
exit_button = ttk.Button(bottom_frame, text="Exit", command=window.destroy)
exit_button.pack(side=tk.RIGHT, padx=10, pady=2)

# Add a status label at the bottom
status_label = ttk.Label(bottom_frame, text="Ready", anchor='w', relief='sunken')
status_label.pack(fill=tk.X, side=tk.LEFT, expand=True, ipady=2)

# Run the application
if __name__ == "__main__":
    window.mainloop()
