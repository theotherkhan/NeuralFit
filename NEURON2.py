## Ball and stick model w/ NEURON 
## Hasan Khan
## July 28, 2016 

import neuron
from neuron import h,gui
import matplotlib
from matplotlib import pyplot


## TOPOLOGY ################################################################

soma = h.Section(name='soma')
dend = h.Section(name='dend')

h.psection(sec=soma) ## retrieve info using this. Pass in section u want info for

dend.connect(soma(1)) ## connects dendrite to the '1' end of the Soma

h.psection(sec=dend)

h.topology()

## GEOMETRY  ################################################################

# Surface area of cylinder is 2*pi*r*h (sealed ends are implicit).
# Here we make a square cylinder in that the diameter
# is equal to the height, so diam = h. ==> Area = 4*pi*r^2
# We want a soma of 500 microns squared:
# r^2 = 500/(4*pi) ==> r = 6.2078, diam = 12.6157
soma.L = soma.diam = 12.6157 # Makes a soma of 500 microns squared.
dend.L = 200 # microns
dend.diam = 1 # microns
print "Surface area of soma =", h.area(0.5, sec=soma)

h.allsec()
