from .base import *

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

try:
    from .local import *
except ImportError:
    pass
