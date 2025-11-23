from core.constants import CB_BLACKLISTED_FILES, FB_BLACKLISTED_FILES, LB_BLACKLISTED_FILES, UG_BLACKLISTED_FILES
import os
#copy and paste and copy and paste and copy and paste

def check_cb_blacklist(path):
    f = os.path.basename(path).split(".")
    for o in f:
        if o in CB_BLACKLISTED_FILES:
            return True
    return False

def check_fb_blacklist(path):
    f = os.path.basename(path).split(".")
    for o in f:
        if o in FB_BLACKLISTED_FILES:
            return True
    return False

def check_lb_blacklist(path):
    f = os.path.basename(path).split(".")
    for o in f:
        if o in LB_BLACKLISTED_FILES:
            return True
    return False

def check_ug_blacklist(path):
    f = os.path.basename(path).split(".")
    for o in f:
        if o in UG_BLACKLISTED_FILES:
            return True
    return False