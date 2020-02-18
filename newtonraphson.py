

""" Write a Python module newtonraphson.py that contains functions to 
find the roots of an equation for a polynomial in x using the 
Newton-Raphson method. 

Coefficients should be an iterable (tuple or list) of coefficients 
for the powers of x.  As an example:

    7𝑥^4 + 3𝑥^3 − 5𝑥^2 + 32𝑥 − 7𝑥^0 = 0

    would be represented as [7, 3,−5, 32,−7].    
    Show the answers for the equation above given 
    starting points of x=5 and x = -50:

    NewtonRaphson( [7, 3, -5, 32, -7], 5) and 
    NewtonRaphson( [7, 3, -5, 32, -7], -50)

Note that only real roots will be returned when we start the search 
with a real value.  YOU MAY NOT USE ANY library functions for taking 
derivatives or evaluating polynomials.

"""

# Solution Function

def NewtonRaphson(fpoly, a, tolerance = .00001):     
    """Given a set of polynomial coefficients fpoly 
    for a univariate polynomial function, 
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,     
    find the real roots of the polynomial (if any)      
    using the Newton-Raphson method.    

    a is the initial estimate of the root and      
    starting state of the search.  

    This is an iterative method that stops when the     
    change in estimators is less than tolerance.
"""
# Auxillary Functions

def polyval(fpoly, x):    
    """polyval(fpoly, x)     
    Given a set of polynomial coefficients from highest order to x^0,    
    compute the value of the polynomial at x.  We assume zero     
    coefficients are present in the coefficient list/tuple. 

    Example:  f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5       
    polyval([4, 0, 9, 3], 5))    
    returns 548    
    """

def derivative(fpoly):    
    """derivative(fpoly)     
    Given a set of polynomial coefficients from highest order to x^0,    
    compute the derivative polynomial.  We assume zero coefficients     
    are present in the coefficient list/tuple.

    Returns polynomial coefficients for the derivative polynomial.    
    Example:    
    derivative((3,4,5))  # 3 * x**2 + 4 * x**1 + 5 * x**0    
    returns:  [6, 4]     # 6 * x**1 + 4 * x**0     
    """