import json
import sys


def load_json(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return None, json.load(file_handler)
    except json.decoder.JSONDecodeError:
        return 'parse error', None
    except FileNotFoundError:
        return 'no such file', None


def get_pretty_json(json_decoded):
    pretty_json = json.dumps(json_decoded, indent=4, ensure_ascii=False)
    return pretty_json


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Error: no filepath')

    error, json_decoded = load_json(sys.argv[1])

    if json_decoded is None:
        print('Error: {}'.format(error))
    else:
        print(get_pretty_json(json_decoded))
