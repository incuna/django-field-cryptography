import factory

from .models import DummyModel


class DummyModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = DummyModel

    aes_field = factory.Sequence('encrypted message {}'.format)
