# import os
# import shutil
# import tempfile
# import unittest
# from src.organizer import organise_files

# class TestOrganizeFilesComprehensive(unittest.TestCase):
#     def setUp(self):
#         # Create a temporary directory
#         self.test_dir = tempfile.mkdtemp()
#         # Define test files for each category
#         self.test_files = {
#             'Images': ['photo.jpg', 'graphic.png', 'vector.svg'],
#             'Documents': ['report.pdf', 'notes.txt', 'paper.docx'],
#             'Spreadsheets': ['data.xls', 'table.xlsx', 'sheet.csv'],
#             'Presentations': ['slides.ppt', 'talk.pptx'],
#             'Videos': ['movie.mp4', 'clip.avi'],
#             'Audio': ['song.mp3', 'recording.wav'],
#             'Archives': ['archive.zip', 'backup.tar'],
#             'Code': ['script.py', 'web.js', 'program.java']
#         }
#         # Create all test files
#         for files in self.test_files.values():
#             for fname in files:
#                 with open(os.path.join(self.test_dir, fname), 'w') as f:
#                     f.write('test')

#     def tearDown(self):
#         # Remove the directory after the test
#         shutil.rmtree(self.test_dir)

#     def test_organize_files(self):
#         organise_files(self.test_dir)
#         # Check if files are in correct folders
#         for category, files in self.test_files.items():
#             folder = os.path.join(self.test_dir, category)
#             self.assertTrue(os.path.isdir(folder), f"{category} folder should exist")
#             for fname in files:
#                 self.assertTrue(os.path.isfile(os.path.join(folder, fname)), f"{fname} should be in {category}")

# if __name__ == '__main__':
#     unittest.main()
