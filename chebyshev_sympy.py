#!/usr/bin/env python

from sympy import symbols, cos, pi
from sympy.core.numbers import One


def chebyshev(func, interval, degree=7, precision=20):
    n = degree + 1

    x, u = symbols('x u')

    # x ∈ [a, b]
    a, b = interval

    #     2 x - a - b
    # u = -----------
    #        b - a
    x_to_u = (2 * x - a - b) / (b - a)

    #      b - a     a + b
    # x =  ----- u + -----
    #        2         2
    u_to_x = (b - a) / 2 * u + (a + b) / 2

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
    chebyshev_nodes = cos((symbols('i') + 0.5) / n * pi)

    result_u = [ chebyshev_nodes.evalf(precision, subs={'i': i}) for i in range(n) ]
    result_x = [ u_to_x.evalf(precision, subs={u: i}) for i in result_u ]
    result_y = [ func(i) for i in result_x ]

    #
    # T_0(u) = 1
    # T_1(u) = u
    # T_i+2(u) = 2u T_i+1(u) - T_i(u)
    #
    #                   -1
    # T_n(u) = cos(n cos  (u))
    #

    t = [One(), u]

    for _ in range(n-2):
        t.append(2 * u * t[-1] - t[-2])

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

    c = [ sum(result_y) / n ]

    for index in range(1, n):
        c.append( 2 * sum(t[index].evalf(precision, subs={u: i}) * j for i, j in zip(result_u, result_y)) / n )

    #             n
    # y = f(x) =  Σ  ( C_i * T_i(u) )
    #            i=1

    y = 1 * c[0]

    for i in range(1, n):
        y += t[i] * c[i]

    return y.subs({u: x_to_u}).simplify()


if __name__ == '__main__':

    # the usage of approxmation function should not exceed the given interval,
    # otherwise it may has larger error

    from math import sin, pi

    f = chebyshev(sin, (0, pi/4), 10)

    print("[formula        ]", f)
    print("[function result]", sin(0.7))
    print("[approxmation   ]", f.evalf(20, subs={'x': 0.7}))
