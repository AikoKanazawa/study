from __future__ import print_function

import numpy as np

from pct_adv_21 import find_solution


def main():
    h = 0
    tmin = 0
    tmax = 1
    n = 201
    for t in np.linspace(tmin, tmax, n):
        try:
            m = find_solution(1., t, h)
        except:
            print(f"# {t:.4f}")
        else:
            print(f"{t:.4f} {m:.5e}")


if __name__ == '__main__':
    main()