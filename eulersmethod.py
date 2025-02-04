import numpy as np
import pprint as pp
import typing as t

def f(f: t.Callable[[float, float], float], initial: tuple[float, float], h: float, n: int) -> None:
    (x, y) = initial
    result_list = [(0, x, y, f(x, y))]
    for i in range(n):
        (x, y) = (x + h, y + h * (f_n := f(x, y)))
        result_list.append((i + 1, x, y, f_n))
    pp.pprint(np.array(result_list))
    return

f(lambda x, y: 9/x**2 - y/x - y**2, (2, -3/2), 0.1, 10)