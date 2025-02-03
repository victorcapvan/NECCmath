import typing

def f(f: typing.Callable[[float, float], float], initial: tuple[float, float], h: float, n: int) -> None:
    (x, y) = initial
    x_list = []
    y_list = []
    f_list = []
    for i in range(n):
        f_n = f(x, y)
        f_list.append(f_n)
        y += h*f_n
        x += h
        x_list.append(x)
        y_list.append(y)   
    print(f"x_list {x_list}")
    print(f"y_list {y_list}")
    print(f"f_list {f_list}")
    return

f(lambda x, y: ((1/x)*(y**2 + y)), (6, 3), 0.2, 4)