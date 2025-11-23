#finds applicable carrier for the content
import loguru
import os
from core.constants import MB, GB
from core.check_file_blacklist import check_cb_blacklist, check_fb_blacklist, check_lb_blacklist, check_ug_blacklist
from core.upload import upload_cb, upload_fb, upload_lb, upload_ug


def find_carrier(logger:loguru.logger, path, keys=None, p=None, t=None, tp=None):
    if os.path.isfile(path):
        s = os.path.getsize(path)
        if not p:
            if s<MB*200 and not check_cb_blacklist(path) and tp!="temp":#catbox
                if keys:
                    try:
                        return upload_cb(logger, path, keys)
                    except Exception as e:
                        logger.error("error uploading to catbox, error: "+str(e))
                else:
                    logger.warning("no keys found, this may cause issues")
            if s<GB and not check_lb_blacklist(path) and tp!="notemp":#litterbox
                try:
                    return upload_lb(logger, path, t)
                except Exception as e:
                    logger.error("error uploading to litterbox, error: "+str(e))
            elif not check_fb_blacklist(path) and tp!="temp": #filebin
                try:
                    logger.warning("filebin support is still in development and may not work as indented, so please expect issues")
                    return upload_fb(logger, path)
                except Exception as e:
                    logger.error("error uploading to filebin, error: "+str(e))
            elif not check_ug_blacklist(path) and tp!="notemp": #uguu
                try:
                    return upload_ug(logger, path)
                except Exception as e:
                    logger.error("error uploading to uguu, error: " + str(e))
            else:
                logger.error("no viable service found for select file, please try again with another file.")
        else:
            if p == "cb":  # catbox
                if s<MB * 200 and not check_cb_blacklist(path):
                    if keys:
                        try:
                            return upload_cb(logger, path, keys)
                        except Exception as e:
                            logger.error("error uploading to catbox, error: "+str(e))
                else:
                    logger.error("file does not meet catbox specifications, please try another service.")
            elif p == "lb": #litterbox
                if s<GB and not check_lb_blacklist(path):
                    try:
                        return upload_lb(logger, path, t)
                    except Exception as e:
                        logger.error("error uploading to litterbox, error: "+str(e))
                else:
                    logger.error("file does not meet litterbox specifications, please try another service.")
            elif p == "fb": #filebin
                if not check_fb_blacklist(path):
                    try:
                        return upload_fb(logger, path)
                    except Exception as e:
                        logger.error("error uploading to filebin, error: "+str(e))
                else:
                    logger.error("file does not meet catbox specifications, please try another service.")
            elif p == "ug": #uguu
                if not check_ug_blacklist(path):
                    try:
                        return upload_ug(logger, path)
                    except Exception as e:
                        logger.error("error uploading to uguu, error: "+str(e))
            else:
                logger.error("illegal service selected, please choose a service that exists :P")

    else:
        logger.error("failed to find carrier due to path not being a file or existing")
