from django.db import models

from ..fields import EncryptedTextField


class DummyModel(models.Model):
    aes_field = EncryptedTextField()
