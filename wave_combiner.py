# -*- coding: utf-8 -*-
# Author: Mason Rawson

import wave
import numpy as np
import matplotlib.pyplot as plt
import sys

class time_domain_wave_combiner:
    def __init__(self, wave_arr: [wave] = None):
        #wave_arr is an list of wave objects to be combined into one
        if(wave_arr == None):
            print("wave_arr is empty - no waves to be combined")
            sys.exit(0)
        self.wave_arr = wave_arr
        self.check_len() #check lengths of input waves
        self.wave_vec = self.wave_arr[0].wave_vec #grab first wave vec
        for i in np.arange(1,len(self.wave_arr),1): #sum all waves vectors
            self.wave_vec = self.wave_vec + self.wave_arr[i].wave_vec 
    
    def check_len(self):
        #waves need to be the same length in time domain
        for i in np.arange(1,len(self.wave_arr),1):
            if(self.wave_arr[0].time_s != self.wave_arr[i].time_s or self.wave_arr[0].total_samples != self.wave_arr[i].total_samples):
                print("**********************************************")
                print("wave_arr[0] and wave_arr[",i,"] aren't the same size")
                print("wave_arr[0]:")
                self.wave_arr[0].print_members()
                print("wave_arr[",i,"]")
                self.wave_arr[i].print_members()
                sys.exit(0)
        self.time_s = self.wave_arr[0].time_s
        self.total_samples = self.wave_arr[0].total_samples
        self.t_axis = np.arange(0,self.total_samples)

        
    def print_members(self, total_samples=0):
        if total_samples<=0: 
            total_samples=self.total_samples 
        plt.plot(self.t_axis[0:total_samples], self.wave_vec[0:total_samples])
        plt.plot(self.t_axis[0:total_samples], self.wave_vec[0:total_samples], 'o')
        plt.show()

