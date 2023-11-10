import os
import pytest
import sys
sys.path.insert(1, '..')
from src.utils import clear_output_directory



@pytest.fixture
def test_directory(tmpdir):
    test_directory = tmpdir.mkdir("test_output_files")
    for i in range(5):
        test_directory.join(f"test_file_{i}.json").write('')
    yield test_directory


def test_clear_path_action(test_directory):
    clear_output_directory(str(test_directory), 'test_file')
    final_file_count = len(
        [f for f in os.listdir(str(test_directory)) if os.path.isfile(os.path.join(str(test_directory), f))])
    assert final_file_count == 0, "Files were not cleared from the directory."


if __name__ == '__main__':
    pytest.main()
