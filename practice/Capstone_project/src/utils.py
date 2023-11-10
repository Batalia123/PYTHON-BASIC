def parse_arguments():
    parser = argparse.ArgumentParser(prog='test data generator',
                                     description='generate test data based on the provided schema')
    parser.add_argument('--data_schema', type=str, dest='data_schema', help='pass dataschema guidelines or location')
    parser.add_argument('--data_lines', dest='data_lines', type=int, help='pass number of lines in each file')
    parser.add_argument('--file_count', dest='file_count', type=int, help='pass number of output files')
    parser.add_argument('--file_name', dest='file_name', type=str, help='pass template output file name')
    parser.add_argument('--prefix', type=str, choices=['count', 'random', 'uuid'], dest='prefix',
                        help='pass file prefix when more than one file')
    parser.add_argument('--path_to_save_files', dest='path_to_save_files', type=str,
                        help='pass path to save output files')
    parser.add_argument('--clear_path', action='store_true')
    parser.add_argument('--multiprocessing', type=int, dest='multiprocessing',
                        help='pass number of processes used to create files')

    return parser.parse_args()


def load_schema(data_schema_from_input):
    if data_schema_from_input[-4:] == 'json':
        with open(data_schema_from_input) as json_file:
            return json.load(json_file)
    return json.loads(data_schema_from_input)


def generate_single_record(schema_dict):
    generated_test = dict()
    for key, value in schema_dict.items():
        type_list = value.split(':')

        if type_list[0] == 'str':
            if type_list[1] == '':
                generated_test[key] = ''
            elif type_list[1][:5] == 'rand(':
                logging.error("random value within bounds can't be string, setting it to empty string")
                generated_test[key] = ''
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
                try:
                    generated_test[key] = int(random.choice(choices))
                except ValueError:
                    logging.error(f"{type_list[1]} could not be converted to string")
            else:
                try:
                    generated_test[key] = int(type_list[1])
                except ValueError:
                    logging.error(f"{type_list[1]} could not be converted to string")
        elif type_list[0] == 'timestamp':
            if type_list[1]:
                logging.warning("Timestamp does not support any values and it will be ignored")
            if type_list[1][:5] == 'rand(':
                logging.error("random value within bounds can't be timestamp")
            generated_test[key] = time.time()

    return generated_test


def create_file(path_to_save_files, file_name, line_count, prefix, start, end, schema_dict):
    for file in range(start, end):
        if prefix == 'count':
            complete_name = os.path.join(path_to_save_files, f"{file_name}{file + 1}.json")
        elif prefix == 'uuid':
            complete_name = os.path.join(path_to_save_files, f"{file_name}{uuid.uuid4()}.json")
        elif prefix == 'random':
            complete_name = os.path.join(path_to_save_files, f"{file_name}{random.randint(1, 1000)}.json")

        logging.info(f"Creating file: {complete_name}")

        with open(complete_name, "w") as f:
            for _ in range(int(line_count)):
                content = json.dumps(generate_single_record(schema_dict), indent=4)
                f.write(content + '\n')
                print(content)

        logging.info(f"File {complete_name} created successfully")


def clear_output_directory(path_to_save_files, file_name):
    files = os.listdir(path_to_save_files)
    for file in files:
        if file.startswith(file_name):
            file_path = os.path.join(path_to_save_files, file)
            os.remove(file_path)


def generate_records(args, schema_dict):
    logging.info('Starting to get the parameters')
    prefix = args['prefix']
    file_count = max(0, int(args['file_count']))
    path_to_save_files = args['path_to_save_files']
    file_name = args['file_name']
    process_count = max(1, int(args['multiprocessing']))
    line_count = int(args['data_lines'])
    files_per_process = file_count // process_count
    logging.info('Parameters fetched')

    if args['clear_path']:
        logging.info("Starting to clear the output directory")
        clear_output_directory(path_to_save_files, file_name)
        logging.info("Output directory cleared")

    logging.info(f"Number of files is {file_count}")
    if file_count == 0:
        logging.info("Writing output to terminal")
        for _ in range(int(line_count)):
            content = json.dumps(generate_single_record(schema_dict), indent=4)
            print(content)
        logging.info("Output generated")
        return

    logging.info(f"Number of processes to create the output files is {process_count}")

    processes = []
    for i in range(process_count):
        logging.info("Starting to create files")
        start = i * files_per_process
        end = (i + 1) * files_per_process if i < file_count - 1 else file_count

        process = multiprocessing.Process(target=create_file,
                                          args=(
                                          path_to_save_files, file_name, line_count, prefix, start, end, schema_dict))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    logging.info("Output generated")