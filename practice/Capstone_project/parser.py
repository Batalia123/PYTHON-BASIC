import argparse
import json
import re
import uuid
import random
import time

parser = argparse.ArgumentParser(prog='test data generator', description='generate test data based on the provided schema')
parser.add_argument('data_schema', type=json.loads, help='pass dataschema guidelines')
parser.add_argument()

#data_schema="{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"str:['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"}"
#args = json.dumps(test)
args = vars(parser.parse_args())  # Pass the JSON string as an argument
print(type(args))
args_dict = list(args.values())[0]

def generate_single_record():
    generated_test = dict()
    for key, value in args_dict.items():
        type_list = value.split(':')
        print(type_list)

        if type_list[0] == 'str':
            if type_list[1] == '':
                generated_test[key] = ''
            elif type_list[1][:5] == 'rand(':
                generated_test[key] = 'error'
            elif type_list[1] == 'rand':
                generated_test[key] = str(uuid.uuid4())
            elif type_list[1][0] == '[':
                choices=type_list[1][1:-1].split(',')
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



print(generate_single_record().items())







#for key, value in args.items():


#print(args.data_schema)