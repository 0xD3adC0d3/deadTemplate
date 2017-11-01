#!/usr/bin/python

'''
Usage: deadTemplate.py [-h] [-v]

Description

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Enable verbose output
'''

import argparse
import logging
import sys

API_KEY = "CENSORED"

parser = argparse.ArgumentParser(description='Description')

parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output', default=False)

if len(sys.argv) < 3:
    parser.print_help()
    exit(1)

args = parser.parse_args()

level = logging.DEBUG if args.verbose else logging.INFO
logging.basicConfig(level=level, format='[%(asctime)s.%(msecs)03d]  %(message)s', datefmt="%Y-%m-%d %H:%M:%S")