import os
import shutil

def organise_files(path):
    file_types = {
        'Images': ['.jpg', '.png', '.gif'],
        'Documents': ['.pdf', '.txt', '.docx'],
        'Videos': ['.mp4', '.avi'],
        'Audio': ['.mp3', '.wav']
    }
    
    files = os.listdir(path)
    output = []

    def ensure_folder_exists(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file in files:
        try:
            filename, extension = os.path.splitext(file)
            extension = extension.lower()

            folder_found = False
            for category, exts in file_types.items():
                if extension in exts:
                    folder = os.path.join(path, category)
                    ensure_folder_exists(folder)
                    shutil.move(os.path.join(path, file), os.path.join(folder, file))
                    output.append(f"Moved {file} to {category} folder\n")
                    folder_found = True
                    break
            
            if not folder_found:
                output.append(f"Unsupported file type for {file}\n")

        except Exception as e:
            output.append(f"Error with file {file}: {str(e)}\n")

    return output
