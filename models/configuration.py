class Config:
    '''Data convert config class'''
    def __init__(self, config: dict):
        self.audio_frequency = config.get('audio_frequency')
        self.unitary_time = config.get('unitary_time')
        self.dictionary = config.get('dictionary')

    def get_audio_frequency(self):
        return self.audio_frequency

    def get_unitary_time(self):
        return self.unitary_time

    def get_dictionary(self):
        return self.dictionary