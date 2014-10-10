from setuptools import setup, find_packages


version = '0.1.3'


setup(
    name='django-simple-aes-field',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    license='BSD',
    description='A SimpleAES encoded field for Django.',
    install_requires=('SimpleAES>=0.2',),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database',
    ),
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-simple-aes-field',
)
