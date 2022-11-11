#! usr/bin/env python3
import subprocess
import argparse
import time

parser = argparse.ArgumentParser(description="shut_me_down , a program to program your shudowns easily !")
# we have four time options : seconds , minutes , hours
def parse_arguments():
    parser.add_argument("time",nargs="?",type=int,help="specify the a number in second or minute or hour (should be an integer greater than or equal to 0)")
    parser.add_argument("-m" , "--mode" , choices=["seconds" , "minutes" , "hours"],help="specify the mode")
    parser.add_argument("-c" , "--cancel" , action="store_true",help="a switch to cancel the shutdown operation")
    parser.add_argument("-s" , "--status" , action="store_true" , help="a switch that tells you wether there is a shutdown operation or not")


def is_there_shutdown_operation():
    command_result = subprocess.check_output(["sudo","busctl","get-property","org.freedesktop.login1","/org/freedesktop/login1","org.freedesktop.login1.Manager"
        ,"ScheduledShutdown"])
    if "poweroff" in str(command_result):
        return True
    else:
        return False


def handle_cancelling_operation():
    if is_there_shutdown_operation():
            subprocess.run(["sudo" , "shutdown" , "-c"], stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print("shudown operation cancelled")
    else:
            print("There is no operation no cancel , anyway")


def handle_showing_status():
    if is_there_shutdown_operation():
            print("There is shutdown operation . you can cancel it by -c option")
    else:
            print("There is no operation")


parse_arguments()
args = parser.parse_args()


if vars(args)['time'] != None and vars(args)['mode'] == None:
    print("Error. mode should be specified")
    exit(); 

if vars(args)['time'] == None and vars(args)['mode'] == None:
    if vars(args)['cancel'] == False and vars(args)['status'] ==True:
        handle_showing_status()

    elif vars(args)['status'] == False and vars(args)['cancel'] == True:
        handle_cancelling_operation()    
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
