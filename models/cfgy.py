class Config:
    '''Data convert config class'''

    SPACE_BETWEEN_LETTERS = ""
    SPACE_BETWEEN_WORDS = " "
    NEW_LINE = "\n"

    def __init__(self, config: dict):
        self.amplitude = config.get('amplitude', 16000)
        self.audio_frequency = config.get('audio_frequency', 400)
        self.dictionary = config.get('dictionary', {})
        self.sampling_rate = config.get('sampling_rate', 480000)
        self.unitary_time = config.get('unitary_time', 0.25)

    def get_audio_frequency(self):
        return self.audio_frequency

    def get_unitary_time(self):
        return self.unitary_time

    def get_dictionary(self):
        return self.dictionary
    
    def get_sampling_rate(self):
        return self.sampling_rate
    
    def get_amplitude(self):
        return self.amplitude
    
