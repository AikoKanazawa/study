from __future__ import print_function

import numpy as np
from scipy import optimize

# scipy.optimize.root_scalar
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar


def func(m, zj, beta, h):
    return m - np.tanh(beta * zj * (m + h))


def find_solution(zj, t, h, m_min=1e-6, m_max=1, verbose=False):
    beta = np.inf if t==0 else 1./t
    sol = optimize.root_scalar(func, args=(zj, beta, h), method='brentq', bracket=(m_min, m_max))
    if verbose:
        print(sol)
    return sol.root


def main():
    t = 0.1
    zj = 1.0
    h = 0.1
    m = find_solution(zj, t, h, verbose=True)
    print(f"zJ = {zj}")
    print(f"T  = {t}")
    print(f"h  = {h}")
    print(f"m  = {m}")


if __name__ == '__main__':
    main()