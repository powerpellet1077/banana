import requests
import loguru
import os
import time
import json
from core.constants import CB_API, FB_API
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
        logger.warning("no key specified, the file will live on with the stars..")
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

def upload_fb(logger: loguru.logger, path):
    logger.info("beginning send to filebin, this might take a while")
    f = {'file': (path, open(path, 'rb'), get_mimetype(logger, path))}
    r = requests.post(FB_API, files=f, headers={"filename":os.path.basename(path).strip()})
    if r.status_code==201:
        d=None
        try:
            d = str(json.loads(r.text.strip())["bin"]["id"])
        except KeyError:
            logger.error("failed to decode response due to improper json, try again with catbox")
        except Exception as e:
            logger.error("failed to decode response, error: "+str(e))
        if d:
            return "https://filebin.net/"+d
    else:
        logger.error("failed to upload to filebin D: "+str(r.status_code)+"/"+r.text)
