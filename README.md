# Django Field Cryptography [![Build Status](https://travis-ci.org/incuna/django-field-cryptography.svg?branch=master)](https://travis-ci.org/incuna/django-field-cryptography)

---

## Warning if you have used `django-simple-aes-field`

**`django-simple-aes-field` can be found under the tag [v0.1.3](https://github.com/incuna/django-field-cryptography/tree/v0.1.3).**

**This project was formely known as `django-simple-aes-field` which has been deprecated.**

To migrate from `django-simple-aes-field` to `django-field-cryptography`:

  - create a model with the new fields;
  - create a migration to transfer the data;
  - remove the old fields.

---


`django-field-cryptography` provides a django `TextField` subclass which
encodes itself using [cryptography](https://github.com/pyca/cryptography) in
the database.

`EncryptedTextField` uses [Fernet](https://cryptography.io/en/latest/fernet/)
which is an implementation of symmetric cryptography.

`Fernet` uses `AES` in `CBC` mode and `HMAC` for authentication.
See [implementation](https://cryptography.io/en/latest/fernet/#implementation)
for more details.

## Installation

Install with your favourite package manager:

```bash
    pip install django-field-cryptography
```

Add `FERNET_KEY` to your `settings.py`. A `FERNET_KEY` should contains 32
characters and should be encoded with `base64`. It's possible to generate
one with the `cryptography` library.

To generate a key:
```python
>>> from cryptography.fernet import Fernet
>>> Fernet.generate_key()
b'your_key...'
>>>
```

In `settings.py`:
```python
FERNET_KEY = b'your_key...'
```

## Usage

```python
    from django_cryptography.fields import EncryptedTextField

    class MyModel(models.Model):
        my_secret_field = EncryptedTextField()
```

