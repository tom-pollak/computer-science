from random import random
import math


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


def gradient_descent(f_ddx, x, alpha, epsilon):
    """Gradient descent algorithm
    :param f_ddx: differntiated function to optimize
    :param x: starting point
    :param alpha: learning rate
    :param epsilon: convergence criteria
    :return: minimizer of f
    """
    x_old = x
    x_new = x
    while True:
        x_new = x_old - alpha * f_ddx(x_old)
        print(x_old, f_ddx(x_old))
        if abs(x_new - x_old) < epsilon:
            break
        x_old = x_new
    return x_new


def boltzmann_distribution(x, T):
    """Boltzmann distribution
    :param x: value to evaluate
    :param T: temperature
    :return: probability of x
    """
    return math.exp(x / T) / (math.exp(x / T) + 1)


def simulated_annealing(f, x, T, alpha, epsilon):
    """Simulated annealing algorithm
    :param f: function to optimize
    :param x: starting point
    :param T: temperature
    :param alpha: learning rate
    :param epsilon: convergence criteria
    :return: minimizer of f
    """
    x_old = x
    x_new = x
    while True:
        x_new = x_old - alpha * f(x_old)
        if boltzmann_distribution(f(x_new), T) > boltzmann_distribution(f(x_old), T):
            x_old = x_new
        else:
            if random() < boltzmann_distribution(f(x_new), T):
                x_old = x_new
        if abs(x_new - x_old) < epsilon:
            break
    return x_new


print(gradient_descent(f6_ddx, 1, 0.05, 0.000000001))
