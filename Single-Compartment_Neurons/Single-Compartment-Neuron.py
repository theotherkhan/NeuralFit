'''
Hasan Khan
Meliza Lab
NeuralFits

July 7th, 2016

This python program creates a HOC object single-compartment neuron. Hodgkin Huxeley biophysical models
are applied to the neuron, along with custom channel modifications (pulled from ModelDB). Once the 
neuron is setup, a simple current is applied. The program outputs two graphs: one with action potential 
voltage values, and another with gating variable values (n, m, h). 

'''

## IMPORTS ################################

import neuron
import nrn 
import matplotlib

from neuron import h, gui

## TOPOLOGY ################################

h = neuron.hoc.HocObject()

soma = h.Section()

soma.L = soma.diam = 12.6157
soma.nseg = 3

soma.cm = 1.0
soma.Ra = 35.399999999999999


'''
print "(psection alternate) Location, diameter, capacitance:"
for nseg in soma: 
	print nseg.x, nseg.diam, nseg.cm

soma_segloc = []
soma_segdiam = []
soma_segcap =[] # create an empty list of segments

for nseg in soma:
    soma_segloc.append(nseg.x)
    soma_segdiam.append(nseg.diam)
    soma_segcap.append(nseg.cm)


print "Soma segment locations: " , soma_segloc
print "Soma segment diams: " , soma_segdiam
print "Soma segment capactiance: " , soma_segcap
'''


## BIOPHYSICS ################################

## Here, the hodgkin huxeley model is being 
## applied, along with custom channel modifications

soma.insert('hh')

soma.insert('Na_T')
soma.insert('leak')
soma.insert('K1')


##soma.gnabar_hh = 0.12  # Sodium conductance in S/cm2
##soma.gkbar_hh = 0.036  # Potassium conductance in S/cm2

soma.gl_hh = 0.0003    # Leak conductance in S/cm2
soma.el_hh = -54.3     # Reversal potential in mV

soma.gnabar_Na_T = .12
soma.gkbar_K1 = .606
soma.g_leak = .0003


'''

soma.i_leak = .4
soma.g_leak = .002
soma.e_leak = -65

The Hodgkin-Huxley channels add the following new properties to the section:

gnabar_hh: The maximum specific sodium channel conductance [Default value = 0.120 S/cm^2]
gkbar_hh: The maximum specific potassium channel conductance [Default value = 0.036 S/cm^2]
gl_hh: The maximum specific leakage conductance [Default value = 0.0003 S/cm^2]
ena: The reversal potential for the sodium channel [Default value = 50 mV]
ek: The reversal potential for the potassium channel [Default value = -77 mV]
el_hh: The reversal potential for the leakage channel [Default value = -54.3 mV]

'''



## POINT PROCESSES ################################


stim = h.IClamp(0.5,soma)



time = h.Vector()
time.record(h._ref_t)


## Current to be applied

VecT = h.Vector([0, 100, 200])
VecStim = h.Vector([0.2, 0.4])


stim.delay = 5
stim.dur = 1e9
##stim.amp = 0.4

VecStim.play(stim._ref_amp, VecT) 


## Vectors for membrane potential and gating variables:

v_vec = h.Vector() # Membrane potential vector
n_vec = h.Vector()  
h_vec = h.Vector()
m_vec = h.Vector()
t_vec = h.Vector() # Time stamp vector

v_vec.record(soma(0.5)._ref_v)
n_vec.record(soma(0.5)._ref_m_K1)
h_vec.record(soma(0.5)._ref_h_Na_T)
m_vec.record(soma(0.5)._ref_m_Na_T)

t_vec.record(h._ref_t)
simdur = 210.0

h.tstop = simdur
h.run()



## PLOTTING #######################################

from matplotlib import pyplot

##h_vec = h.Vector()
##h_vec.record(&soma(0.5).hh.h_hh)

pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, m_vec, "r", label = 'm')
pyplot.plot(t_vec, n_vec, "b", label = 'n')

pyplot.plot(t_vec, h_vec, "g", label = 'h')
pyplot.legend(loc='upper right')
pyplot.xlabel('time (ms)')
pyplot.ylabel('probability')

pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec, label = 'Vm')
pyplot.legend(loc='upper right')
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()


'''

import numpy
pyplot.figure(figsize=(8,4))



print "h value: ", soma.h_hh
print "m value: ",soma.m_hh
print "n value: ",soma.n_hh

stim.amp = .05
h.run()
pyplot.plot(t_vec, v_vec, color='black')

stim.amp = .2
h.run()
pyplot.plot(t_vec, v_vec, color='blue')


stim.amp = .4
h.run()
pyplot.plot(t_vec, v_vec, color='red')

##pyplot.plot(t_vec, h_vec, color='red')

pyplot.plot(t_vec, v_vec, color='green')


pyplot.plot(VectT, v_vec, color='green')


pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()

''' 

## End program

