Django SimpleAES Field
======================
Provides a simple django CharField subclass which encodes itself using
[SimpleAES](https://github.com/nvie/SimpleAES/) in the database.

Installation
------------
Install with your favourite package manager:

    pip install django-simple-aes-field

Add `django-simple-aes-field` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'countries',
        ...
    )

Usage
-----

    from django_simple_aes_field.fields import AESField

    class MyModel(models.Model):
        my_secret_field = AESField()

