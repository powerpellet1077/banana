#banana made by powerpellet1077
#INFO
__author__ = "powerpellet1077"
__version__ = "1.0.0"
__status__ = "spaghetti code"
#ARGUMENTS
import argparse
parser = argparse.ArgumentParser(description="upload and share files quickly with mutliple services")
parser.add_argument("-f", "--filename", help="path of target file to upload")
parser.add_argument("-s", "--service", help="select target service")
parser.add_argument("-k", "--key", help="save key for service usage (catbox and dropbox)")
parser.add_argument("-t", "--time", help="time set for temporary uploads, please only choose from options as said on the readme (you can ignore this argument if you are not using temporary file hosting)")
args = parser.parse_args()
#INITALIZATION
import loguru
from core.load_keys import load_keys
from core.find_carrier import find_carrier
from core.logger_sink import sink
from core.write_keys import write_keys
from core.constants import *
from sys import stdout
log = loguru.logger
#really inefficient, someone make this look nicer please
log.remove()
log.add(sink, colorize=True, format=YELLO+"{file}/{line}|{time}"+YELLO_CLOSE+"|<level>[{level}] {message}</level>")
log.level("WARNING", color=YELLO)
log.level("ERROR", color=RED)
log.level("INFO", color=BLU)
log.level("CRITICAL", color=MAGENTA)
#LOADING
if args.key:
    if args.service:
        if args.service=="cb":
            write_keys(log, cb=args.key)
    else:
        log.error("when declaring a key, please use the service flag to declare which service it should apply to")
elif args.filename:
    k = load_keys(log)
    if args.service:
        fc = find_carrier(log, args.filename, k, p=args.service, t=args.time)
    else:
        fc = find_carrier(log, args.filename, k, t=args.time)
    if fc:
        log.critical("uploaded: "+fc)
    else:
        log.critical("no link generated")
else:
    log.error("please provide a value")