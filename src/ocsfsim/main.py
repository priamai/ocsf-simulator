"""
Module Docstring
"""

__author__ = "Paolo Di Prodi"
__version__ = "0.1.0"
__license__ = "Apache GPL 2"

import argparse
import os
import logging
from pathlib import Path
from .utils import get_base_event
import time
from random import randrange
from socfaker import SocFaker

def current_milli_time():
    return round(time.time() * 1000)

# create logger
logger = logging.getLogger('sigmatau')
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def main(args):
    sc = SocFaker()

    if args.console:
        logger.info("Events to console")
        bevent = get_base_event()

        for i in range(args.total-1):
            bevent['time'] = current_milli_time()
            bevent['message'] = sc.logs.windows.sysmon()
            bevent['data'] = {}
            bevent['enrichments'] = {}
            bevent['observables'] = []
            bevent['Count'] =randrange(1000)
            bevent['metadata']['logged_time'] = bevent['time']
            logger.info(bevent)

def run():
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument('-folder', type=dir_path)

    # Optional argument flag which defaults to False
    parser.add_argument("-c", "--console", action="store_true", default=True)
    parser.add_argument("-n", "--total",type=int, default=10)
    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)

if __name__ == "__main__":
    run()