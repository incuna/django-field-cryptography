# Django SimpleAES Field [![Build Status](https://travis-ci.org/incuna/django-simple-aes-field.svg?branch=master)](https://travis-ci.org/incuna/django-simple-aes-field)

Provides a simple django `CharField` subclass which encodes itself using
[SimpleAES](https://github.com/nvie/SimpleAES/) in the database.

If you installed `v0.1.2` or lower, newer versions are not backward compatible as
we've changed the encryption method.

Migrating from `v0.1.2` or lower would involve to:

  - remove AESField from your model;
  - decrypt and save the data in a temporary table;
  - update this library;
  - create a migration to save data from the temporary table to your model;
  - delete the table;

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
