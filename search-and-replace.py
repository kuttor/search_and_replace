#!/usr/bin/env python

"""
Search and Replace

Usage:
    search_and_replace.py (-b | --bucket) <bucket> (-e | --env) <env> (-f | --filename) <filename> [--dryrun]
    search_and_replace.py (-h | --help)
    search_and_replace.py (-v | --version)

Options:
    -d --dryrun              Executes a theoretical run
    -v -version                 Show version
    -h --help                Show this Screen

Examples:
    search_and_replace.py -b hli-processed-rad-pdx -e dev3 -f ebstags.py
"""

from boto3 import client
from boto3 import resource
from pathlib import Path
from docopt import docopt

# about
__author__ = "Andrew Kuttor "
__maintainer__ = "Andrew Kuttor"
__email__ = "akuttor@gmail.com"
__version__ = "0.1.0"


# list all key paths within environment
def list_paths(args):
    c = client('s3')
    r = c.list_objects(Bucket=bucket, Prefix=env)
    l = [Path(key['Key']).parent for k in r['Contents'] if filename in k['Key']]
    return l


# uploads file based on path retrieved by list_paths
def upload_file(args):
    r = resource('s3')
    for i in list_paths(bucket, env, filename):
        r.Object(i, filename).upload_file(filename)

# main
def main():
    arguments = docopt(__doc__, version='Search and Replace 1.0')
    # upload_file(arguments)
    # list_paths(arguments)
    print arguments

if __name__ == '__main__':
    main()
