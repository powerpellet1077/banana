import loguru
import os
import platform
import json
from pathlib import Path
from os import geteuid
def get_keys_path(logger: loguru.logger, log=True, w=True):
    if platform.system()=="Windows":
        if "APPDATA" in os.environ:
            p = os.path.join(os.environ["APPDATA"], "banana.json")
            # logger.info(p)
            if not os.path.exists(p):
                if w:
                    logger.warning("unable to find banana.json, making new keys...")
                    with open(p, "w+") as f:
                        f.write(json.dumps({}))
                    return p
                else:
                    logger.warning("unable to find banana.json, returning null")
                    return None
            else:
                return p
        else:
            if log:
                logger.warning("no appdata environment variable found, returning null keys")
            return None
    elif platform.system()=="Linux":
        if geteuid()==0:
            logger.warning("do not run banana as root, this will cause issues!")
        hp = Path.home()
        if hp:
            p = str(hp/".config"/"banana.json")
            if not os.path.exists(p):
                if w:
                    logger.warning("unable to find banana.json, making new keys...")
                    with open(p, "w+") as f:
                        f.write(json.dumps({}))
                    return p
                else:
                    logger.warning("unable to find banana.json, returning null")
                    return None
            else:
                return p
        else:
            if log:
                logger.warning("no home environment variable found, returning null keys")
            return None
    else:
        logger.error(f"operating system '{platform.system()}' not supported, please use a supported operating system or make a pr to further resolve this issue.")