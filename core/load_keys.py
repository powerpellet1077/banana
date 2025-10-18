#imports keys to be used for services
import json
import os.path
import loguru
from core.get_keys_path import get_keys_path
def load_keys(logger: loguru.logger):
    p = get_keys_path(logger)
    if p and os.path.exists(p):
        try:
            with open(p, "r") as f:
                j = json.load(f)
                logger.info("loaded keys successfully")
                return j
        except Exception as e:
            logger.error("failed to load keys with error: "+str(e))

    else:
        return {}