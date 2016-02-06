#!/usr/bin/env python

import numpy as np


def chebyshev(func, interval, degree=7, precision=20):
    n = degree + 1

    # x ∈ [a, b]
    a, b = interval

    #     2 x - a - b
    # u = -----------
    #        b - a
    #
    #      b - a     a + b
    # x =  ----- u + -----
    #        2         2
    #
    #       2 i - 1
    # cos ( ------- π ), i = 1, ..., degree
    #         2 n
    #
    #         i - 0.5
    # = cos ( ------- π ), i = 1, ..., degree
    #            n
    #
    #         i + 0.5
    # = cos ( ------- π ), i = 0, ..., degree + 1
    #            n
    #
    #         i + 0.5
    # = cos ( ------- π ), i = 0, ..., n
    #            n
    result_u = np.cos((np.arange(n) + 0.5) / n * np.pi)
    result_x = (b - a) / 2 * result_u + (a + b) / 2
    result_y = np.vectorize(func)(result_x)

    #
    # T_0(u) = 1
    # T_1(u) = u
    # T_i+2(u) = 2u T_i+1(u) - T_i(u)
    #
    #                   -1
    # T_n(u) = cos(n cos  (u))
    #

    t = [np.ones(result_u.shape), result_u]

    for _ in range(n-2):
        t.append(2 * t[1] * t[-1] - t[-2])

    t = np.vstack(t).T

    #
    # c_i
    #
    #       n-1
    # c_0 =  Σ  y_i
    #       i=0
    #       --------
    #          n
    #
    #         n-1
    # c_k = 2  Σ  ( T_k(u_i) y_i )
    #         i=0
    #       --------------------
    #                n

    c = 2 * result_y.dot(t) / n
    c[0] /= 2

    #             n
    # y = f(x) =  Σ  ( C_i * T_i(u) )
    #            i=1

    def y(x):
        u = (2 * x - a - b) / (b - a)
        total = c[0]

        t = [1, u]

        for _ in range(n-2):
            t.append(2 * t[1] * t[-1] - t[-2])

        return sum(c * t)

    return y


if __name__ == '__main__':

    # the usage of approxmation function should not exceed the given interval,
    # otherwise it may has larger error

    from math import sin, pi

    f = chebyshev(sin, (0, pi/4), 10)

    print("[function result] {:.20f}".format(sin(0.7)))
    print("[approxmation   ] {:.20f}".format(f(0.7)))
