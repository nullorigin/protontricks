from .steam import *
from .winetricks import *
from .gui import *
from .util import *

try:
    from setuptools import version as __version__
except ImportError:
    # Package not installed
    __version__ = "unknown"
