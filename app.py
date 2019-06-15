#!/usr/bin/python3

import argparse
import json
import os
import sys

from src.converter import Converter


def run(arguments):
    '''Loads configs and calls procedures'''
    try:
        cfg_file = arguments.config
        if type(arguments.config) == list:
            cfg_file = arguments.config[0]
        conf = json.load(cfg_file)
        if conf:
            Converter(conf, arguments.filename[0]).convert()
    except Exception as e:
        raise Exception(e)


def parse_args():
    '''Argument parser function'''
    arguments_parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description='Morse code text-audio converter.')
    arguments_parser.add_argument(
        'filename',
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
