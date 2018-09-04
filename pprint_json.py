import json
import sys


def load_json(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        return None


def pretty_print_json(json_decoded):
    pretty_json = json.dumps(json_decoded, indent=4, ensure_ascii=False)
    return pretty_json


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        filepath = None
    else:
        filepath = load_json(sys.argv[1])

    if filepath is None:
        print("Please add a path to a valid JSON file")
    else:
        print(pretty_print_json(filepath))
