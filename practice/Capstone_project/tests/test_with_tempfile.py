import sys
import pytest
from src.parser import generate_records, load_schema


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


@pytest.mark.parametrize("data_schema_str", data_schemas_str)
def test_generate_records_with_different_data_schemas(tmpdir, data_schema_str):
    data_schema_fullpath = str(tmpdir.mkdir("sub").join("/file.json"))
    with open(data_schema_fullpath, 'w') as f:
        f.write(data_schema_str)
    args_from_input = {
        'data_schema': data_schema_fullpath,
        'data_lines': 1,
        'file_count': 0,
        'file_name': 'file_name',
        'prefix': 'random',
        'path_to_save_files': '../output/',
        'multiprocessing': 1,
        'clear_path': True
    }
    args_dict = load_schema(data_schema_fullpath)
    generate_records(args_from_input, args_dict)


if __name__ == 'main':
    pytest.main()
