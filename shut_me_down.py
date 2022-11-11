#! usr/bin/env python3
import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
# we have four time options : seconds , minutes , hours
parser.add_argument("time",nargs="?",type=int,help="specify the a number in second or minute or hour (should be an integer greater than or equal to 0)")
parser.add_argument("-m" , "--mode" , choices=["seconds" , "minutes" , "hours"],help="specify the mode")
parser.add_argument("-c" , "--cancel" , action="store_true")
parser.add_argument("-s" , "--status" , action="store_true")
args = parser.parse_args()

def is_there_shutdown_operation():
    command_result = subprocess.check_output(["sudo","busctl","get-property","org.freedesktop.login1","/org/freedesktop/login1","org.freedesktop.login1.Manager"
        ,"ScheduledShutdown"])
    if "poweroff" in str(command_result):
        return True
    else:
        return False
   


if vars(args)['time'] != None and vars(args)['mode'] == None:
    print("Error. mode should be specified")
    exit(); 

if vars(args)['time'] == None and vars(args)['mode'] == None:
    if vars(args)['cancel'] == False and vars(args)['status'] ==True:
        if is_there_shutdown_operation():
            print("There is shutdown operation . you can cancel it by -c option")
        else:
            print("There is no operation")

    elif vars(args)['status'] == False and vars(args)['cancel'] == True:
        if is_there_shutdown_operation():
            subprocess.run(["sudo" , "shutdown" , "-c"], stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print("shudown operation cancelled")
        else:
            print("There is no operation no cancel , anyway")

    else:
        print("nothing will happen")
    exit()





mode = args.mode
t = args.time

minutes = 0
if (mode == "seconds"):
    minutes = t // 60
    seconds = t%60
    print(f"[+] your system will shutdown in {minutes} minutes and {seconds} seconds")
    time.sleep(seconds)
elif mode == "minutes" :
    minutes = t
    hours = t // 60
    minutes_ = t % 60
    print(f"[+] your system will shutdown in {hours} hours and {minutes_} minues")
elif mode == "hours":
    hours = t
    minutes = t * 60
    print(f"[+] your system will shutdown in {hours} hours")
else:
    print("mode not specified")
subprocess.run(["sudo" , "shutdown" , f"+{minutes}"] , stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)



