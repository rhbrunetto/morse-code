from enum import Enum


class DataType(Enum):
    '''Available data types'''
    MORSE = '.morse',
    TEXT = '.text',
    AUDIO = '.wav',
    INVALID = None
