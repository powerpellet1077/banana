import loguru
import sys
def sink(message):
    r = message.record
    lev = r["level"].name
    text = message
    print(text, end="")
    if lev == "ERROR":
        sys.exit(1)