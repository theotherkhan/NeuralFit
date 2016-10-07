
import neuron
from neuron import h,gui 
import pickle
from matplotlib import pyplot

with open('t_vec.p') as t_vec_file:
    py_t_vec = pickle.load(t_vec_file)
##t_vec_restore = h.Vector(py_t_vec)

with open('v_vec.p') as v_vec_file:
    py_v_vec = pickle.load(v_vec_file)
##v_vec_restore = h.Vector(py_v_vec)
             
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(py_t_vec, py_v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()
