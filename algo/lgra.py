import numpy as np


def LGRA(matrix, ref):
    n = matrix.shape[0]
    m = matrix.shape[1]
    refmax = np.max(ref)
    refmin = np.min(ref)
    cmax = np.zeros(n)
    cmin = np.zeros(n)
    rmax = np.zeros(m)
    rmin = np.zeros(m)
    for i in range(n):
        cmax[i] = np.max(matrix[i, :])
        cmin[i] = np.min(matrix[i, :])
    for i in range(m):
        rmax[i] = np.max(matrix[:, i])
        rmin[i] = np.min(matrix[:, i])
    c = np.zeros(n)
    r = np.zeros(m)
    for i in range(n):
        if ref[i] >= refmax:
            c[i] = 1
        elif ref[i] <= refmin:
            c[i] = 0
        else:
            c[i] = (ref[i] - refmin) / (refmax - refmin)
    for i in range(m):
        for j in range(n):
            if matrix[j, i] >= rmax[i]:
                r[i] = 1
            elif matrix[j, i] <= rmin[i]:
                r[i] = 0
            else:
                r[i] += (rmax[i] - matrix[j, i]) / (rmax[i] - rmin[i])
        r[i] /= n
    p = np.zeros(n)
    for i in range(n):
        p[i] = sum(matrix[i, :] * r) / sum(matrix[i, :] * c)
    return p
