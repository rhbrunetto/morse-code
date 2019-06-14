class Config:
    '''Data convert config class'''

    SPACE_BETWEEN_LETTERS = ""
    SPACE_BETWEEN_WORDS = " "
    NEW_LINE = "\n"

    def __init__(self, config: dict):
        self.audio_frequency = config.get('audio_frequency', 400)
        self.unitary_time = config.get('unitary_time', 0.25)
        self.dictionary = config.get('dictionary', {})

    def get_audio_frequency(self):
        return self.audio_frequency

    def get_unitary_time(self):
        return self.unitary_time

    def get_dictionary(self):
        return self.dictionary