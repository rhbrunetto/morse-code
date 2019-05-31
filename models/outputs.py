from configuration import Config
from middle import MiddleLanguageObject


class IOutput:
    '''Output Interface which all inputs are based'''
    def __init__(self):
        self.data = None

    def save_to_file(self):
        '''Saves data to a file'''
        return NotImplementedError

    def convert_from_mid(self, mid: MiddleLanguageObject):
        '''Converts from middle language to target'''
        return NotImplementedError


class TextOutput(IOutput):
    def convert_from_mid(self, mid: MiddleLanguageObject):
        return 'ha'


class AudioOutput(IOutput):
    def __init__(self, config: Config):
        self.config = config

    def convert_from_mid(self, mid: MiddleLanguageObject):
        return 'ha'


class MorseOutput(IOutput):
    def convert_from_mid(self, mid: MiddleLanguageObject):
        self.data = mid.get_data()
        return True