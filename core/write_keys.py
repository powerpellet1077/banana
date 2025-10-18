import loguru
from core.load_keys import load_keys
from core.get_keys_path import get_keys_path
import json
def write_keys(logger:loguru.logger, cb=None):
    kk = load_keys(logger)
    if cb:
        kk["cb"]=cb
    kp = get_keys_path(logger)
    if kp:
        try:
            with open(kp, "w") as f:
                json.dump(kk, f)
            logger.critical("successfully written new keys!")
        except Exception as e:
            logger.error("failed to write to keys with error: "+str(e))