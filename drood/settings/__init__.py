"""
Settings used by drood project.

This consists of the general production settings, with an optional import of any local
settings.
"""

# Import production settings.
from drood.settings.production import *

# Import optional local settings.
try:
    from drood.settings.local import *
except ImportError:
    pass
