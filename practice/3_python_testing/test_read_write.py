"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import sys
import random
import tempfile
sys.path.append('/Users/nwykpis/PYTHON-BASIC/practice/2_python_part_2')
from task_read_write import *

def test_read_write():
    numbers = [str(random.randint(0, 100)) for _ in range(20)]
    with tempfile.TemporaryDirectory() as tmpdirname:
        for i, number in enumerate(numbers, start=1):
            with open(f"{tmpdirname}/file_{i}.txt", 'w') as f:
                f.write(number)

        values = read_from_file(tmpdirname, 'file_')
        write_to_file(values, f'{tmpdirname}/result.txt')
        with open(f"{tmpdirname}/result.txt", 'r') as f:
            assert f.read().split(', ') == numbers