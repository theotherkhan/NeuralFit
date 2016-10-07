: Hasan's HH voltage-gated potassium current (persistent)

NEURON {
     SUFFIX K1
     USEION k READ ek WRITE ik
     RANGE gkbar, gk, ik
}

UNITS {
     (S)  = (siemens)
     (mV) = (millivolt)
     (mA) = (milliamp)
}

PARAMETER { gkbar = 0.0606 (S/cm2) 


k1Vhalfm = -21.0
k1km = 7.561
k1sigmam = 20.11
k1tauInitm = .34
k1tauMaxm = 8.556
 

}

ASSIGNED {
v (mV)
ek (mV) : typically ~ -77.5 ik (mA/cm2)
ik (mA/cm2)
gk (S/cm2)
}

STATE { m }

BREAKPOINT {
     SOLVE states METHOD cnexp
     gk = gkbar*m*m*m*m
     ik = gk * (v - ek)
}

INITIAL {
     : Assume v has been constant for a long time
     m = mInf(v, k1km, k1Vhalfm)
}

DERIVATIVE states {
     : Computes state variable n at present v & t
     m' = (mInf(v, k1km, k1Vhalfm) - m)/mTau(v, k1tauInitm, k1tauMaxm, k1Vhalfm, k1sigmam)
}

FUNCTION mInf(Vm (mV), k1km, k1Vhalfm) (/ms) {
       
     UNITSOFF
       
     mInf = 0.5*(1+tanh((Vm - k1Vhalfm)/k1km))
           
     UNITSON
} 

FUNCTION mTau(Vm (mV), k1tauInitm, k1tauMaxm, k1Vhalfm, k1sigmam) {

     UNITSOFF

     mTau = k1tauInitm + k1tauMaxm * (1-tanh(Vm - k1Vhalfm)/k1sigmam)

     UNITSON
}
