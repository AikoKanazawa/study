from __future__ import print_function

import numpy as np

from pct_adv_23 import find_solution


def main():
    hmin = 0
    hmax = 0.11
    tmin = 0
    tmax = 1
    n = 201
    for t in np.linspace(tmin, tmax, n):
        for h in np.linspace(hmin, hmax, n):
            try:
                m = find_solution(1., t, h)
            except:
                print(f"# {t:.4f}")
            else:
                print(f"{h:.4f} {t:.4f} {m:.5e}")


if __name__ == '__main__':
    main()