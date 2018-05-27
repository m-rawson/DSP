# -*- coding: utf-8 -*-
# Author: Mason Rawson

import numpy as np
import matplotlib.pyplot as plt

class wave:
    #The actual wave and properties
    
    def __init__(self, amp=10, freq_hz=10, phase_rad=0, len_str = 'time_s', len_data = 1, fs_hz = 0):
        #need time, period, or total_samples and fs (which defaults to 4xfreq)
        
        #base prop
        self.amp = amp
        self.freq_hz = freq_hz
        self.phase_rad = phase_rad    
        self.peak_to_peak = 2*self.amp

        #waveform prop
        if (fs_hz > 0):
            self.fs_hz = fs_hz
        else: 
            self.fs_hz = 4*self.freq_hz #assign fs
            
        if(len_str == "time_s"):
            self.time_s = len_data
            self.num_periods = self.time_s*self.freq_hz #calc periods within time given
            self.total_samples = self.time_s*self.fs_hz
        
        elif(len_str == "num_periods"):
            self.num_periods = len_data
            self.time_s = self.num_periods/self.freq_hz #calc total time from periods
            self.total_samples = self.time_s*self.fs_hz

        elif(len_str == "total_samples"):
            self.total_samples = len_data
            self.time_s = 1/self.fs_hz
            self.num_periods = self.time_s*self.freq_hz #calc periods within time given
        
        self.points_within_period = int(self.fs_hz/self.freq_hz)
        
        self.create_waveform() #create the actual wave
        
    def create_waveform(self):
        self.t_axis = np.arange(0,2*np.pi*self.num_periods,2*np.pi*self.num_periods/self.fs_hz)
        self.wave_vec = self.amp*np.sin(self.t_axis+self.phase_rad)

    def plot(self, num_periods=0):
        if num_periods<=0: 
            num_periods=self.num_periods 
        plt.plot(self.t_axis[0:int(num_periods*self.points_within_period)], self.wave_vec[0:int(num_periods*self.points_within_period)])
        plt.plot(self.t_axis[0:int(num_periods*self.points_within_period)], self.wave_vec[0:int(num_periods*self.points_within_period)], 'o')
        plt.show()
    
    def print_members(self):
        print("amp:", self.amp)
        print("freq_hz: ", self.freq_hz)
        print("phase_rad: ", self.phase_rad)
        print("peak_to_peak: ", self.peak_to_peak)
        print("fs_hz: ", self.fs_hz)
        print("time_s: ", self.time_s)
        print("num_periods: ", self.num_periods)
        print("total_samples: ", self.total_samples)
        self.plot(2)
        
        
#%%
test = wave()
test.print_members()
