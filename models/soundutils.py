import struct
import wave

import numpy as np

from .cfgy import Config


class AudioHanlder():
    '''Represents an audio handler with basic functions'''
    def __init__(self, config: Config):
        self.frequency = config.get_audio_frequency()
        self.sampling_rate = config.get_sampling_rate()
        self.duration = config.get_unitary_time()
        self.amplitude = config.get_amplitude()
        print(
            'Frequency: {}'
            'Sampling rate: {}'
            'Duration: {}'
            'Amplitude: {}'
            .format(self.frequency, self.sampling_rate, self.duration, self.amplitude)
        )
        self.waves = None

    def load_wave(self, file_path: str, stereo: bool =False):
        # if time is not None:
            # num_frames = sampling_rate * time
        with wave.open(file_path) as wave_file:
            len_ = wave_file.getnframes()
            print(len_)
            data = wave_file.readframes(len_)
            if stereo:
                data = struct.unpack('{n}h'.format(n=len_*2), data)
            else:
                data = struct.unpack('{n}h'.format(n=len_), data)
            # data = struct.unpack('<h'.format(n=len_), data)
            return np.array(data)

    # def plot(wave1, wave2=None, limit=2000):
    #     plt.plot(wave1[:limit])
    #     if wave2 is not None:
    #         plt.plot(wave2[:limit])
    #     plt.show()

    # def plots(plots, limit=2000):
    #     n = len(plots)
    #     for i, plot in enumerate(plots):
    #         plt.subplot(n, 1, i+1)
    #         plt.plot(plot[:limit])
    #     plt.show()

    def save_wave(self,
                  file_path: str,
                  comptype: str ='NONE',
                  compname: str ='not compressed',
                  sampwidth: int =2,
                  num_channels: int =1):
        '''Saves generated wave signal'''
        try:
            if not self.waves:
                return False
            print(self.waves)
            n_frames = len(self.waves)  # Len of the wave is number of the frames.
            with wave.open('file_path.wav', 'w') as wave_file:
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
            duration = 0.25
            wavs = []
            num_samples = int(self.sampling_rate * duration)
            real_range = np.arange(num_samples)
            zero_range = np.zeros(num_samples)
            for char in data:
                rng = real_range if char == '1' else zero_range
                k = [
                    np.sin(2 * np.pi * self.frequency * x / self.sampling_rate)
                    for x in rng]
                wavs.extend(k)
            self.waves = wavs
        except Exception as e:
            print('Failed generating waves', e)
            return False
        return True
    
    def get_waves(self):
        return self.waves
