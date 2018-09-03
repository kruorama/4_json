import json
import sys


if len(sys.argv) <=1:
    print('Please add a path to JSON file')
    exit()

filepath = sys.argv[1]


if filepath.split(".")[-1] != "json":
    print("It's not a JSON")
    exit()


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


json_decoded = load_data(filepath)


def pretty_print_json(json_decoded):
    print(json.dumps(json_decoded,
            indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(json_decoded)
