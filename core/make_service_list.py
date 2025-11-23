import loguru
from core.constants import HELP_SERVICES

def format_list(l):
    bss = ""
    if len(l)<=0:
        return "none"
    elif len(l)==1:
        return l[0]
    for o in l:
        bss+=f"{o}, "
    return bss[:-2]

def make_service_list(logger: loguru.logger):
    bs = ">> SERVICES <<\n    name/[id]    |    temporary    |    disallowed filetypes    |    requirements    |       arguments       |\n"
    for o in HELP_SERVICES:
        #bs += f"{o[0]}/[{o[1]}]{(11-len(f"{o[0]}/[{o[1]}]"))*" "}|{o[2]}{(13-len(o[2]))*" "}|{str(o[3])}{(24-len(str(o[3])))*" "}|{str(o[4])}{(16-len(str(o[4])))*" "}|{str(o[5])}{(13-len(str(o[5])))*" "}|\n" #mistakes were made
        bs+=f"{str(o[0]+"/["+o[1]+"]"):<17}|{o[2]:<17}|{format_list(o[3]):<28}|{o[4]:<20}|{o[5]:<23}|\n"
    logger.critical(bs)