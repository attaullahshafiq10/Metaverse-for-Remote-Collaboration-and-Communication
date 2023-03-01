# Ambisonics Algorithm in Python

def ambisonics_basis_functions(order, x, y, z):
    """
    Compute ambisonics basis functions for a given order and position.

    Parameters:
    order (int): ambisonics order
    x (float): x coordinate
    y (float): y coordinate
    z (float): z coordinate

    Returns:
    numpy array: ambisonics basis functions of shape (num_coefficients,)
    """
    num_coefficients = (order + 1)**2
    basis_functions = np.zeros(num_coefficients)

    for n in range(order + 1):
        for m in range(-n, n + 1):
            index = n**2 + n + m
            basis_functions[index] = ambisonics_basis_function(order, n, m, x, y, z)

    return basis_functions


def ambisonics_basis_function(order, n, m, x, y, z):
    """
    Compute a single ambisonics basis function for a given order, degree, and position.

    Parameters:
    order (int): ambisonics order
    n (int): degree of basis function
    m (int): order of basis function
    x (float): x coordinate
    y (float): y coordinate
    z (float): z coordinate

    Returns:
    float: ambisonics basis function
    """
    if m > 0:
        return np.sqrt(2) * ambisonics_pnm(n, m, z) * np.cos(m * np.arctan2(y, x))
    elif m < 0:
        return np.sqrt(2) * ambisonics_pnm(n, -m, z) * np.sin(-m * np.arctan2(y, x))
    else:
        return ambisonics_pnm(n, m, z)


def ambisonics_pnm(n, m, x):
    """
    Compute a single spherical harmonic function for a given degree, order, and position.

    Parameters:
    n (int): degree of spherical harmonic function
    m (int): order of spherical harmonic function
    x (float): position on the unit sphere

    Returns:
    float: spherical harmonic function
    """
    if m == 0:
        return ambisonics_legendre(n, x)
    elif m > 0:
        return np.sqrt(2) * np.cos(m * np.arccos(x)) * ambisonics_legendre(n, x)
    else:
        return np.sqrt(2) * np.sin(-m * np.arccos(x)) * ambisonics_legendre(n, x)


def ambisonics_legendre(n, x):
    """
    Compute the nth degree Legendre polynomial for a given position.

    Parameters:
    n (int): degree of Legendre polynomial
    x (float): position on the unit sphere

    Returns:
    float: Legendre polynomial
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * ambisonics_legendre(n - 1, x) - (n - 1) * ambisonics_legendre(n - 2, x)) / n

