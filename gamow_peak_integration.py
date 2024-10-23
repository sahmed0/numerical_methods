# -*- coding: utf-8 -*-

"""
This is a program to evaluate a numerical integration
using Simpson's Rule
made for calculating the area of the Gamow Peak
For Origins of the Solar System
by Sajid on 25-10-2023.
"""

# USING SCIPY.INTEGRATE.SIMPSONS FUNCTION
# import libraries
import numpy as np
from scipy import integrate

# GLOBAL VARIABLES
k = 1.380649*(10**-23)
GAMOW = 10**-6

# Mass is in units of solar masses
MASS = np.linspace(10, 100, 90, True)

for m in MASS:

    # calculate Core Temp of star from it's mass using the derived equation.
    T = 1.6*(10**7)*(m**0.2866)
    
    def p_fusion():
        """ Define the probability of fusion function """
        prob = ((np.exp(-x/(k*T)))/((k*T)**1.5))*(np.exp(-GAMOW/np.sqrt(x)))
        return prob
    
    #Conduct the integration of p_fusion to get Gamow Peak Area
    
    # Define the integration limits
    LOW = 10**-20  # Lower limit
    UP = 10**-10  # Upper limit
    
    
    # Number of subintervals (must be even for Simpson's rule)
    SUB = 10000000
    
    # Create an array of equally spaced points in the interval [LOW, UP],
    # (SUB+1 includes the last point 'UP')
    x = np.linspace(LOW, UP, SUB+1)
    
    # Calculate the values of the function at these points
    y = p_fusion()
    
    # Use Simpson's rule for integration
    result = integrate.simpson(y, x)
    log = np.log10(result)
    
    # output results
    print(m, T, result, log)

   # print("Mass:", m, "M☉", "Temp:", "%.0f" % T, "K", "Area:", "%.10f" % result, "LogA:", "%.2f" %  log)
