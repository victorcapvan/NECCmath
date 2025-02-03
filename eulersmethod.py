import typing
import numpy as np
import pprint

def f(f: typing.Callable[[float, float], float], initial: tuple[float, float], h: float, n: int) -> None:
    x, y = initial
    result_list = []
    for i in range(n):
        f_n = f(x, y)
        y += h * f_n
        x += h
        result_list.append((i + 1, x, y, f_n)) # (n, x_n, y_n, f_n)
    result_matrix = np.array(result_list)
    pprint.pprint(result_matrix)
    return

f(lambda x, y: ((9/x**2) - (y/x) - y**2), (2, -(3/2)), 0.1, 10)
