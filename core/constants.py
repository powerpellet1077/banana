#LOGGING
YELLO = "<fg #ffff00>" #yes this is spelled wrong intentionally
YELLO_CLOSE = "</fg #ffff00>"
RED = "<fg #ff0000>"
RED_CLOSE = "</fg #ff0000>"
BLU = "<fg #0000ff>"
BLU_CLOSE = "</fg #0000ff>"
MAGENTA = "<fg #ff00ff>"
MAGENTA_CLOSE = "</fg #ff00ff>"
#PROCESSING
MB = 1048576
GB = 1073741824
#CATBOX
CB_BLACKLISTED_FILES = ("exe", "scr", "cpl", "doc", "jar")
CB_API = "https://catbox.moe/user/api.php"
#FILEBIN
FB_BLACKLISTED_FILES = ["exe"] #PLEASE PLEASE MAKE A PR IF YOU GET ANY MORE ILLEGAL FILE EXTENSION ERRORS
FB_API = "https://filebin.net/"
#LITTERBOX
LB_BLACKLISTED_FILES = ("exe", "scr", "cpl", "doc", "jar")
LB_API = "https://litterbox.catbox.moe/resources/internals/api.php"
#UGUU
UG_BLACKLISTED_FILES = ()
UG_API = "https://uguu.se/upload"
#HELP
HELP_SERVICES = [
    #name, id, temp (y/n), blocked filetypes, requirements, arguments
    ["catbox","cb","not temporary",CB_BLACKLISTED_FILES,"userhash","file"],
    ["litterbox","lb","temporary",LB_BLACKLISTED_FILES,"none","file + time specified"],
    ["filebin","fb","not temporary",FB_BLACKLISTED_FILES,"none","file"],
    ["uguu","ug","temporary",UG_BLACKLISTED_FILES,"none","file"]
]