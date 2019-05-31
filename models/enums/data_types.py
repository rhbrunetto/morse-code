from enum import Enum


class DataType(Enum):
    '''Available data types'''
    MORSE = 1,
    TEXT = 2,
    AUDIO = 3,
    INVALID = 4
