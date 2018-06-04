# -*- coding: utf-8 -*-
# Author: Mason Rawson

#%%
import wave
import numpy as np
import matplotlib.pyplot as plt
import wave_analyzer
import wave_combiner

cos = wave.wave(phase_rad = np.pi/2, freq_hz = 100, fs_hz=400, len_str='total_samples', len_data=128)
sin = wave.wave(freq_hz = 150, fs_hz=400, len_str='total_samples', len_data=128)

wave_arr = [cos, sin]

cos_plus_sin = wave_combiner.time_domain_wave_combiner(wave_arr)
cos_plus_sin.plot()

wave_analyzer.time_domain_wave_analyzer(cos_plus_sin.wave_vec).data()

