# import random
# import struct
# import wave

# # import matplotlib.pyplot as plt

# import numpy as np


# def load_wave(
#         file_path='test.wav', num_frames=96000, sampling_rate=48000, time=None,
#         stereo=False):
#     if time is not None:
#         num_frames = sampling_rate * time
#     with wave.open(file_path) as wave_file:
#         len_ = wave_file.getnframes()
#         print(len_)
#         data = wave_file.readframes(len_)
#         if stereo:
#             data = struct.unpack('{n}h'.format(n=len_*2), data)
#         else:
#             data = struct.unpack('{n}h'.format(n=len_), data)
#         # data = struct.unpack('<h'.format(n=len_), data)
#         return np.array(data)


# def fft(data, abs_=True):
#     data = np.fft.fft(data)
#     if abs_:
#         data = np.abs(data)
#     # print('1000', data[1000])
#     # print('2000', data[2000])
#     # print('200', data[200])
#     # print('Argmax:', np.argmax(data))
#     # print('max:', max(data))
#     return data


# # def plot(wave1, wave2=None, limit=2000):
# #     plt.plot(wave1[:limit])
# #     if wave2 is not None:
# #         plt.plot(wave2[:limit])
# #     plt.show()


# # def plots(plots, limit=2000):
# #     n = len(plots)
# #     for i, plot in enumerate(plots):
# #         plt.subplot(n, 1, i+1)
# #         plt.plot(plot[:limit])
# #     plt.show()


# def save_wave(
#         wave_, amplitude=16000, sampling_rate=48000, comptype='NONE',
#         compname='not compressed', sampwidth=2, num_channels=1,
#         file_path='test.wav'):
#     n_frames = len(wave_)  # Len of the wave is the number of the frames.
#     with wave.open(file_path, 'w') as wave_file:
#         wave_file.setparams((
#             num_channels, sampwidth, sampling_rate, n_frames, comptype, compname))
#         for signal in wave_:
#             if amplitude == 0:
#                 value = int(signal)
#             else:
#                 value = int(signal * amplitude)
#             wave_file.writeframes(struct.pack('h', value))


# def signalwave(
#         frequency=1000, num_samples=48000, sampling_rate=48000, time=5,
#         noisy=False):
#     """Sine function: y(t) = A * sin(2 * pi * f * t)."""
    
#     chars = ['0', '1', '0', '0', '0', '1']
    

#     def noise():
#         if noisy:
#             # Aumentar e diminuir "noise".
#             return random.uniform(0, 4)
#         else:
#             return 0

#     # if time is not None:
#     duration = 0.25
#     num_samples = sampling_rate * duration

#     return [
#         # 10 * (1 if chars[t] == '1' else 0) *
#         np.sin(2 * np.pi * frequency * t / sampling_rate) for t in range(num_samples)]

# wv = signalwave()
# save_wave(wv)
# # plot(wv)


import struct
import wave

# import matplotlib.pyplot as plt

import numpy as np


def load_wave(
        file_path='test.wav', num_frames=96000, sampling_rate=48000, time=None,
        stereo=False):
    if time is not None:
        num_frames = sampling_rate * time
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


def fft(data, abs_=True):
    data = np.fft.fft(data)
    if abs_:
        data = np.abs(data)
    # print('1000', data[1000])
    # print('2000', data[2000])
    # print('200', data[200])
    # print('Argmax:', np.argmax(data))
    # print('max:', max(data))
    return data


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


def save_wave(
        wave_, amplitude=16000, sampling_rate=48000, comptype='NONE',
        compname='not compressed', sampwidth=2, num_channels=1,
        file_path='test.wav'):
    n_frames = len(wave_)  # Len of the wave is the number of the frames.
    with wave.open(file_path, 'w') as wave_file:
        wave_file.setparams((
            num_channels, sampwidth, sampling_rate, n_frames, comptype, compname))
        for signal in wave_:
            value = int(signal) if amplitude == 0 else int(signal * amplitude)
            wave_file.writeframes(struct.pack('h', value))


def signalwave(data, frequency=440, sampling_rate=48000):
    """Sine function: y(t) = A * sin(2 * pi * f * t)."""
    duration = 0.25
    wavs = []
    num_samples = int(sampling_rate * duration)
    for char in data:
        rng = np.arange(num_samples) if char == '1' else np.zeros(num_samples)
        k = [np.sin(2 * np.pi * frequency * x / sampling_rate) for x in rng]
        wavs.extend(k)
    return wavs


wv = signalwave(
    '100010111000101000000011101110001011100010111010001110111010111000101011100010100011101000000011101010001011101110111')
save_wave(wv)
# plot(wv)
