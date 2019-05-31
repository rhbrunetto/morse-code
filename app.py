#!/bin/usr/python3

import argparse
import json
import os
import sys

from models.configuration import Config


def run(arguments):
    '''Loads configs and calls procedures'''
    try:
        conf = json.load(arguments.config)
        if conf:
            cfg = Config(conf)
    except Exception as e:
        raise Exception(e)
    print(conf)


def parse_args():
    '''Argument parser function'''
    arguments_parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description='Morse code text-audio converter.')
    arguments_parser.add_argument(
        'positional',
        nargs=1,
        metavar='<file_path>',
        type=argparse.FileType('rt'),
        help=('File to be converted.'))
    arguments_parser.add_argument(
        '-c', '--config',
        nargs=1,
        metavar='<file_path>',
        default='config/config.json',
        type=argparse.FileType('rt'),
        help=('Morse code configuration file. '
              'Default: "conf/config.json"'))
    return arguments_parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    run(arguments=parse_args())
