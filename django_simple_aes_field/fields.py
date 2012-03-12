from django.conf import settings
from django.db import models

from SimpleAES import SimpleAES


aes = SimpleAES(settings.SECRET_KEY)

class AESField(models.CharField):

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        return super(AESField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return aes.base64_encrypt(str(value))

    def to_python(self, value):
        try:
            return aes.base64_decrypt(value)
        except:
            return value

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], ["^django_simple_aes_field\.fields\.AESField"])

