# -*- coding: utf-8 -*-

from django.test import TestCase

from .. import fields
from . import factories


class TestField(TestCase):
    def setUp(self):
        self.value = 'Encrypt mé unicode'
        self.encrypted = (
            b'gAAAAABUP8RQmzcfuItm2QduS4lMqYXQl9rfnX-Fmdq3gWz6g7350CrKDhFiA1FJ'
            + b'1t8tBLFOrqNMtM6l1rZBeS2zOKzMo8N_3TStSIk_uZ4DRwKIfDoKfD4='
        )

    def test_get_prep_value(self):
        encrypted_value = fields.EncryptedTextField().get_prep_value(self.value)
        self.assertNotEqual(encrypted_value, self.value)

    def test_to_python(self):
        encrypted_value = fields.EncryptedTextField().to_python(self.encrypted)
        self.assertEqual(encrypted_value, self.value)

    def test_south_field_triple(self):
        south_triple = fields.EncryptedTextField().south_field_triple()
        expected = ('django_field_cryptography.fields.EncryptedTextField', [], {})
        self.assertEqual(south_triple, expected)


class TestModel(TestCase):
    def test_value(self):
        value = 'Encrypt me'
        dummy_model = factories.DummyModelFactory.create(aes_field=value)
        self.assertEqual(dummy_model.aes_field, value)
