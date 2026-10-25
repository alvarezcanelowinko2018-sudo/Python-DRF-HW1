from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.players.filter import PlayerFilter
from apps.players.models import PlayerModel
from apps.players.serializers import PlayerSerializer


class PlayerListCreateView(ListCreateAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlayerFilter


class PlayerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'put', 'delete']