import requests
import loguru
import os
import time
from core.constants import CB_API
from core.get_mimetype import get_mimetype
def upload_cb(logger: loguru.logger, path, keys):
    logger.info("beginning send to catbox, this might take a while")
    f = open(path, "rb")
    mt = get_mimetype(logger, path)
    if "cb" in keys:
        d = {
            "reqtype": "fileupload",
            "userhash": keys["cb"],
        }
    else:
        d = {
            "reqtype": "fileupload"
        }
    r = requests.post(CB_API, data=d, files={'fileToUpload': (os.path.basename(path), f, mt)})
    if r.status_code==200:
        while True:
            if r.text.strip():
                return r.text.strip()
            else:
                logger.info("waiting for a repsonse from the site...")
                r = requests.post(CB_API, data=d, files={'fileToUpload': (os.path.basename(path), f, mt)})
                time.sleep(0.5)
    else:
        logger.error("failed to upload to catbox D: "+str(r.status_code)+"/"+r.text)