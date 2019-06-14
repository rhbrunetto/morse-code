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
        text_output = TextOutput(self.config, mid)
        text_output.convert_from_mid()
        # text_output.save_to_file()
        # # Audio Output
        # audio_output = AudioOutput(self.config)
        # audio_output.convert_from_mid(mid)
        # audio_output.save_to_file()
        # # Morse Output
        # morse_output = MorseOutput(self.config)
        # morse_output.convert_from_mid(mid)
        # morse_output.save_to_file()
