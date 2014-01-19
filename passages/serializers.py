from .models import Passage, Phrase
from rest_framework import serializers


class PassageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passage
        fields = ('name',)


class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phrase
        fields = ('text', 'passage')
