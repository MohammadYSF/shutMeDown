#! usr/bin/env python3
import subprocess
import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument("time",type=int)
args = parser.parse_args()
print(f"starting timer of {args.time} seconds")
for _ in range(args.time):
    print("." , end="" , flush=True)
    time.sleep(1)
print ("\n Done !")