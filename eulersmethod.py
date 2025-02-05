import typing as t

def f(f: t.Callable[[float, float], float], initial_conditions: tuple[float, float], h: float, n: int, show_all: bool = True) -> None:
    (x_n, y_n), result_list = initial_conditions, [(0, *initial_conditions, f(*initial_conditions))]
    for i in range(n):
        (x_n, y_n) = (x_n + h, y_n + h * (f_n := f(x_n, y_n)))
        result_list.append((i + 1, x_n, y_n, f_n))
    show_all and [print(element) for element in result_list] or print(result_list[-1]); print("\n")
    return

f(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 10, True)