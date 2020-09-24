from distutils.core import setup
from Cython.Build import cythonize
import sys

if __name__ == "__main__":
	# setup(name = "compiled app", ext_modules = cythonize(sys.argv[1]))
	setup(name = "compiled app", ext_modules = cythonize("numba_ma.pyx"))
	# print(sys.argv)