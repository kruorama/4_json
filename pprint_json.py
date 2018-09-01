import json
import sys


filepath = sys.argv[1]


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


json_decoded = load_data(filepath)


def pretty_print_json(json_decoded):
    print(json.dumps(json_decoded, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(json_decoded)
