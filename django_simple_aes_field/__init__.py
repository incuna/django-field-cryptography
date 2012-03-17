from .fields import AESField


__version__ = (0, 1, 2)

def get_version():
    return '.'.join(map(str, __version__))

__all__ = ['AESField']

