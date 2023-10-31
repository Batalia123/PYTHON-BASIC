import os
import pytest
import json
from your_script_name import create_file, clear_output_directory

# Assuming you have the necessary imports and configurations for the script.

# Define the test case for checking if files are saved to the disk
def test_file_saving(tmpdir):
    # Temporary directory for testing
    temp_dir = tmpdir.mkdir("test_files")

    # Define test parameters
    path_to_save_files = temp_dir
    file_name = "test_file"
    line_count = 5
    prefix = "count"
    start = 0
    end = 1
    args_dict = {"key1": "value1", "key2": "value2"}  # Replace with your actual args_dict

    # Call the function to create a file
    create_file(path_to_save_files, file_name, line_count, prefix, start, end, args_dict)

    # Check if the file is created
    file_path = os.path.join(path_to_save_files, f"{file_name}{start + 1}.json")
    assert os.path.isfile(file_path)

    # Clean up the temporary directory
    clear_output_directory(path_to_save_files, file_name)

    # Check if the file is deleted
    assert not os.path.isfile(file_path)