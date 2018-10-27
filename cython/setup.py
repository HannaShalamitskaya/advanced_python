from Cython.Build import cythonize
from distutils.core import setup

setup(
    ext_modules=cythonize("fibonacci_cython.pyx"),
    name='fibonacci_cython',
    version='1.0',
    author="Hanna Shalamitskaya",
    description='Cython Package calculating n items of the fibonacci series',
)
