import pytest
import os
import sys
sys.path.insert(1, '..')
from src.utils import generate_records, load_schema, clear_output_directory


data_schemas_str = [
    """
    {
  "date": "timestamp:",
  "name": "str:rand",
  "type": "str:['client', 'partner', 'government']",
  "age": "int:rand(1, 90)"
}
    """
]

processes = [2, 3, 4, 5, 10]


@pytest.mark.parametrize("processes_count", processes)
@pytest.mark.parametrize("data_schema_str", data_schemas_str)
def test_generate_records_with_different_data_schemas(tmpdir, data_schema_str, processes_count):
    data_schema_fullpath = str(tmpdir.mkdir("sub").join("/file.json"))
    with open(data_schema_fullpath, 'w') as f:
        f.write(data_schema_str)
    args_from_input = {
        'data_schema': data_schema_fullpath,
        'data_lines': 1,
        'file_count': 2,
        'file_name': 'file_name',
        'prefix': 'random',
        'path_to_save_files': '../output/',
        'multiprocessing': 2,
        'clear_path': True
    }
    clear_output_directory('../output', '')

    args_dict = load_schema(data_schema_fullpath)
    generate_records(args_from_input, args_dict)

    folder_path = '../output'
    number_of_files = len(os.listdir(folder_path))

    assert number_of_files == 2


if __name__ == '__main__':
    pytest.main()