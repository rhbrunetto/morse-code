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

    def get_type(self):
        '''Returns data type that is being manipulated'''
        if self.input_file.name.endswith('.txt'):
            return DataType.TEXT
        if self.input_file.name.endswith('.morse'):
            return DataType.MORSE
        if self.input_file.name.endswith('.wav'):
            return DataType.AUDIO
        return DataType.INVALID
