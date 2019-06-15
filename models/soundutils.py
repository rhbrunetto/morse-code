import struct
import wave

import matplotlib.pyplot as plt
import numpy as np

from .cfgy import Config


class AudioHanlder():
    '''Represents an audio handler with basic functions'''
    def __init__(self, config: Config):
        self.frequency = config.get_audio_frequency()
        self.sampling_rate = config.get_sampling_rate()
        self.duration = config.get_unitary_time()
        self.amplitude = config.get_amplitude()
        self.waves = np.array([])

    def load_wave(self, file_path: str, stereo: bool =False):
        '''Reads a wave file into wave signal array'''
        try:
            with wave.open(file_path) as wave_file:
                len_ = wave_file.getnframes()
                data = wave_file.readframes(len_)
                if stereo:
                    data = struct.unpack('{n}h'.format(n=len_*2), data)
                else:
                    data = struct.unpack('{n}h'.format(n=len_), data)
                self.waves = np.array(data)
        except Exception as e:
            print('Fail reading wave file', e)
            return None
        return True

    def retrieve_message(self):
        '''Maps characters from wave signal array'''
        if self.waves.size == 0:
            return False
        num_samples = int(self.sampling_rate * self.duration)
        num_chars = int(self.waves.size/num_samples)
        chars = np.array_split(self.waves, num_chars)
        return ''.join(
            ['1' if any(x) else '0' for x in chars])

    def plot(self, file_path: str):
        '''Saves a visual representation of the signal'''
        if self.waves.size == 0:
            return False
        plt.plot(self.waves)
        plt.savefig(file_path + '.pdf')
        return True

    def save_wave(self,
                  file_path: str,
                  comptype: str ='NONE',
                  compname: str ='not compressed',
                  sampwidth: int =2,
                  num_channels: int =1):
        '''Saves generated wave signal'''
        try:
            if self.waves.size == 0:
                return False
            n_frames = self.waves.size  # Len of the wave = # frames.
            with wave.open(file_path, 'w') as wave_file:
                wave_file.setparams((
                    num_channels,
                    sampwidth,
                    self.sampling_rate,
                    n_frames,
                    comptype,
                    compname))
                for signal in self.waves:
                    value = int(signal) if self.amplitude == 0 else int(
                            signal * self.amplitude)
                    wave_file.writeframes(struct.pack('h', value))
        except Exception as e:
            print('Fail saving waves', e)
            return False
        return True

    def generate_wave(self, data: str):
        '''Generates wave signal based on data'''
        try:
            wavs = []
            num_samples = int(self.sampling_rate * self.duration)
            real_range = np.arange(num_samples)
            zero_range = np.zeros(num_samples)
            for char in data:
                rng = real_range if char == '1' else zero_range
                k = [
                    np.sin(2 * np.pi * self.frequency * x / self.sampling_rate)
                    for x in rng]
                wavs.extend(k)
            self.waves = np.array(wavs)
        except Exception as e:
            print('Failed generating waves', e)
            return False
        return True
    
    def get_waves(self):
        return self.waves
