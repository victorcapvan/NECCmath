import numpy as np
import pprint
import typing

def eulers_method(f: typing.Callable[[float, float], float], initial_conditions: tuple[float, float], h: float, n: int, decimals: int) -> np.matrix:
    
    """
    @param f: function in terms of x, y
    @param initial_conditions: (x, y) as a tuple
    @param h: step size
    @param n: number of iterations
    @param decimals: numbers of decimals that the solutions are rounded to
    """
    
    (x_n, y_n) = initial_conditions
    solution_set = [(0, *initial_conditions, f(*initial_conditions))]

    for i in range(n):
        f_n = f(x_n, y_n)
        x_n = x_n + h
        y_n = y_n + h * f_n
        solution_set.append((i + 1, x_n, y_n, f_n))
        
    solution_set = [(i, round(x, decimals), round(y, decimals), round(f_n, decimals)) for (i, x, y, f_n) in solution_set]
    
    return np.array(solution_set)

pprint.pprint(eulers_method(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 25, 5)) # Shaun's number 4 from 1.4)
pprint.pprint(eulers_method(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 10, 5)[-1])
pprint.pprint(eulers_method(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 10, 5)[-1][2])
