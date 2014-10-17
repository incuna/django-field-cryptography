#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691"""
import sys

from colour_runner.django_runner import ColourRunnerMixin
import dj_database_url
from django.conf import settings


settings.configure(
    DATABASES={
        'default': dj_database_url.config(default='postgres://localhost/encrypted_field'),
    },
    INSTALLED_APPS=('django_field_cryptography.tests',),
    MIDDLEWARE_CLASSES = (),
    FERNET_KEY=b'pLw0TKXzFxIQTuuDZl4sXpkJkmDLbvpfVzl5-FHgayE=',
)

import django
if django.VERSION >= (1, 7):
    django.setup()

from django.test.runner import DiscoverRunner


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    pass


test_runner = TestRunner(verbosity=1)
failures = test_runner.run_tests(['django_field_cryptography'])
if failures:
    sys.exit(1)
