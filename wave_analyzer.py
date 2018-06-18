# -*- coding: utf-8 -*-
# Author: Mason Rawson

import wave
import numpy as np
import matplotlib.pyplot as plt
import sys

class time_domain_wave_analyzer:
    
    def __init__(self, wave_vec = None, fs_hz = None, n_point_dft = None, wave_obj:wave.wave = None):
        if not wave_vec and not wave_obj:
            print("Either wave vector or wave obj must be specified")
            sys.exit(0)
            
        if wave_obj:
            self.wave_vec = wave_obj.wave_vec
            if not fs_hz:
                self.fs_hz = wave_obj.fs_hz
            self.fs_hz = fs_hz
            
        else:
            self.wave_vec = wave_vec
            self.fs_hz = fs_hz
            if not fs_hz:
                print("must supply fs if no wave object provided")
                sys.exit(0)
            
        self.n_point_dft = n_point_dft
        self.find_amp()
        self.find_power()
        self.find_stats()
        self.find_fft()
        
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
        self.power_watts = self.vpp**2 / 100 #assuming a 50 Olm system
        self.power_dbm = 10 + 20*np.log(self.vpp) #assuming a 50 Olm system
        
    def find_stats(self):
        self.xrms = np.sqrt(self.total_power)
        self.var = self.ac_power
        self.std_dev = np.sqrt(self.var)
        
    def find_fft(self):
        self.spec = np.abs(np.fft.fft(self.wave_vec)) #find full raw spectrum of input
        self.spec_bins_n = len(self.spec) #find number of freq bins
        self.spec_bins_hz = (np.arange(self.spec_bins_n) * (self.fs_hz / self.spec_bins_n)) #fs/n are the bin sizes of the fft
        self.r_spec = self.spec[1:self.spec_bins_n//2] #isolate just the real component - x axis of polar transform
        self.i_spec = np.flip(self.spec[self.spec_bins_n//2 + 1:], 0) #isolate just the imaginary component - y axis of polar transform
        self.power_spec = self.spec**2
        
    def print_members(self):
        print(
            "Power:",
            "\nDC power", self.dc_power,
            "\nAC power", self.ac_power,
            "\nTotal power", self.total_power,
            "\nPower_watts", self.power_watts,
            "\nPower_dbm", self.power_dbm,
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
        
        #time domain plot
        self.total_samples = len(self.wave_vec)
        self.t_axis = np.arange(0,self.total_samples)
        plt.plot(self.t_axis[0:self.total_samples], self.inst_power[0:self.total_samples])
        plt.plot(self.t_axis[0:self.total_samples], self.inst_power[0:self.total_samples], 'o')
        plt.show()
        
        #freq response plot
        plt.plot(self.spec_bins_hz, self.spec)
        plt.show()
        plt.plot(self.spec_bins_hz[1:len(self.r_spec)+1], self.r_spec)
        plt.show()
        plt.plot(self.spec_bins_hz[1:len(self.i_spec)+1], self.i_spec)
        plt.show()        
        plt.plot(self.spec_bins_hz, self.power_spec)
        plt.show()
