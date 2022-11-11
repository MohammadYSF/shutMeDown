#! usr/bin/env python3
import subprocess
import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument("time",type=int,help="specify the time in seconds")
args = parser.parse_args()
seconds = args.time
print(f"starting timer of {seconds} seconds")
s = ""
for i in range(seconds):
    s+="."
print(s , end="\r" , flush=True)
for i in range(seconds):
    s = list(s)
    for j in range(0,i+1):
        s[j] = "#"
    s = "".join(s)
    print(s , end="\r" , flush=True)
    time.sleep(1)
print ("\n Done !")