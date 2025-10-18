#finds applicable carrier for the content
import loguru
import os
from core.constants import MB
from core.check_file_blacklist import check_cb_blacklist
from core.upload import upload_cb
def find_carrier(logger:loguru.logger, path, keys=None):
    if os.path.isfile(path):
        s = os.path.getsize(path)
        if s<MB*200 and not check_cb_blacklist(path):#catbox
            if keys:
                return upload_cb(logger, path, keys)
        else:
            logger.error("no viable service found, make sure it's within the specifications!")
    else:
        logger.error("failed to find carrier due to path not being a file or existing")