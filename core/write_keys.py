import loguru
from core.load_keys import load_keys
from core.get_keys_path import get_keys_path
import json
def write_keys(logger:loguru.logger, cb=None):
    kk = load_keys(logger)
    if cb:
        if cb != "clear":
            kk["cb"]=cb
        elif cb == "clear":
            try:
                del kk["cb"]
                logger.info("cleared key cb :D")
            except KeyError:
                logger.error("could not clear cb due to no cb key existing!")
            except Exception as e:
                logger.error("could not clear cb due to error: "+str(e))

    kp = get_keys_path(logger)
    if kp:
        try:
            with open(kp, "w") as f:
                json.dump(kk, f)
            logger.critical("successfully written new keys!")
        except Exception as e:
            logger.error("failed to write to keys with error: "+str(e))