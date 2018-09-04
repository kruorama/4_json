import json
import sys


def pretty_print_json(filepath):

    try:
        with open(filepath, 'r') as file_handler:
            json_decoded = json.load(file_handler)
    except json.decoder.JSONDecodeError:
        return None

    pretty_json = json.dumps(json_decoded, indent=4, ensure_ascii=False)
    return pretty_json


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit(print('Please add a path to JSON file'))

    pretty_json = pretty_print_json(sys.argv[1])
    if pretty_json == None:
        print("It's not a valid JSON")
    else:
        print(pretty_json)
