############### try a package called joblib ################


import numpy as np
# instantiate and configure the worker pool
# from pathos.multiprocessing import ProcessPool
# pool = ProcessPool(nodes=4)

from joblib import Parallel, delayed
import time


if __name__ == '__main__':

	# pool = ParallelPool(nodes=4)

	B = 1000000

	print("------------- Parallel ---------------")
	start_time = time.time()
	# do a blocking map on the chosen function
	# a = pool.map(pow, list(np.arange(B)), list(np.ones(B)*2))
	a = Parallel(n_jobs=5)(delayed(pow)(i,2) for i in range(B))
	print("--- %s seconds ---" % (time.time() - start_time))


	print("------------- Normal ---------------")
	start_time = time.time()
	# do a blocking map on the chosen function
	b = [pow(i,2) for i in range(B)]
	print("--- %s seconds ---" % (time.time() - start_time))