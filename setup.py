from setuptools import setup, find_packages

from django_simple_aes_field import get_version


setup(
    name = 'django-simple-aes-field',
    packages = find_packages(),
    include_package_data=True,
    version = get_version(),
    description = 'A SimpleAES encoded field for Django.',
    install_requires = (
        'SimpleAES>=0.2',
    ),
    author = 'Incuna Ltd',
    author_email = 'dev@incuna.com',
    url = 'http://incuna.com/',
)
