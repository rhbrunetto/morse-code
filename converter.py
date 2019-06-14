from models.cfgy import Config
from models.middle import MiddleLanguageObject
from models.input import Input
from models.outputs import AudioOutput, MorseOutput, TextOutput


class Converter:
    '''Responsible for manipulate data types and handle final files'''
    def __init__(self, config: dict, input_file):
        self.config = Config(config)
        self.input_file = Input(input_file)

    def convert(self):
        mid = MiddleLanguageObject(self.input_file, self.config)
        # Text Output
        if self.input_file.get_type() != TextOutput.get_type():
            TextOutput(self.config, mid).execute()
        # # Audio Output
        if self.input_file.get_type() != AudioOutput.get_type():
            AudioOutput(self.config, mid).execute()
        # # Morse Output
        if self.input_file.get_type() != MorseOutput.get_type():
            MorseOutput(self.config, mid).execute()
