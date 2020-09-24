import numpy as np

def numba_ma(double[:] x, int m):
	cdef int n = len(x), i
	cdef double[:] x_ma = np.full(n,np.nan)
	cdef double next_value = 0.0

	for i in range(n):
		next_value += x[i] / m
		if i >= m - 1:
			x_ma[i] = next_value
			next_value -= x[i - m + 1] / m
	return x_ma