import os
import sys
sys.path.insert(1, '..')
from parser import create_file, clear_output_directory

def test_file_saving(tmpdir):
    temp_dir = tmpdir.mkdir("test_files")

    path_to_save_files = temp_dir
    file_name = "test_file"
    line_count = 5
    prefix = "count"
    start = 0
    end = 1
    args_dict = {"key1": "value1", "key2": "value2"}

    create_file(path_to_save_files, file_name, line_count, prefix, start, end, args_dict)

    file_path = os.path.join(path_to_save_files, f"{file_name}{start + 1}.json")
    assert os.path.isfile(file_path)

    clear_output_directory(path_to_save_files, file_name)

    assert not os.path.isfile(file_path)