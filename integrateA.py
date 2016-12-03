import numpy as np

# количество отрезков для разбиения
n = 1E3
# левая граница
L0 = 0.0
# правая граница
L1 = 80 # cm
# высота провисания
d = 0.5 # cm
# угол провисания
a = (2.0 / L1) * np.arccosh(d + 1.0)

def integral(x):
    return np.sqrt(1 + np.power(a * np.sinh(a * (x - L1 / 2)), 2))

if __name__ == '__main__':
    h = (L1 - L0) / n
    d1 = lambda r: (r - L1) *100 / L1

    result = h * sum([integral(xi - h / 2.0) for xi in np.arange(L0, L1, h)])
    print('<square> L(d) = {}'.format(result))
    print('delta = {} %'.format(d1(result)))

    result = 0
    x_j = lambda j: L0 + j * h
    for k in range(1, int(n), 2):
        result += integral(x_j(k-1)) + 4 * integral(x_j(k)) + integral(x_j(k+1))
    result *= h / 3.0
    print('<simpson> L(d) = {}'.format(result))
    print('delta = {} %'.format(d1(result)))
