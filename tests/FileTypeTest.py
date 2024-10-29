import unittest
from src.organizer import *

class FileTypeTest(unittest.TestCase):
    
    def test_file_type(self):
        self.assertEqual(organise_files("test"), ["Created test folder and moved test\n"])
        self.assertEqual(organise_files("test.txt"), ["Created txt folder and moved test.txt\n"])
        self.assertEqual(organise_files("test.jpg"), ["Created jpg folder and moved test.jpg\n"])
        self.assertEqual(organise_files("test.mp4"), ["Created mp4 folder and moved test.mp4\n"])
        self.assertEqual(organise_files("test.exe"), ["Created exe folder and moved test.exe\n"])
        self.assertEqual(organise_files("test.zip"), ["Created zip folder and moved test.zip\n"])
        self.assertEqual(organise_files("test.rar"), ["Created rar folder and moved test.rar\n"])
        self.assertEqual(organise_files("test"), ["Created unknown folder and moved test\n"])

if __name__ == "__main__":
    unittest.main()
