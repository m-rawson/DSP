# -*- coding: utf-8 -*-
# Author: Mason Rawson

import wave
import numpy as np
import matplotlib.pyplot as plt

class time_domain_wave_analyzer:
    
    def __init__(self, wave_vec):
        self.wave_vec = wave_vec
        self.find_amp()
        self.find_power()
        self.find_stats()
        
    def find_amp(self):
        self.max = max(self.wave_vec)
        self.min = min(self.wave_vec)
        self.vpp = max(self.wave_vec) - min(self.wave_vec)
        self.amp = self.vpp/2
        
    def find_power(self):
        self.dc_power = np.average(self.wave_vec)
        self.inst_power = self.wave_vec**2
        self.total_power = np.average(self.inst_power)
        self.ac_power = self.total_power - self.dc_power
        
    def find_stats(self):
        self.xrms = np.sqrt(self.total_power)
        self.var = self.ac_power
        self.std_dev = np.sqrt(self.var)
        
    def data(self):
        print(
            "Power:",
            "\nDC power", self.dc_power,
            "\nAC power", self.ac_power,
            "\nTotal power", self.total_power,
            "\nAmplitudes:",
            "\nMax", self.max,
            "\nMin", self.min,
            "\nVpp", self.vpp,
            "\nAmplitude", self.amp,
            "\nStats:",
            "\nXrms", self.xrms,
            "\nVariance", self.var,
            "\nStd Dev", self.std_dev
            )
        self.total_samples = len(self.wave_vec)
        self.t_axis = np.arange(0,self.total_samples)
        plt.plot(self.t_axis[0:self.total_samples], self.inst_power[0:self.total_samples])
        plt.plot(self.t_axis[0:self.total_samples], self.inst_power[0:self.total_samples], 'o')
        plt.show()