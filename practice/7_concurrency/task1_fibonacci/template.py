import os
from random import randint
import sys
from multiprocessing import Pool


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def calculate_fibonacci(ordinal_number: int):
    """Calculate Fibonacci value for an ordinal number and write it to a file"""
    sys.set_int_max_str_digits(0)

    result = fib(ordinal_number)
    filename = f'{ordinal_number}.txt'
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(str(result))


def func1(array: list):

    pool = Pool(processes=os.cpu_count())
    pool.map(calculate_fibonacci, array)

    pool.close()
    pool.join()

import csv

def func2(result_file: str):
    sys.set_int_max_str_digits(0)
    ordinal_values = []
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith('.txt'):
            ordinal_number = int(filename.split('.')[0])
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, 'r') as f:
                fibonacci_value = f.read().strip()
                if fibonacci_value:
                    ordinal_values.append((ordinal_number, int(fibonacci_value)))

    with open(result_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Ordinal Number', 'Fibonacci Value'])
        writer.writerows(ordinal_values)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
