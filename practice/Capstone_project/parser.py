import argparse
import json
import re
import uuid
import random
import time
import os
import multiprocessing

parser = argparse.ArgumentParser(prog='test data generator',
                                 description='generate test data based on the provided schema')
parser.add_argument('--data_schema', type=str, help='pass dataschema guidelines or location')
parser.add_argument('--data_lines', default=1, type=int, help='pass number of lines in each file')
parser.add_argument('--file_count', default=0, type=int, help='pass number of output files')
parser.add_argument('--file_name', default='file_number_', type=str, help='pass template output file name')
parser.add_argument('--file_prefix', type=str, choices=['count', 'random', 'uuid'],
                    help='pass file prefix when more than one file')
parser.add_argument('--path_to_save_files', default='./output/', type=str, help='pass path to save output files')
parser.add_argument('--clear_path', action='store_true')
parser.add_argument('--multiprocessing', type=int, default=1, help='pass number of processes used to create files')

# data_schema="{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"str:['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"}"
# args = json.dumps(test)
args = parser.parse_args().data_schema  # Pass the JSON string as an argument

if args[-4:] == 'json':
    with open(args) as json_file:
        args_dict = json.load(json_file)
        print(args_dict)
else:
    print(False)
    args_dict = json.loads(args)


def create_file(path_to_save_files, file_name, line_count, prefix, start, end):
    for i in range(start, end):
        if prefix == 'count':
            completeName = os.path.join(path_to_save_files, file_name + str(file + 1) + ".json")
        elif prefix == 'uuid':
            completeName = os.path.join(path_to_save_files, file_name + str(uuid.uuid4()) + ".json")
        elif prefix == 'random':
            completeName = os.path.join(path_to_save_files, file_name + str(random.randint(1, 1000)) + ".json")
        with open(completeName, "w") as f:
            print(completeName)
            for line in range(line_count):
                content = json.dumps(generate_single_record(), indent=4)
                f.write(content + '\n')
                print(content)


def generate_single_record():
    generated_test = dict()
    for key, value in args_dict.items():
        type_list = value.split(':')

        if type_list[0] == 'str':
            if type_list[1] == '':
                generated_test[key] = ''
            elif type_list[1][:5] == 'rand(':
                generated_test[key] = 'error'
            elif type_list[1] == 'rand':
                generated_test[key] = str(uuid.uuid4())
            elif type_list[1][0] == '[':
                choices = type_list[1][1:-1].split(',')
                generated_test[key] = random.choice(choices)
            else:
                generated_test[key] = type_list[1]
        elif type_list[0] == 'int':
            if type_list[1] == '':
                generated_test[key] = None
            elif type_list[1][:5] == 'rand(':
                split_pattern = r'[(,)]'
                bounds = re.split(split_pattern, type_list[1])
                generated_test[key] = random.randint(int(bounds[1]), int(bounds[2]))
            elif type_list[1] == 'rand':
                generated_test[key] = random.randint(0, 1000)
            elif type_list[1][0] == '[':
                choices = type_list[1][1:-1].split(',')
                generated_test[key] = int(random.choice(choices))
            else:
                generated_test[key] = int(type_list[1])
        elif type_list[0] == 'timestamp':
            generated_test[key] = time.time()
    return generated_test


def generate_records():
    prefix: object = parser.parse_args().file_prefix
    file_count = parser.parse_args().file_count
    path_to_save_files = parser.parse_args().path_to_save_files
    file_name = parser.parse_args().file_name
    process_count = parser.parse_args().multiprocessing
    files_per_process = file_count // process_count

    files = os.listdir(path_to_save_files)
    for file in files:
        if file.startswith(file_name):
            file_path = os.path.join(path_to_save_files, file)
            os.remove(file_path)

    for file in range(file_count):
        line_count = parser.parse_args().data_lines

    processes = []
    for i in range(process_count):
        start = i * files_per_process
        end = (i + 1) * files_per_process if i < file_count - 1 else file_count
        process = multiprocessing.Process(target=create_file, args=(path_to_save_files, file_name, line_count, prefix, start, end))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    generate_records()

# for key, value in args.items():


# print(args.data_schema)
