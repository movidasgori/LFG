from rest_framework import viewsets

from .serializers import JuegoSerializer
from .serializers import PartySerializer
from .serializers import PartyPlayersSerializer
from .serializers import PartyChatSerializer

from .models import Juego
from .models import Party
from .models import PartyPlayers
from .models import PartyChat


class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all().order_by('nombre')
    serializer_class = JuegoSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('nombre')
    serializer_class = PartySerializer

class PartyPlayersViewSet(viewsets.ModelViewSet):
    queryset = PartyPlayers.objects.all().order_by('party')
    serializer_class = PartyPlayersSerializer

class PartyChatViewSet(viewsets.ModelViewSet):
    queryset =  PartyChat.objects.all().order_by('id')
    serializer_class = PartyChatSerializer
