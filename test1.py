import neuron
import nrn
soma = nrn.Section()
soma.L = 30
soma.nseg = 3
soma.diam = 30

for nseg in soma:
    nseg.x, nseg.diam, nseg.cm

soma_seg = soma(.5)
soma.insert('hh')

from neuron import h
tstop = 1
print neuron.run(tstop)

#################################################################

>>> import neuron
>>> import nrn
soma = nrn.Section()
soma.L = 30
soma.nseg = 3
soma.diam = 30
run()
Traceback (most recent call last):
  File "stdin", line 1, in <module>
NameError: name 'run' is not defined
soma.cm
1.0
soma.Ra
35.4
>>> for nseg in soma:
... nseg.x, nseg.diam, nseg.cm
  File "stdin", line 2
    nseg.x, nseg.diam, nseg.cm
       ^
IndentationError: expected an indented block
for nseg in soma:
...     nseg.x, nseg.diam, nseg.cm
... 
(0.16666666666666666, 30.0, 1.0)
(0.5, 30.0, 1.0)
(0.8333333333333333, 30.0, 1.0)
>>> soma_seg.diam
Traceback (most recent call last):
  File "stdin", line 1, in <module>
NameError: name 'soma_seg' is not defined
soma_seg = soma(.5)
soma_seg.diam
30.0
soma_nseg = []
for nseg in soma:
...     soma_nseg.append(nseg.x)
... 
soma(soma_nseg[1]).diam
30.0
soma.insert('hh')
<nrn.Section object at 0x103002f80>
soma(0.5).v
-65.0
stimulator = neuron.h.IClamp(0.5,soma)
stimulator.delay = 0.1
stimulator.dur = 0.8
stimulator.amp = 1.2
from neuron import h
h.run()
0.0
h('run()')
1
h('run()')
1
tstop = 1.5
neuron.run(tstop)
h('run()')
1
soma(.5).v
32.81043517271196
>>> v_vec = h.Vector()
>>> t_vec = h.Vector()
>>> stimulator.delay = 5
>>> stimulator.dur = 1
>>> stimulator.amp = 0.1
>>> 
>>> v_vec.record(soma(0.5)._ref_v)
1.0
>>> t_vec.record(h._ref_t)
1.0
>>> v_vec.record(soma(0.5)._ref_v)
1.0
>>> simdur = 25
>>> h.tstop = simdur
>>> h.run()
0.0
>>> import matplotlib
>>> from matplotlib import pyplot
>>> pyplot.figure(figsize=(8,4)) 
<matplotlib.figure.Figure object at 0x10317d910>
>>> pyplot.plot(t_vec, v_vec)
[<matplotlib.lines.Line2D object at 0x107e63590>]
>>> pyplot.xlabel('time (ms)')
<matplotlib.text.Text object at 0x104ab3510>
>>> pyplot.ylabel('mV')
<matplotlib.text.Text object at 0x107e03490>
>>> pyplot.show()

^Z
[3]+  Stopped                 nrngui -python
d-172-27-46-43:Desktop hk4cd$ nrngui -python
NEURON -- VERSION 7.4 (1380:90539e842093) 90539e842093
Duke, Yale, and the BlueBrain Project -- Copyright 1984-2015
See http://www.neuron.yale.edu/neuron/credits

>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
d-172-27-46-43:Desktop hk4cd$ clear

d-172-27-46-43:Desktop hk4cd$ nrngui -python

