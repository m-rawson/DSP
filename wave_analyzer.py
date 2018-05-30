# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

class time_domain_wave_analyzer:
    def __init__(self, wave_vec):
        self.wave_vec = wave_vec
        self.find_amp()
        
    def find_amp(self):
        self.max = max(self.wave_vec)
        self.min = min(self.wave_vec)
        self.vpp = max(self.wave_vec) - min(self.wave_vec)
        self.amp = vpp/2
        
    def find_power(self):
        self.dc_power = np.avg(self.wave_vec)
        self.total_power = np.avg((self.wave_vec)**2)
        self.ac_power = self.total_power - self.dc_power
        
    def find_stats(self):
        self.xrms = np.sqrt(self.total_power)
        self.var = self.ac_power
        self.std_dev = np.sqrt(self.var)
        
        
        