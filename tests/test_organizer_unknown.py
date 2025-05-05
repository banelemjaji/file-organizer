import os
import shutil
import tempfile
import unittest
from src.organizer import organise_files

class TestOrganizeFilesUnknown(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        # Files with unknown extensions
        self.unknown_files = ['random.xyz', 'file.abc', 'mystery.qwerty']
        for fname in self.unknown_files:
            with open(os.path.join(self.test_dir, fname), 'w') as f:
                f.write('test')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_unknown_files_moved_to_others(self):
        organise_files(self.test_dir)
        others_folder = os.path.join(self.test_dir, 'Others')
        self.assertTrue(os.path.isdir(others_folder), "Others folder should exist")
        for fname in self.unknown_files:
            self.assertTrue(os.path.isfile(os.path.join(others_folder, fname)), f"{fname} should be in Others")

if __name__ == '__main__':
    unittest.main()
