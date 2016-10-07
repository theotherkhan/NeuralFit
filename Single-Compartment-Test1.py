'''
Basic single compartment neuron. Test file. 

'''


import neuron
from neuron import h,gui 

## TOPOLOGY ###########################################################

soma = h.Section(name = 'soma')  ## creating soma section
h.psection()                     

print dir(soma)                   ## attributes of soma. Returns all vars/methods associated with soma
                          

## printing some of soma's attributes

print "Length:", soma.L
print "Resistance (ohms):", soma.Ra
print soma.cell()
print soma.orientation()
print "Name: ", soma.name()
print "nseg: ", soma.nseg
## finding help on somas functions: help(soma.insert)





## BIOPHYSICAL PARAMS ################################################

soma.insert('pas') ## insert passive leak channel (specify strategy)

##type() function tells us what type variabel is:

print "type(soma) =", type(soma)
print "type(soma(0.5)) =", type(soma(0.5))

## Observing diff attributes of segments and their variables:

mech = soma(0.5).pas
print "Soma section .5, passive curent attributes: ", dir(mech)

print " Soma section .5, passive curent conductance (g):", mech.g
print " Soma section .5, passive curent resting potential (e): " , soma(0.5).e_pas





## POINT PROCESS #################################################### 
#Inserting alpha synapse. This is equivalent to NEURON GUI point process menu


asyn = h.AlphaSynapse(0.5, sec = soma)  ## new point process. Pass the a-synapse the segment to whic it will bind

'''
print "asyn.e", asyn.e
print "asyn.gmax", asyn.gmax
print "asyn.onset", asyn.onset
print "asyn.tau", asyn.tau
'''

print "Alpha synapse attributes: ", dir(asyn)

asyn.onset = 20
asyn.gmax = 5

print "  "
print "CURRENT STATE OF SOMA:"
h.psection()




## RECORDING VARIABLES, PLOTTING #####################################
print "  "
print "  "
print "  "
print "  "
print "  "
print "  "


v_vec = h.Vector()             # Membrane potential vector
t_vec = h.Vector()             # Time stamp vector  (x,y axis for spike plot)
v_vec.record(soma(0.5)._ref_v)  # set Y axis to record mem potential
t_vec.record(h._ref_t)          # set X axis to record for time 

h.tstop = 40.0
h.run()

from matplotlib import pyplot
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
##pyplot.show()





## PICKLING ##########################################################

import pickle

'''
tempObj1 = open('tVec.p', 'w')   # Pickle file is newly created where foo1.py is
pickle.dump( t_vec, tempObj1)          # dump data to f
tempObj1.close()    
'''


with open('t_vec.p', 'w') as t_vec_file:
    pickle.dump(t_vec, t_vec_file)


with open('v_vec.p', 'w') as v_vec_file:
    pickle.dump(v_vec, v_vec_file)































