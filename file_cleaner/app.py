# first and last name: andrea cantelli
# serial number: 156529
#
# path: /mnt/c/Users/andre/Documents/GitHub/Fogli_Esami/File_Cleaner/app.py

import argparse
import os
import sys


def walk(basepath, extension):
    for filename in os.listdir(basepath):
        path = os.path.join(basepath, filename)

        if os.path.isfile(path) and path.endswith(extension):
            print(f"removing {path}")
            os.remove(path)
        elif os.path.isdir(path):
            walk(path, extension)


def main():
    parser = argparse.ArgumentParser(description="file cleaner")
    parser.add_argument("--path", type=str, required=True, help="directory to clean")
    parser.add_argument(
        "--extension", type=str, required=True, help="file extension to remove"
    )
    args = parser.parse_args()

    path = args.path
    extension = args.extension

    if not os.path.isabs(path):
        print(f"error: {path} must be absolute", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(path):
        print(f"error: {path} does not exist", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(path):
        print(f"error: {path} is not a directory", file=sys.stderr)
        sys.exit(1)

    if not extension.startswith("."):
        print(f"error: {extension} must start with a dot", file=sys.stderr)
        sys.exit(1)

    walk(path, extension)


if __name__ == "__main__":
    main()