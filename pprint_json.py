import json
import sys


def pretty_print_json(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            json_decoded = json.load(file_handler)
    except Exception:
        exit(print("It's not a valid JSON"))

    print(json.dumps(json_decoded, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit(print('Please add a path to JSON file'))

    pretty_print_json(sys.argv[1])
