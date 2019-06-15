from .cfgy import Config
from .enums.data_types import DataType
from .middle import MiddleLanguageObject
from .soundutils import AudioHanlder


class IOutput:
    '''Output Interface which all outputs are based'''

    def __init__(self, config: Config, mid: MiddleLanguageObject):
        self.data = None
        self.config = config
        self.mid = mid
        self.file_name = self.mid.get_input_name() + str(self.get_type())

    def save_to_file(self):
        '''Saves data to a file'''
        raise NotImplementedError

    def convert_from_mid(self):
        '''Converts from middle language to target'''
        raise NotImplementedError
    
    def execute(self):
        '''Converts and saves files'''
        return self.convert_from_mid() and self.save_to_file()

    @staticmethod
    def get_type():
        '''Returns output expected type'''
        raise NotImplementedError


class TextOutput(IOutput):
    @staticmethod
    def get_type():
        return DataType.TEXT.value[0]

    def save_to_file(self):
        print('Saving text file at {}'.format(self.file_name))
        try:
            with open(self.file_name, 'w') as f:
                f.write(self.data)
        except Exception as e:
            print('Fail to save text', e)
            return False
        return True

    def convert_from_mid(self):
        print('Converting to text format...')
        try:
            converted = []
            dictionary = self.config.get_dictionary()
            i_dictionary = {v: k for k, v in dictionary.items()}
            # Split data into lines
            lines = self.mid.get_data().split(Config.NEW_LINE)
            for line in lines:
                converted_line = []
                # Split line into words
                words = line.split(dictionary.get(Config.SPACE_BETWEEN_WORDS))
                for word in words:
                    # Convert each letter and concatenate them 
                    converted_line.append(Config.SPACE_BETWEEN_LETTERS.join(
                        map(
                            lambda letter: i_dictionary.get(letter,''),
                            word.split(
                                dictionary.get(Config.SPACE_BETWEEN_LETTERS))
                        )))
                # Concatenate words with SPACE_BETWEEN_WORDS
                converted.append(
                    Config.SPACE_BETWEEN_WORDS.join(converted_line))
            # Concatenate lines with NEW_LINE
            self.data = Config.NEW_LINE.join(converted)
        except Exception as e:
            print('Failed to convert middle language to text output.', e)
            return False
        return True


class AudioOutput(IOutput):
    def __init__(self, config: Config, mid: MiddleLanguageObject):
        super(AudioOutput, self).__init__(config, mid)
        self.a_handler = AudioHanlder(self.config)

    @staticmethod
    def get_type():
        return DataType.AUDIO.value[0]

    def save_to_file(self):
        print('Saving audio file at {}'.format(self.file_name))
        return self.a_handler.save_wave(
            self.file_name) and self.a_handler.plot(self.file_name)

    def convert_from_mid(self):
        print('Converting to audio format...')
        if self.a_handler.generate_wave(self.mid.get_data()):
            self.data = self.a_handler.get_waves()
            return True
        return False


class MorseOutput(IOutput):
    @staticmethod
    def get_type():
        return DataType.MORSE.value[0]

    def save_to_file(self):
        print('Saving morse file at {}'.format(self.file_name))
        try:
            with open(self.file_name, 'w') as f:
                f.write(self.data)
        except Exception as e:
            print('Fail to save morse', e)
            return False
        return True

    def convert_from_mid(self):
        print('Converting to morse format...')
        self.data = self.mid.get_data()
        return True
