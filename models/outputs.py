from .cfgy import Config
from .middle import MiddleLanguageObject


class IOutput:
    '''Output Interface which all outputs are based'''

    def __init__(self, config: Config, mid: MiddleLanguageObject):
        self.data = None
        self.config = config
        self.mid = mid

    def save_to_file(self):
        '''Saves data to a file'''
        raise NotImplementedError

    def convert_from_mid(self):
        '''Converts from middle language to target'''
        raise NotImplementedError


class TextOutput(IOutput):
    def convert_from_mid(self):
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
                            lambda letter: i_dictionary.get(letter),
                            word.split(
                                dictionary.get(Config.SPACE_BETWEEN_LETTERS))
                        )))
                # Concatenate words with SPACE_BETWEEN_WORDS
                converted.append(
                    Config.SPACE_BETWEEN_WORDS.join(converted_line))
            # Concatenate lines with NEW_LINE
            self.data = Config.NEW_LINE.join(converted)
            print('From middle to text:')
            print(self.data)
        except Exception as e:
            print('Failed to convert middle language to text output.')
            return False
        return True


# https: // oz123.github.io/writings/morse-fun-with-python/index.html
# http: // g4akw.blogspot.com/2011/12/python-morse-code-generator.html
class AudioOutput(IOutput):
    def convert_from_mid(self):
        self.data = 'converted_data'
        return True


class MorseOutput(IOutput):
    def convert_from_mid(self):
        self.data = self.mid.get_data()
        return True
