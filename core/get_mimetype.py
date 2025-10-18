import mimetypes
import os
import loguru
def get_mimetype(logger:loguru.logger, filename):
    try:
        ext = os.path.basename(filename).split(".")[1]
    except Exception as e:
        logger.warning("error decoding extension for file, defaulting to plain/text..")
        return 'plain/text'
    mimetypes.init()
    try:
        logger.info("using mimetype "+mimetypes.types_map["."+ext])
        return mimetypes.types_map["."+ext]
    except KeyError:
        logger.warning("unable to find type for extension "+ext+", defaulting to plain/text..")
        return 'plain/text'