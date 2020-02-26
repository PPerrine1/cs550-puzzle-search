def NewtonRaphson(fpoly, a, tolerance=.00001):
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
    n = 100  # Set max amount of loops

    # Utilize Newton Raphson method n times
    for i in range(n):
        # Calculate b (x-intercept) of line tangent to fpoly
        # Using approximate value a
        b = a - polyval(fpoly, a) / polyval(derivative(fpoly), a)

        # If the difference between a and b is less than tolerance, return b
        if abs(a - b) < tolerance:
            break
        elif i == n:
            raise Exception("No root found")
        else:
            # Else, set b as new approximation and continue loop
            a = b

    return b


""" Auxillary Functions """


def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the value of the polynomial at x.  We assume zero
    coefficients are present in the coefficient list/tuple.

    Example:  f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
    polyval([4, 0, 9, 3], 5))
    returns 548
    """
    val = 0
    # Find sum of each term when plugging in x
    for i, c in enumerate(fpoly, 1):
        val += c * round(x, 6) ** (len(fpoly) - i)
    return val


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
    # Find derivative by looping through fpoly and multiplying the coefficient
    # by the respective index starting at 1
    deriv = [c * (len(fpoly) - i) for i, c in enumerate(fpoly, 1)]

    # Return slice of derivative, removing 0 term
    return deriv[0:2]


if __name__ == '__main__':
    print(NewtonRaphson([4, 0, 9, 3], 5))
