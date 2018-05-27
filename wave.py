# -*- coding: utf-8 -*-
# Author: Mason Rawson

import numpy as np
import matplotlib.pyplot as plt
import sys

class wave:
    #The actual wave and properties
    
    def __init__(self, amp=1, freq_hz=10, phase_rad=0, len_str = 'time_s', len_data = 1, fs_hz = 0, base_wave = None):
        #need time, period, or total_samples and fs (which defaults to 4xfreq)
                
        #base properties
        self.amp = amp
        self.freq_hz = freq_hz
        self.phase_rad = phase_rad    
        self.peak_to_peak = 2*self.amp

        #waveform properties
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
        else:
            print("invalid len_str")
            sys.exit(0)
        
        #calculated properties
        self.period = 1/freq_hz
        self.sample_within_period = int(self.fs_hz/self.freq_hz)
                
        #create the actual wave
        self.create_waveform() 
        
    def create_waveform(self):
        self.t_axis = np.arange(0,2*np.pi*self.num_periods,2*np.pi*self.num_periods/self.fs_hz)
        self.wave_vec = self.amp*np.sin(self.t_axis+self.phase_rad)

    def plot(self, num_periods=0):
        if num_periods<=0: 
            num_periods=self.num_periods 
        plt.plot(self.t_axis[0:int(num_periods*self.sample_within_period)], self.wave_vec[0:int(num_periods*self.sample_within_period)])
        plt.plot(self.t_axis[0:int(num_periods*self.sample_within_period)], self.wave_vec[0:int(num_periods*self.sample_within_period)], 'o')
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
        print("samples_within_period: ", self.sample_within_period)
        self.plot()
        
#%%
class time_domain_wave_combiner:
    def __init__(self, wave_arr = None):
        #wave_arr is an list of wave objects to be combined into one
        if(wave_arr == None):
            print("wave_arr is empty - no waves to be combined")
            sys.exit(0)
        self.wave_arr = wave_arr
        self.check_len() #check lengths of input waves
        self.comb_wave = self.wave_arr[0].wave_vec #grab first wave vec
        for i in np.arange(1,len(self.wave_arr),1): #sum all waves vectors
            self.comb_wave = self.comb_wave + self.wave_arr[i].wave_vec 
    
    def check_len(self):
        #waves need to be the same length in time domain
        for i in np.arange(1,len(self.wave_arr),1):
            if(self.wave_arr[0].time_s != self.wave_arr[i].time_s or self.wave_arr[0].total_samples != self.wave_arr[i].total_samples):
                print("wave_arr[0] and wave_arr[",i,"] aren't the same size")
                print("wave_arr[0]:")
                self.wave_arr[0].print_members()
                print("wave_arr[",i,"]")
                self.wave_arr[i].print_members()
                sys.exit(0)
        self.time_s = self.wave_arr[0].time_s
        self.total_samples = self.wave_arr[0].total_samples
        self.t_axis = np.arange(0,self.total_samples)

        
    def plot(self, total_samples=0):
        if total_samples<=0: 
            total_samples=self.total_samples 
        plt.plot(self.t_axis[0:total_samples], self.wave_vec[0:total_samples])
        plt.plot(self.t_axis[0:total_samples], self.wave_vec[0:total_samples], 'o')
        plt.show()

#%%
cos = wave(phase_rad = np.pi/2, fs_hz = 100)
sin = wave(fs_hz = 100)
cos.print_members()
sin.print_members()
cos_plus_sin = wave(phase_rad = np.pi/2, fs_hz=100, base_wave = sin)
cos_plus_sin.print_members()
