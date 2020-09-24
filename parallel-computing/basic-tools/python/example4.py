import numpy as np
import multiprocessing
import time


# if __name__ == '__main__':

def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	print('Done sleeping...')

if __name__ == '__main__':

	n_repeat = 5
	sleep_time = 2

	# print("------------- Normal ---------------")
	# start = time.perf_counter()

	# for _ in range(n_repeat):
	# 	do_something(sleep_time)
	# finish = time.perf_counter()
	# print(f'Finished in {round(finish - start,2)} second(s)')

	print("------------- Multiprocessing ---------------")
	start = time.perf_counter()

	processes = []
	n_jobs = n_repeat

	for _ in range(n_jobs):
		p = multiprocessing.Process(target = do_something,args = [sleep_time])
		p.start()
		processes.append(p)

	for process in processes:
		process.join()

	finish = time.perf_counter()
	print(f'Finished in {round(finish - start,2)} second(s)')