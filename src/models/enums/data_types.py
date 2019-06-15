from enum import Enum


class DataType(Enum):
    '''Available data types'''
    MORSE = '.morse',
    TEXT = '.txt',
    AUDIO = '.wav',
    INVALID = None
