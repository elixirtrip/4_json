import json
import os
import argparse
import sys


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf8') as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(python_object_data):
    print(json.dumps(python_object_data, indent=4))


def get_console_args():
    parser = argparse.ArgumentParser(
        prog='Pretty json',
        description='Script turns compact json data'
        'into a beautiful and easy to read view'
    )

    parser.add_argument(
        '--file_path',
        default='alco_shops.json',
        help='You have to specify a file'
        'path to any file with compact json data'
    )

    return parser.parse_args()


if __name__ == '__main__':
    parse_args = get_console_args()
    python_object_data = load_data(parse_args.file_path)
    if python_object_data is None:
        sys.exit('File not found or data is not in json format')
    pretty_print_json(python_object_data)
