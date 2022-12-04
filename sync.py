import os
import time
import argparse




parser = argparse.ArgumentParser(description="Copy files modified in the last number of seconds")

parser.add_argument("-s",default=300 ,required=False)
parser.add_argument("-f" ,default="./",required=False)

args = parser.parse_args()


def recursice_scan_dir(dir,seconds):
    for i in os.scandir(dir):
        if i.is_dir():
            recursice_scan_dir(i.path,seconds)
        else:
            last_modify = int(time.time() - i.stat().st_mtime)
            if last_modify < seconds:
                os.system(f"mpremote cp {i.path} :{i.path[2:]}")
            
        
def main():
    print(f"Copying {args.f} modified in the last {args.s} seconds")
    recursice_scan_dir(args.f,args.s)


