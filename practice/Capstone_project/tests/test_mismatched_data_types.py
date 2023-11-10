import sys
import os
import pytest
from src.parser import generate_records, load_schema



data_schemas = [
    """
    {
  "date": "timestamp:rand(1,2)",
  "name": "timestamp:rand",
  "type": "int:str:7",
  "age": "int:head"
}
    """
]


@pytest.mark.parametrize("data_schema", data_schemas)
def test_generate_records_with_different_data_schemas(data_schema):
    args_from_input = {
        'data_schema': data_schema,
        'data_lines': 1,
        'file_count': 0,
        'file_name': 'file_name',
        'prefix': 'random',
        'path_to_save_files': '../output/',
        'multiprocessing': 1,
        'clear_path': True
    }
    args_dict = load_schema(data_schema)
    generate_records(args_from_input, args_dict)


if __name__ == '__main__':
    pytest.main()
