from distutils.core import setup
from distutils.core import Extension

sfc_module = Extension('fibonacci', sources=['fibonacci.cpp'])

setup(
    name='fibonacci',
    version='1.0',
    author="Hanna Shalamitskaya",
    description='Python Package with fibonacci C++ extension',
    ext_modules=[sfc_module]
)
