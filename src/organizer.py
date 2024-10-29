import os
import shutil

def organise_files(path):
    files = os.listdir(path)
    output = []

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(os.path.join(path, extension)):
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            output.append(f"Moved {file} to {extension} folder\n")
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            output.append(f"Created {extension} folder and moved {file}\n")

    return output