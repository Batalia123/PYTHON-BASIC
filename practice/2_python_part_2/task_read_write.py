"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os



def read_from_file(directory, prefix):
    values = []
    for i in range(1, 20):
        filename = f'{prefix}{i}.txt'
        path = os.path.join(directory, filename)
        with open(path) as f:
            values.append(f.read())
    return values



def write_to_file(values):
    with open('files/result.txt', "w") as r:
        r.write(", ".join(values))


