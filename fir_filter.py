# -*- coding: utf-8 -*-
# Author: Mason Rawson

import wave
import numpy as np
import matplotlib.pyplot as plt
import sys

class time_series_fir_filter:
    
    def __init__(self, wave_obj:wave=None, wave_vec=None, coef=None, taps=None, zeropad=None):
        
        #sanity check for input
        if not wave_obj and not wave_vec:
            print("need either a wave object or a wave vector")
            sys.exit(0)
        
        #get input wave
        self.wave = wave_obj
        if self.wave:
            self.wave_vec = self.wave.wave_vec
        else:
            self.wave_vec = wave_vec
        
        #input coef
        self.coef = coef
        self.taps = taps            



    def compute(self):
        if not self.wave_vec or not self.coef or self.taps <= 0 or len(taps) != len(coef):
            print("input data error")
            self.data
            sys.exit(0)
        
        self.filt = np.dot(self.wave_vec, self.coef)
        
    def quick_filt_setup(self, quick_filt='Avg'):
        if quick_filt == 'Avg':
                self.taps = len(self.wave_vec)
                self.coef = np.ones([1,self.taps]) * 1/np.sum(self.wave_vec)     

    def data(self):
        print(self)
        