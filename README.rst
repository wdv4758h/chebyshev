========================================
Chebyshev Approximation
========================================

Give me a function, I'll give you a polynomial approximation.


For actual use, consider implementation in the below links :

* `NumPy - Chebyshev Module <http://docs.scipy.org/doc/numpy/reference/routines.polynomials.chebyshev.html>`_
* `SymPy - Function approximation <http://docs.sympy.org/dev/modules/mpmath/calculus/approximation.html>`_


Dependency
========================================

Chebyshev - SymPy
------------------------------

* Python
* `SymPy <https://github.com/sympy/sympy>`_


Chebyshev - NumPy
------------------------------

(this implementation is faster than ``chebyshev_sympy.py``)

* Python
* `NumPy <https://github.com/numpy/numpy>`_


Usage
========================================

look the example at the end of the ``chebyshev_sympy.py``

.. code-block:: sh

    $ ./chebyshev_sympy.py
    [formula        ] x*(-1.05140968116488e-7*x**9 + 2.94906160251081e-6*x**8 - 2.02095616447828e-7*x**7 - 0.000198281116601832*x**6 - 5.51329792038988e-8*x**5 + 0.00833334818611353*x**4 - 2.49652847988328e-9*x**3 - 0.166666666421714*x**2 - 1.23325091579106e-11*x + 1.00000000000024)
    [function result] 0.644217687237691
    [approxmation   ] 0.64421768723769211138

    $ ./chebyshev_numpy.py
    [function result] 0.64421768723769101683
    [approxmation   ] 0.64421768723769079479



Usage in Other Implementation
========================================

SymPy - chebyfit
------------------------------

.. code-block:: python

    # mpmath.chebyfit(ctx, f, interval, N, error=False)

    from sympy.mpmath import mp, chebyfit, polyval
    from math import sin, pi

    mp.pretty = True    # this will make "mpf('42.0')" display as "42.0"
    poly, err = chebyfit(sin, [0, pi/4], 10, error=True)

    print(polyval(poly, 0.7))   #  c_n x^n + \ldots + c_2 x^2 + c_1 x + c_0
    # 0.644217687237708
    print(err)
    # 1.95187454392545e-14



Reference
========================================

* `Wikipedia - Chebyshev polynomials <https://en.wikipedia.org/wiki/Chebyshev_polynomials>`_
