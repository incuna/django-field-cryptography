from setuptools import setup, find_packages

from django_simple_aes_version.version import get_version


setup(
    name = 'django-simple-aes-field',
    packages = find_packages(),
    include_package_data=True,
    version = get_version(),
    description = 'A SimpleAES encoded field for Django.',
    author = 'Incuna Ltd',
    author_email = 'dev@incuna.com',
    url = 'http://incuna.com/',
)
