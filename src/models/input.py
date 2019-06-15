import os

from .enums.data_types import DataType


class Input:
    '''Represents an input data'''
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None

    def get_data(self):
        '''Returns contained input data'''
        if not self.data:
            self.data = self.input_file.read()
        return self.data
    
    def get_main_name(self):
        return os.path.splitext(self.input_file.name)[0]

    def get_complete_name(self):
        return self.input_file.name
        
    def get_type(self):
        '''Returns data type that is being manipulated'''
        if self.input_file.name.endswith(DataType.TEXT.value[0]):
            return DataType.TEXT
        if self.input_file.name.endswith(DataType.MORSE.value[0]):
            return DataType.MORSE
        if self.input_file.name.endswith(DataType.AUDIO.value[0]):
            return DataType.AUDIO
        return DataType.INVALID
