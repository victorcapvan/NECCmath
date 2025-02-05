import typing as t

def f(f: t.Callable[[float, float], float], initial_conditions: tuple[float, float], h: float, n: int, show_all: bool = True) -> None:
    x_n, y_n = initial_conditions
    solution_set = [(0, *initial_conditions, f(*initial_conditions))]
    for i in range(n):
        (x_n, y_n) = (x_n + h, y_n + h * (f_n := f(x_n, y_n)))
        solution_set.append((i + 1, x_n, y_n, f_n))
    show_all and [print(element) for element in solution_set] or print(solution_set[-1]); print("\n")
    return

f(lambda x, y: (1/x**2) - (y/x) - y**2, (1, -1), 0.1, 10, True)