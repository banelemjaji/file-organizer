# File Organizer

A modern, user-friendly desktop application for automatically organizing files into categorized folders.

## Features
- Organizes files into categories: Images, Documents, Spreadsheets, Presentations, Videos, Audio, Archives, Code, Others
- Easy-to-use graphical interface (built with Tkinter)
- Clear, grouped output of moved files
- Status updates and summary after organizing
- Error handling and logging (`organizer.log`)
- Extensible: add new file types/categories in the code
- Cross-platform (Windows, macOS, Linux)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/banelemjaji/file-organizer.git
   cd file-organizer
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *(Currently, only standard Python libraries are used)*

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. In the GUI:
   - Enter or browse to the folder you want to organize.
   - Click "Execute Organizer".
   - View the grouped output and summary.
   - Click "Exit" to close the app.

## Configuration
- To add or change file type categories, edit the `file_types` dictionary in `src/organizer.py` inside the `FileOrganizer` class.
- Log output is written to `organizer.log`.

## Screenshots
*(Add screenshots here to showcase the UI!)*

## Project Structure
```
file-organizer/
├── main.py               # Entry point
├── src/
│   ├── organizer.py      # FileOrganizer class (core logic)
│   └── user_interface.py # Tkinter GUI
├── tests/                # Unit and integration tests
├── .gitignore
└── README.md
```