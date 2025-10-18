import loguru
import os
import platform
import json
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
    else:
        logger.error("unable to load keys due to operating system. this program is in an early stage and only supports windows currently, please make a pr or issue to bump this issue further.")