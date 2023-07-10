from distutils.core import setup
from Cython.Build import cythonize
import numpy
from distutils.extension import Extension

setup(
  name = 'monotonic_align',
  ext_modules = cythonize([Extension(name='core',sources=['core.pyx'])])
,
  include_dirs=[numpy.get_include()]
)
