import math
from random import random


def f1(x):
    if type(x) == tuple:
        if x[0] < -20 or x[0] > 20:
            raise ValueError("x out of bounds")
        else:
            return abs(x[0]) + math.cos(x[0])
    else:
        if x < -20 or x > 20:
            raise ValueError("x out of bounds")
        else:
            return abs(x) + math.cos(x)


def f1_ddx(x):
    if x < -20 or x > 20:
        raise ValueError("x out of bounds")
    else:
        return (x / abs(x)) - math.sin(x)


def f6(x):
    if type(x) == tuple:
        if x[0] < -10 or x[0] > 10:
            raise ValueError("x out of bounds")
        else:
            return (x[0] ** 2 + x[0]) * math.cos(x[0])
    else:
        if x < -10 or x > 10:
            raise ValueError("x out of bounds")
        else:
            return (x ** 2 + x) * math.cos(x)


def f6_ddx(x):
    if x < -10 or x > 10:
        raise ValueError("x out of bounds")
    else:
        # d/dx = (2x+1)cos(x) - x(x+1)sin(x)
        return (2 * x + 1) * math.cos(x) - (x + 1) * x * math.sin(x)


def holder(x_vec):
    x = x_vec[0]
    y = x_vec[1]
    if x < -10 or x > 10:
        raise ValueError("x out of bounds")
    elif y < -10 or y > 10:
        raise ValueError("y out of bounds")
    else:
        part1 = math.sin(x) * math.cos(y)
        part2 = abs(1 - (math.sqrt(x ** 2 + y ** 2) / math.pi))
        holder = -abs(part1 * math.exp(part2))
        return holder


def new_move_in_range(dims, min, max):
    x = []
    for d in range(dims):
        x.append(min + (random() * (max - min)))
    return tuple(x)


def gradient_descent(f_ddx, x0, eta, max_iter):
    x = x0
    for i in range(max_iter):
        x1 = x - eta * f_ddx(x)
        if x == x1:
            break
        x = x1
    return x


gradient_descent(f1_ddx, 8, 0.05, 10000)
