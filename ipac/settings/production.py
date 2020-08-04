from .base import *

ALLOWED_HOSTS = ['www.ipacindo.com']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
