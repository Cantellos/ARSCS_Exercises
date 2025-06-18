# first and last name:
# serial number:
#
# path:

import argparse
import os
import sys

def clean(path, extension):
    print(f"Clean {path}")
    for file in os.listdir(path):
        path_file = os.path.join(path, file)
        if not os.path.isdir(path_file):
                if path_file.endswith(extension):
                    print(f"Rimuovo {path_file}")
                    os.remove(path_file)
        else:
            clean(path_file, extension)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required = True)
    parser.add_argument('--extension', required = True)
    args = parser.parse_args()
    print(f"Path: {args.path} , Extension: {args.extension}")
    
    if not os.path.isabs(args.path):
        print("Path non assoluto")
        sys.exit(1)
    if not os.path.exists(args.path):
        print("Path non esiste")
        sys.exit(1)
    if not os.path.isdir(args.path):
        print("Path non è una cartella")
        sys.exit(1)
    if not args.extension.startswith('.'):
        print("Extension non inizia con .")
        sys.exit(1)
        
    clean(args.path, args.extension)
        
    pass
            
if __name__ == "__main__":
    main()
