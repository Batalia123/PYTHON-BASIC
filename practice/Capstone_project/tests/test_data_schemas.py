import sys
from datetime import date

import pytest
import os

sys.path.insert(1, '..')

from parser import generate_records, load_schema

data_schemas = ['../jsons/test' + str(i) + '.json' for i in range(1, 5)]

@pytest.mark.parametrize("data_schema", data_schemas)
def test_generate_records_with_different_data_schemas(data_schema):
    args_from_input = {
        'data_schema': data_schema,
        'data_lines': 1,
        'file_count': 0,
        'file_name': 'file_name',
        'file_prefix': 'random',
        'path_to_save_files': '../output/',
        'multiprocessing': 1,
        'clear_path': True
    }
    args_dict = load_schema(data_schema)
    generate_records(args_from_input, args_dict)

if __name__ == '__main__':
    pytest.main([__file__])