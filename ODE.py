import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

class MyODESolution():
    '''
     sol = MyODESolution()
     
     A class to store the output of a numerical ODE solver.
    '''
    def __init__(self):
        self.t = np.array([])
        self.y = np.array([])
        

def MyODE(f, tspan, y0, rtol=0.001):
    '''
    sol = MyOde(f, tspan, y0, rtol=0.001)
    
    Numerically solves the initial value problem
    
        dy(t)/dt = f(t,y)
            y(0) = y0
    
    using the Modified Euler adaptive time-stepping method.
    
    Input
      f       a Python dynamics function with calling sequence
                  dydt = f(t, y)
      tspan   2-tuple giving the start and end times, [start, end]
      y0      initial state of the system (as a 1D vector)
      rtol    the tolerance for the relative error (default 0.001)
    
    Output
      sol is an object of class MyODESolution. It has two member variables:
      sol.t   1D vector holding time stamps
      sol.y   an array that holds one state vector per row (corresponding
              to the time stamps)
    
      Notes:
          - t and y have the same number of rows.
    
          - The first element of sol.t should be tspan[0], and the first
            row of sol.y should be the initial state, y0.
    
          - If the computation was stopped by the triggering of an event,
            then the last row of t and y should correspond to the
            time that linear interpolation indicates for the zero-crossing
            of the event-function.
    '''
    
    # Marking breakdown
    # [2] for (a) Modified Euler
    # [3] for (b) Adaptive Time-Stepping
    # [2] for (c) Interpolate Terminal Event 
    
    # Initialize output arrays, tl and yl
    t = tspan[0]
    y = np.array(deepcopy(y0))
    
    tlst = [t]
    ylst = [list(y)]
    print(ylst)
    # As an initial guess, let's try 1/100 th of the total time.
    h = ( tspan[1] - tspan[0] ) / 100.
    
    while t<tspan[1]:
        #=== (a) Modified Euler step
        y_prime = f(t, y)
        forward_euler = y + h * y_prime
        modified_euler = y + (h/2) * (y_prime + f(t + h, forward_euler))
        
        #=== (b) Adaptive time-stepping
        ## YOUR CODE HERE
        relative_error = np.linalg.norm(modified_euler - forward_euler) / np.linalg.norm(modified_euler)
        if relative_error > rtol:
            h = h/2
        else:
            y = modified_euler
            t = t + h
            tlst.append(t)
            ylst.append(list(y))
            h = h*1.2
        
    # Assign values for sol.t and sol.y
    sol = MyODESolution()
    sol.t = np.array(tlst)
    sol.y = np.array(ylst)
  
    
    #=== (c) Interpolate the last point if we stepped past the end of the interval
    if sol.t[-1] > tspan[1]:
        ## YOUR CODE HERE
        slope = (sol.y[-1] - sol.y[-2]) / (sol.t[-1] - sol.t[-2])
        sol.y[-1] = sol.y[-2] + slope * (tspan[1] - sol.t[-2])
        sol.t[-1] = tspan[1]

    
    return sol
  
# Dynamics function
def projectile(t, z):
    '''
        z[0] = x'(t)
        z[1] = y'(t)
        z[2] = y''(t)
    '''
    # Vx is defined globally
    return np.array([Vx, z[2], -9.81])

# IVP parameters
# Start at 0; end at 3
tspan = [0, 3]
# Initialise x=0, y=0, y'=15
y0 = [0, 0, 15]
# Declare horizontal velocity (x'). This is "how hard you hit the ball"
Vx = 25.

sol = MyODE(projectile, tspan, y0)
print(sol.t)
plt.plot(sol.y[:,0], sol.y[:,1], '.-');
plt.xlabel('x'); plt.ylabel('y');
plt.title('For the initial value problem of a projectile');
plt.show()
