class Converter:
    '''Responsible for manipulate data types and handle final files'''
    def __init__(self, config, input_file):
        self.audio_frequency = config.get('audio_frequency', 400)
        self.dictionary = config.get('dictionary', {})
        self.unitary_time = config.get('unitary_time', 0.25)
        self.input_file = input_file

    # def convert(self):
        