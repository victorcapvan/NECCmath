import numpy as np, pprint as pp, typing as t

def eulersMethod(f: t.Callable[[float, float], float], initial_conditions: tuple[float, float], h: float, n: int, show_all: bool = True) -> None:
    x_n, y_n = initial_conditions
    solution_set = [(0, *initial_conditions, f(*initial_conditions))]
    for i in range(n):
        (x_n, y_n) = (x_n + h, y_n + h * (f_n := f(x_n, y_n)))
        solution_set.append((i + 1, x_n, y_n, f_n))     
    pp.pprint(np.array(solution_set)) if show_all else print(solution_set[-1]); print("\n")
    return

# number 8 from 1.4
eulersMethod(lambda x, t: 1 - x**2, (0, 363), 0.0025, 300, False) # number 8 from 1.4

# dT/dt = K(M(t) - T(t))
eulersMethod(lambda t, T: 0.04 * (294 - T), (0, 363), 0.1, 300, False) # number 9 from 1.4
eulersMethod(lambda t, T: 0.04 * (294 - T), (0, 363), 0.1, 600, False)

eulersMethod(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 10, True) # Shaun's number 4 from 1.4