from src.user_interface import *
from src.organizer import *

if __name__ == "__main__":
    set_organizer_function(organise_files)
    window.mainloop()
