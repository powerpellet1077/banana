#finds applicable carrier for the content
import loguru
import os
from core.constants import MB
from core.check_file_blacklist import check_cb_blacklist, check_fb_blacklist
from core.upload import upload_cb, upload_fb
def find_carrier(logger:loguru.logger, path, keys=None, p=None):
    if os.path.isfile(path):
        s = os.path.getsize(path)
        if not p:
            if s<MB*200 and not check_cb_blacklist(path):#catbox
                if keys:
                    try:
                        return upload_cb(logger, path, keys)
                    except Exception as e:
                        logger.error("error uploading to catbox, error: "+str(e))
            elif not check_fb_blacklist(path): #filebin
                try:
                    logger.warning("filebin support is still in development and may not work as indented, so please expect issues")
                    return upload_fb(logger, path)
                except Exception as e:
                    logger.error("error uploading to filebin, error: "+str(e))
            else:
                logger.error("no viable service found for select file, please try again with another file.")
        else:
            if p == "cb":  # catbox
                if s < MB * 200 and not check_cb_blacklist(path):
                    if keys:
                        try:
                            return upload_cb(logger, path, keys)
                        except Exception as e:
                            logger.error("error uploading to catbox, error: " + str(e))
                else:
                    logger.error("file does not meet catbox specifications, please try another service.")
            elif p == "fb": #filebin
                if not check_fb_blacklist(path):
                    try:
                        return upload_fb(logger, path)
                    except Exception as e:
                        logger.error("error uploading to filebin, error: "+str(e))
                else:
                    logger.error("file does not meet catbox specifications, please try another service.")
            else:
                logger.error("illegal service selected, please choose a service that exists :P")
    else:
        logger.error("failed to find carrier due to path not being a file or existing")
