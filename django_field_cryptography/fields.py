from django.conf import settings
from django.db import models
from django.utils.encoding import force_bytes, force_str

from cryptography.fernet import Fernet


fernet = Fernet(settings.FERNET_KEY)


class EncryptedTextField(models.TextField):
    """A TextField encrypted with Fernet (AES).

    EncryptedTextField rely on `Fernet` from `cryptography` to ensure symetric
    encryption. This field is compatible with South migrations.
    """
    def get_prep_value(self, value):
        return fernet.encrypt(force_bytes(value))

    def to_python(self, value):
        decrypted = fernet.decrypt(value)
        return force_str(decrypted)

    def south_field_triple(self):
        """Returns a suitable description of this field for South."""
        from south.modelsinspector import introspector
        field_class = '{}.{}'.format(self.__class__.__module__, self.__class__.__name__)
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
