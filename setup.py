from setuptools import setup, find_packages


version = '0.1.3'


setup(
    name='django-field-cryptography',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    license='BSD',
    description='An encrypted field for Django.',
    install_requires=('cryptography>=0.6,<0.7',),
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
    url='https://github.com/incuna/django-field-cryptography',
)
