#! usr/bin/env python3
import subprocess
import argparse

parser = argparse.ArgumentParser()
# we have four time options : seconds , minutes , hours
parser.add_argument("time" , type=int,help="specify the a number in second or minute or hour (should be an integer greater than or equal to 0)")
parser.add_argument("-m" , "--mode" , choices=["seconds" , "minutes" , "hours"],help="specify the mode")
args = parser.parse_args()
# mode = args.mode
# t = args.time



