# -*- coding: utf-8 -*-

#%%
import wave
import numpy as np
import matplotlib.pyplot as plt

cos = wave.wave(phase_rad = np.pi/2, freq_hz = 100, fs_hz=400, len_str='total_samples', len_data=128)
sin = wave.wave(freq_hz = 150, fs_hz=400, len_str='total_samples', len_data=128)
wave_arr = [cos, sin]
cos_plus_sin = wave.time_domain_wave_combiner(wave_arr)
cos_plus_sin.plot()

