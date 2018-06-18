# -*- coding: utf-8 -*-
# Author: Mason Rawson

import numpy as np
import matplotlib.pyplot as plt
import sys

class wave:
    '''
    The actual wave and properties object
    Notes on Args:
        len_str valid values are 'time_s', 'num_periods', 'total_samples'            
        len_data is the value of the len_str chosen
    '''
    
    def __init__(self, amp=1, freq_hz=10, phase_rad=0, len_str = 'time_s', len_data = 1, fs_hz = 100):
        #need time, period, or total_samples and fs (which defaults to 4xfreq)
                
        #base properties
        self.amp = amp
        self.freq_hz = freq_hz
        self.phase_rad = phase_rad    

        #waveform properties
        self.fs_hz = fs_hz
            
        if(len_str == "time_s"):
            self.time_s = len_data
            self.num_periods = self.time_s*self.freq_hz #calc periods within time given
            self.total_samples = self.time_s*self.fs_hz #calc samples from time and fs
        
        elif(len_str == "num_periods"):
            self.num_periods = len_data
            self.time_s = self.num_periods/self.freq_hz #calc total time from periods
            self.total_samples = self.time_s*self.fs_hz #calc samples from time and fs

        elif(len_str == "total_samples"):
            self.total_samples = len_data
            self.time_s = self.total_samples/self.fs_hz #calc time from samples and fs
            self.num_periods = self.time_s*self.freq_hz #calc periods within time given
        
        else:
            print("invalid len_str: must be time_s, num_periods, or total_samples - you entered:", len_str)
            sys.exit(0)
        
        #calculated properties
        self.period_s = 1/freq_hz
        self.sample_within_period = (self.fs_hz/self.freq_hz)
        self.ang_freq = 2*np.pi*self.freq_hz
        self.vpp = 2*self.amp
        self.power_watts = self.vpp**2 / 100 #assuming a 50 Olm system
        self.power_dbm = 10 + 20*np.log(self.vpp) #assuming a 50 Olm system
        
        #create the actual wave
        self.create_waveform() 
        
    def create_waveform(self):
        self.t_axis = np.arange(0,self.time_s, self.time_s/self.total_samples)
        self.wave_vec = self.amp*np.sin(self.ang_freq*self.t_axis+self.phase_rad)

    def plot(self, num_periods=0):
        if num_periods<=0: 
            num_periods=self.num_periods 
        plt.plot(self.t_axis, self.wave_vec) #plotting the wave over time
        plt.plot(self.t_axis, self.wave_vec, 'o') #plotting the actual sample points
        plt.show()

    
    def print_members(self):
        print("Amp:", self.amp,
        "\nFreq_hz: ", self.freq_hz,
        "\nPeriod_s: ", self.period_s,
        "\nPhase_rad: ", self.phase_rad,
        "\nAng_freq: ", self.ang_freq,
        "\Vpp: ", self.vpp,
        "\nPower_watts: ", self.power_watts,
        "\nPower_dbm: ", self.power_dbm,
        "\nFs_hz: ", self.fs_hz,
        "\nTime_s: ", self.time_s,
        "\nNum_periods: ", self.num_periods,
        "\nTotal_samples: ", self.total_samples,
        "\nSamples_within_period: ", self.sample_within_period)

        self.plot()
   


        
        
        