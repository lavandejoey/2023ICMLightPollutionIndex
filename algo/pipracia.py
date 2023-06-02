import numpy as np


def PIPRECIA(matrix):
    n = matrix.shape[0]
    s = np.zeros(n)
    r = np.zeros(n)
    k = np.zeros(n)
    for i in range(n):
        s[i] = sum(matrix[i, :])
        r[i] = sum(matrix[:, i])
    rbar = np.mean(r)
    for i in range(n):
        k[i] = s[i] / (s[i] + rbar)
    w = k / sum(k)
    v = np.zeros(n)
    for i in range(n):
        v[i] = sum(matrix[i, :] * w)
    return v
