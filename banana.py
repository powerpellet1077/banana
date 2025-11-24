#banana made by powerpellet1077
#INFO
__author__ = "powerpellet1077"
__version__ = "1.0.0"
__status__ = "spaghetti code"
#ARGUMENTS
import argparse
parser = argparse.ArgumentParser(description="upload files to multiple providers quick and painless")
parser.add_argument("-f", "--filename", help="path of target file to upload")
parser.add_argument("-s", "--service", help="select target service w/ service id")
parser.add_argument("-k", "--key", help="save key/userhash for service usage (catbox)")
parser.add_argument("-t", "--time", help="time set for temporary uploads (only used currently for litterbox)")
parser.add_argument("-l", "--list", help="list available services", action='store_true')
parser.add_argument("-p", "--prefer", help="prefer a temporary/non temporary file service (use temp or notemp to declare which perferred file upload service)")
args = parser.parse_args()
#INITALIZATION
import loguru
from core.load_keys import load_keys
from core.find_carrier import find_carrier
from core.logger_sink import sink
from core.write_keys import write_keys
from core.make_service_list import make_service_list
from core.constants import *
from sys import stdout
log = loguru.logger
#really inefficient, someone make this look nicer please
log.remove()
log.add(sink, colorize=True, format=YELLO+"[{module}]"+YELLO_CLOSE+"<level>[{level}] {message}</level>")
log.level("WARNING", color=YELLO)
log.level("ERROR", color=RED)
log.level("INFO", color=BLU)
log.level("CRITICAL", color=MAGENTA)
#LOADING

if args.list:
    make_service_list(log)
elif args.key:
    if args.service:
        if args.service=="cb":
            write_keys(log, cb=args.key)
    else:
        log.error("when declaring a key, please use the service flag to declare which service it should apply to")
elif args.filename:
    pm = None
    if args.prefer:
        if args.perfer.lower() in ["temp", "t"]:
            pm="temp"
            log.info("preferring temporary services")
        elif args.perfer.lower() in ["notemp", "nt"]:
            pm="notemp"
            log.info("preferring non-temporary services")
        else:
            log.error(f"perfer syntax incorrect. flag can only be 'temp', 't', 'notemp' or 'nt', not '{args.perfer}'")
    k = load_keys(log)
    if args.service:
        fc = find_carrier(log, args.filename, k, p=args.service, t=args.time, tp=pm)
    else:
        fc = find_carrier(log, args.filename, k, t=args.time, tp=pm)
    if fc:
        log.critical("uploaded: "+fc)
    else:
        log.critical("no link generated")
else:
    log.error("please provide a value")