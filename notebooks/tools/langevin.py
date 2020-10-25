
import numpy as np
import numpy.random as rdm

def harmonic(x,k):
    f=-k*x
    return f

def langevin_step(x,v,h,gamma,sigma,mass,force=lambda x:0):
    xnew=x+h*v
    vnew=v+h*force(x)/mass-h*gamma/mass*v+np.sqrt(h)*sigma/mass*rdm.normal()
    return xnew,vnew

if __name__ == "__main__":

    k=1.0
    gamma=1.0
    temperature=10.0
    sigma=np.sqrt(2.0*temperature*gamma)
    mass=1.0

    print('Sans force')

    x,v=0.0,0.0

    h=0.01
    nsteps=10000
    step=0
    while (step<nsteps):
        x,v=langevin_step(x,v,h,gamma,sigma,mass)
        print(x,v)
        step=step+1

    print('Avec force harmonique')

    x,v=0.0,0.0

    h=0.01
    nsteps=10000
    step=0
    while (step<nsteps):
        x,v=langevin_step(x,v,h,gamma,sigma,mass,force=lambda x: harmonic(x,k))
        print(x,v)
        step=step+1
