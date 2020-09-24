import numpy as np
import pandas as pd
from tqsdk.tafunc import ma
import time
import numba
import numba_ma as numba_ma_c

def numpy_ma(x,m):
	n = len(x)
	x_ma = np.full(n,np.nan)
	next_value = 0
	for i in range(n):
		next_value += x[i] / m
		if i >= m - 1:
			x_ma[i] = next_value
			next_value -= x[i - m + 1] / m
	return x_ma

@numba.jit
def numba_ma(x,m):
	n = len(x)
	x_ma = np.full(n,np.nan)
	next_value = 0
	for i in range(n):
		next_value += x[i] / m
		if i >= m - 1:
			x_ma[i] = next_value
			next_value -= x[i - m + 1] / m
	return x_ma

if __name__ == "__main__":
	n = 1000000
	a = np.array([[i,i] for i in range(n)]).reshape((-1))
	a = np.array([x for x in [1,1,2,2,3,3,4,4,5,5,6,6,7,7]*100000])

	start = time.time()	
	out = pd.Series(a).rolling(window = 2).mean()
	# print(out)
	end = time.time()
	print(f"pandas_ma: {end-start} seconds.")

	start = time.time()
	out = ma(pd.Series(a),2)
	# print(out)
	end = time.time()
	print(f"tqsdk.tafunc.ma: {end-start} seconds.")
	
	start = time.time()
	out = numpy_ma(a,2)
	# print(out)
	end = time.time()
	print(f"numpy_ma: {end-start} seconds.")

	numba_ma(np.array([1,1]),2)
	start = time.time()
	out = numba_ma(a,2)
	# print(out)
	end = time.time()
	print(f"numba_ma: {end-start} seconds.")

	a = a.astype(float)
	start = time.time()
	out = numba_ma_c.numba_ma(a,2)
	# print(out)
	end = time.time()
	print(f"numba_ma pre-compiled: {end-start} seconds.")
