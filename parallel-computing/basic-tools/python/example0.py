import numpy as np
# instantiate and configure the worker pool
# from pathos.multiprocessing import ProcessPool
# pool = ProcessPool(nodes=4)

from pathos.pp import ParallelPool
import time


if __name__ == '__main__':

	pool = ParallelPool(nodes=4)

	B = 100000

	print("------------- ParallelPool ---------------")
	start_time = time.time()
	# do a blocking map on the chosen function
	a = pool.map(pow, list(np.arange(B)), list(np.ones(B)*2))
	print("--- %s seconds ---" % (time.time() - start_time))


	print("------------- Normal ---------------")
	start_time = time.time()
	# do a blocking map on the chosen function
	b = [pow(i,2) for i in range(B)]
	print("--- %s seconds ---" % (time.time() - start_time))