import sys
import unittest
import os

sys.path.insert(1, '')

from parser import clear_output_directory


class TestClearPathAction(unittest.TestCase):

    def setUp(self):
        self.test_directory = 'test_output_files'
        os.makedirs(self.test_directory, exist_ok=True)
        for i in range(5):
            open(f"{self.test_directory}/test_file_{i}.json", 'a').close()

    def test_clear_path_action(self):
        initial_file_count = len([f for f in os.listdir(self.test_directory) if os.path.isfile(os.path.join(self.test_directory, f))])
        clear_output_directory(self.test_directory, 'test_file')
        final_file_count = len([f for f in os.listdir(self.test_directory) if os.path.isfile(os.path.join(self.test_directory, f))])
        self.assertEqual(final_file_count, 0, "Files were not cleared from the directory.")

    def tearDown(self):
        for file in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, file)
            os.remove(file_path)
        os.rmdir(self.test_directory)

if __name__ == '__main__':
    unittest.main()