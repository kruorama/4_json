import json
import sys

filepath = sys.argv[1]

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

json_decoded = load_data(filepath)

def pretty_print_json(data):
    print (json.dumps(data, indent=4, ensure_ascii=False))

pretty_print_json(json_decoded)
