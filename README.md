Django SimpleAES Field
======================

Provides a simple django CharField subclass which encodes itself using
[SimpleAES](https://github.com/nvie/SimpleAES/) in the database.

Usage
-----

    from django_simple_aes_field import AESField

    class MyModel(models.Model):
        my_secret_field = AESField()
