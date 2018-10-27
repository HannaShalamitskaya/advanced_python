from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibonacci_cython.pyx"),
    name='fibonacci_cython',
    version='1.0',
    author="Hanna Shalamitskaya",
    description='Cython Package forcalculation n items of the fibonacci series',
)
