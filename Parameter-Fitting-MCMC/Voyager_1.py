'''
Voyager_1
Combo of emcee & custom neuron model
'''

import numpy as np 
import emcee
import neuron
from neuron import h, gui
import quickspikes as qs 
import time
import pyspike as spk
import time
from scipy import signal
import matplotlib
from matplotlib import pyplot
import pandas as pd 

## Creating neuron

soma = h.Section()

soma.insert('hh')
soma.insert('Na_T')
soma.insert('leak')
soma.insert('K1')

soma.gl_hh = 0.0003    # Leak conductance in S/cm2
soma.el_hh = -54.3     # Reversal potential in mV

soma.gnabar_Na_T = .12
soma.gkbar_K1 = .606
soma.g_leak = .0003


## Setting up and applying current 

stim = h.IClamp(0.5,soma)
time = h.Vector()
time.record(h._ref_t)

VecT = h.Vector([0, 100, 200])
VecStim = h.Vector([0.2, 0.4])

stim.delay = 5
stim.dur = 1e9

VecStim.play(stim._ref_amp, VecT) 

## Prior function

def lnprior(theta):
    C, gl, el, delt, vt, tw, a, vr, b = theta
 
    # bounds on the uniform prior distributions.
    if (   
            1.0 < C < 500 and 
            0.0  < gl < 30.0 and
            -120 < el < -20 and 
            0.1 < delt < 10 and
            -70 < vt < 0 and
            10 < tw < 210 and
            -10 < a < 10 and  
            -80.0 < vr < 0 and
            0.0 < b < 500
        ):
        
        ''''
        glP = np.log(probsgl[(np.digitize([gl], binsgl))-1]) 
        CP =  np.log(probsC[(np.digitize([C], binsC))-1])
        elP =  np.log(probsel[(np.digitize([el], binsel))-1]) 
        deltP =  np.log(probsdelt[(np.digitize([delt], binsdelt))-1]) 
        '''
        
       
        return 0.0
      
    return -np.inf
