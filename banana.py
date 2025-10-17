import argparse
#ARGUMENTS
parser = argparse.ArgumentParser(description="upload and share files quickly with mutliple services")
parser.add_argument("filename", help="path of target file to upload")
parser.add_argument("-s", "--service", help="select target service")
args = parser.parse_args()



