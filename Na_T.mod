: Hasan's HH voltage-gated fast sodium current (transient)

NEURON {
     SUFFIX Na_T
     USEION na READ ena WRITE ina
     RANGE gnabar, gna, ina, j
}
UNITS {
     (S)  = (siemens)
     (mV) = (millivolt)
     (mA) = (milliamp)
}

PARAMETER { gnabar = 0.12 (S/cm2)

Vhalfh = -65.70
kh = -9.76
tauInith = .02
tauMaxh = 4.552
sigmah = 41.67



Vhalfm = -37.85
km = 9.16
tauInitm = .388
tauMaxm = .012
sigmam = 5.0

}

ASSIGNED {
v (mV)
ena (mV) : typically ~ 50.0 ik (mA/cm2)
ina (mA/cm2)
gna (S/cm2)
}

STATE { h m } 


BREAKPOINT {
     SOLVE states METHOD cnexp
     gna = gnabar*h*m*m*m
     ina = gna * (v - ena)
}


INITIAL {
     : Assume v has been constant for a long time
     m = mInf(v, km, Vhalfm)
     h = hInf(v, kh, Vhalfh)
}



DERIVATIVE states {
     : Computes state variable n at present v & t
     m' = (mInf(v, km, Vhalfm) - m)/mTau(v, tauInitm, tauMaxm, Vhalfm, sigmam)
     h' = (hInf(v, kh, Vhalfh) - h)/hTau(v, tauInith, tauMaxh, Vhalfh, sigmah)
}


FUNCTION mInf(Vm (mV), km, Vhalfm) (/ms) {
       
     UNITSOFF
       
     mInf = 0.5*(1+tanh((Vm - Vhalfm)/km))
           
     UNITSON
} 


FUNCTION hInf(Vm (mV), kh, Vhalfh) (/ms) {
       
     UNITSOFF
       
     hInf = 0.5*(1+tanh((Vm - Vhalfh)/kh))
           
     UNITSON
} 

FUNCTION mTau(Vm (mV), tauInitm, tauMaxm, Vhalfm, sigmam) {

     UNITSOFF

     mTau = tauInitm + tauMaxm * (1-(tanh((Vm - Vhalfm)/sigmam))^2)

     UNITSON
}

FUNCTION hTau(Vm (mV), tauInith, tauMaxh, Vhalfh, sigmah) {

     UNITSOFF

     hTau = tauInith + tauMaxh * (1-(tanh((Vm - Vhalfh)/sigmah))^2)

     UNITSON
}























