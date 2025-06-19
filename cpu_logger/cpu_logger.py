# first and last name: andrea cantelli
# serial number: 156529
#
# path: /mnt/c/Users/andre/Documents/GitHub/ARSCS_Exercises/cpu_logger/cpu_logger.py

import argparse
import psutil
import time
import sys

def main():

    parser = argparse.ArgumentParser(description='cpu logger')

    parser.add_argument('--interval', type=int, required=True)
    args = parser.parse_args()
    interval = args.interval
    while True:
        usage = psutil.cpu_percent()
        print(f"CPU usage: {usage}%", file=sys.stdout)
        time.sleep(interval)
    pass


if __name__ == "__main__":
    main()