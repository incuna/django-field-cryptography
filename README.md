# Django SimpleAES Field [![Build Status](https://travis-ci.org/incuna/django-simple-aes-field.svg?branch=master)](https://travis-ci.org/incuna/django-simple-aes-field)

Provides a simple django `CharField` subclass which encodes itself using
[SimpleAES](https://github.com/nvie/SimpleAES/) in the database.

## Installation

Install with your favourite package manager:

```bash
    pip install django-simple-aes-field
```

Add `django-simple-aes-field` to your `INSTALLED_APPS`:

```python
    INSTALLED_APPS = (
        ...
        'django_simple_aes_field',
        ...
    )
```

## Usage

```python
    from django_simple_aes_field.fields import AESField

    class MyModel(models.Model):
        my_secret_field = AESField()
```
