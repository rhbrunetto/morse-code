from configuration import Config
from enums.data_types import DataType
from input import Input


class MiddleLanguageObject:
    '''Middle Language Object for conversions'''
    def __init__(self, input: Input, config: Config):
        self.config = config
        self.input = input
        self.data = None

    def _convert_from_text(self):
        '''Converts from text to middle language'''
        pass

    def _convert_from_audio(self):
        '''Converts from audio to middle language'''
        pass

    def _convert_from_morse(self):
        '''Converts from morse code to middle language'''
        self.data = self.input.get_data()
        return True

    CONVERSION_MAP = {
        DataType.TEXT: _convert_from_text,
        DataType.AUDIO: _convert_from_audio,
        DataType.MORSE: _convert_from_morse,
        DataType.INVALID: None
    }

    def convert_to_mid(self):
        '''Converts from input data type to middle language'''
        fn = MiddleLanguageObject.CONVERSION_MAP.get(self.input.get_type())
        if not fn:
            return Exception
        return fn(self)

    def get_data(self):
        return self.data