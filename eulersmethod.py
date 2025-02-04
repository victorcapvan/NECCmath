import numpy as np, pprint as pp, typing as t

def f(f: t.Callable[[float, float], float], initial_conditions: tuple[float, float], h: float, n: int) -> None:
    (x_n, y_n) = initial_conditions 
    result_list = [(0, x_n, y_n, f(x_n, y_n))]
    for i in range(n):
        (x_n, y_n) = (x_n + h, y_n + h * (f_n := f(x_n, y_n)))
        result_list.append((i + 1, x_n, y_n, f_n))       
    pp.pprint(np.array(result_list))
    return

f(lambda x, y: (9/x**2) - (y/x) - y**2, (2, -3/2), 0.1, 10)