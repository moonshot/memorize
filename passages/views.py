from .models import Passage, Phrase
from rest_framework import viewsets
from .serializers import PassageSerializer, PhraseSerializer


class PassageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows passages to be viewed or edited.
    """
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer


class PhraseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows phrases to be viewed or edited.
    """
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
