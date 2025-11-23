import mimetypes
import os
import loguru
def get_mimetype(logger:loguru.logger, filename):
    try:
        ext = os.path.basename(filename).split(".")[1]
    except IndexError:
        logger.warning("file extension appears empty, defaulting to plain/text..")
        return 'plain/text'
    except Exception as e:
        logger.warning(f"error '{str(e)}' attempting to obtain file extension, defaulting to plain/text..")
        return 'plain/text'
    mimetypes.init()
    try:
        logger.info("using mimetype "+mimetypes.types_map["."+ext])
        return mimetypes.types_map["."+ext]
    except KeyError:
        logger.warning("unable to find type for extension "+ext+", defaulting to plain/text..")
        return 'plain/text'