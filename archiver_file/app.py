# nome e cognome: andrea cantelli
# matricola: 156529
#
# path: /home/andre/file-archiver/app.py

import argparse
import os
import sys
import time
import shutil


def archive(target, sec):

    archive_path=os.path.expanduser('~/archive')
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)
        print(f'Creating directory {archive_path}')
    
    target_directory = os.listdir(target)

    for filename in target_directory:
        file = os.path.join(target, filename)
        if os.path.isfile(file):
            now = time.time()
            last_mod = os.path.getmtime(file)
            interval = now - last_mod

            if interval >= sec:
                print(f'Moving {file} to {archive_path}', file=sys.stdout)
                shutil.move(file, archive_path)
        elif os.path.isdir(file):
            archive(file, sec)

def main():

    parser = argparse.ArgumentParser(description='file archiver')

    parser.add_argument('--path', type=str, required=True, help="path working directory")
    parser.add_argument('--seconds', type=int, required=True, help="integer expiring time")
    args = parser.parse_args()

    path = args.path
    sec = args.seconds

    print(f'Path: {path} \t Seconds: {sec}')

    if not os.path.isabs(path):
        print(f"{path} must be absolute", file=sys.stderr)
        sys.exit(23)

    if not os.path.exists(path):
        print(f"{path} must exist", file=sys.stderr)
        sys.exit(23)

    if not os.path.isdir(path):
        print(f"{path} must be a directory", file=sys.stderr)
        sys.exit(23)

    if sec <= 0:
        print(f"{sec} must be positive", file=sys.stderr)
        sys.exit(23)
    
    archive(path, sec)

    pass


if __name__ == "__main__":
    main()