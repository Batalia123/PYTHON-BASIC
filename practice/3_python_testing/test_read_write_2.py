"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import sys
import os
import random
sys.path.append('/Users/nwykpis/PYTHON-BASIC/practice/2_python_part_2')
from task_read_write_2 import *
import tempfile


def test_read_write_2_little():
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        words = random_words()
        generate_words(words, 20, tmpdirname)

        with open(f"{tmpdirname}/file1.txt", 'r') as f1, open(f"{tmpdirname}/file2.txt", 'r') as f2:
            contents1 =  f1.read().replace('\\', '')
            contents2 = f2.read().replace(',', '')
            words: str = ''.join(words)
            assert contents1 == words
            assert contents2 == words

def test_read_write_2_more():
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        words = random_words()
        generate_words(words, 200, tmpdirname)

        with open(f"{tmpdirname}/file1.txt", 'r') as f1, open(f"{tmpdirname}/file2.txt", 'r') as f2:
            contents1 =  f1.read().replace('\\', '')
            contents2 = f2.read().replace(',', '')
            words: str = ''.join(words)
            assert contents1 == words
            assert contents2 == words








