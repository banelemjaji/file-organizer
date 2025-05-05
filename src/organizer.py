import os
import shutil

def organise_files(path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Documents': ['.pdf', '.txt', '.doc', '.docx', '.odt', '.rtf', '.md', '.tex', '.log'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm'],
        'Audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.bz2', '.7z', '.xz'],
        'Code': ['.py', '.js', '.java', '.c', '.cpp', '.cs', '.rb', '.go', '.php', '.html', '.css', '.json', '.xml', '.sh', '.bat', '.ipynb']
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
                # Move to 'Others' folder
                others_folder = os.path.join(path, 'Others')
                ensure_folder_exists(others_folder)
                shutil.move(os.path.join(path, file), os.path.join(others_folder, file))
                output.append(f"Moved {file} to Others folder\n")

        except Exception as e:
            output.append(f"Error with file {file}: {str(e)}\n")

    return output
