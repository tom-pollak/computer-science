import math

from test_functions import *


def gradient_descent(x0, eta, max_iter, func, print_rate=25):
    i = 0
    x = x0
    while i < max_iter:
        x1 = x - eta * func(x)
        if x == x1:
            break
        x = x1
        i += 1
        if print_rate > 0 and i % print_rate == 0:
            print(str(i) + " : " + str(x))
    return x


def simulated_annealing(x0, t0, iter_per_temp, func, func_range, print_rate=25):
    stopping = False
    temp = t0
    x = x0
    dims = len(x0)
    ii = 0

    while not stopping:
        for i in range(iter_per_temp):
            m1 = new_move_in_range(dims, func_range[0], func_range[1])
            diff = func(m1) - func(x)
            if diff < 0:
                x = m1
            elif math.exp(-diff / temp) > random():
                x = m1

            if print_rate > 0 and ii % print_rate == 0:
                print("Temp: " + str(temp) + "\t x: " + str(x))
            ii += 1
        temp = temp * 0.995
        if temp < 0.005:
            stopping = True
    return x


# gradient_descent(12.5, 0.05, 10000, f1_ddx, 25)

simulated_annealing((12.5,), 50, 100, f1, (-20, 20), 2000)
simulated_annealing((3.5, 3.5), 50, 100, holder, (-10, 10), 2000)
