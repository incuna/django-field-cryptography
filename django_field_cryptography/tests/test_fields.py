from django.test import TestCase

from .. import fields
from . import factories


class TestField(TestCase):
    def setUp(self):
        self.value = 'Encrypt me'
        self.encrypted = (
            b'gAAAAABUPl6KukHnYKy2h3kKathdY6LDtnYzbEUFgGLX-JxUHyw'
            + b'K4XF2NKeyNHEj2AIXjFR-keSPoFEKY20qKRiidrIevKpQPQ=='
        )

    def test_get_prep_value(self):
        encrypted_value = fields.EncryptedTextField().get_prep_value(self.value)
        self.assertNotEqual(encrypted_value, self.value)

    def test_to_python(self):
        encrypted_value = fields.EncryptedTextField().to_python(self.encrypted)
        self.assertEqual(encrypted_value, self.value)


class TestModel(TestCase):
    def test_value(self):
        value = 'Encrypt me'
        dummy_model = factories.DummyModelFactory.create(aes_field=value)
        self.assertEqual(dummy_model.aes_field, value)
