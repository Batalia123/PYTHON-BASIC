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

directory = 'files'
path = 'files/file_1.txt'
values = []
i = 1
for filename in os.listdir(directory):
    with open(path) as f:
        values.append(f.read())
        print(path)
        i = i + 1
        if(i==21):
            break
        path = path[:11] + str(i) + '.txt'

with open('files/result.txt', "w") as r:
    for i in values[:-1]:
        r.write(i + ", ")
    r.write(values[-1])