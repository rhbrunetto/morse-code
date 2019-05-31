from enums.data_types import DataType


class Input:
    '''Represents an input data'''
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.data = None

    def get_data(self):
        '''Returns contained input data'''
        if not self.data:
            with open(self.input_path, 'r') as f:
                self.data = f.read()
        return self.data

    def get_type(self):
        '''Returns data type that is being manipulated'''
        if self.input_path.endswith('.txt'):
            return DataType.TEXT
        if self.input_path.endswith('.morse'):
            return DataType.MORSE
        if self.input_path.endswith('.wav'):
            return DataType.AUDIO
        return DataType.INVALID