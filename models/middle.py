from .cfgy import Config
from .enums.data_types import DataType
from .input import Input


class MiddleLanguageObject:
    '''Middle Language Object for conversions'''
    def __init__(self, input: Input, config: Config):
        self.config = config
        self.input = input
        self.data = None

        if self.input and self.config:
            self.convert_to_mid()

    def _convert_from_text(self):
        '''Converts from text to middle language'''
        try:
            converted = []
            dictionary = self.config.get_dictionary()
            # Split data into lines
            lines = self.input.get_data().lower().split(Config.NEW_LINE)
            for line in lines:
                converted_line = []
                # Split line into words
                words = line.split(Config.SPACE_BETWEEN_WORDS)
                for word in words:
                    # Convert each letter and concatenate them
                    converted_line.append(
                        dictionary.get(Config.SPACE_BETWEEN_LETTERS).join(
                            map(
                                lambda letter: dictionary.get(letter),
                                [w for w in word]
                            )))
                # Concatenate words with SPACE_BETWEEN_WORDS
                converted.append(
                    dictionary.get(Config.SPACE_BETWEEN_WORDS).join(
                        converted_line))
            # Concatenate lines with NEW_LINE
            self.data = Config.NEW_LINE.join(converted)
            print('From text to middle:')
            print(self.data)
        except Exception as e:
            print('Failed to convert text input to middle language.')
            return False
        return True

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
            raise Exception
        return fn(self)

    def get_data(self):
        return self.data