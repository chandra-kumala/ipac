from .base import *

ALLOWED_HOSTS = ['127.0.0.1', 'www.ipacindo.com']


DEBUG = False

try:
    from .local import *
except ImportError:
    pass
