from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.players.filter import PlayerFilter
from apps.players.models import PlayerModel
from apps.players.serializers import PlayerSerializer


class PlayerListCreateView(ListCreateAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PlayerFilter
    ordering_fields = '__all__'
    ordering = ['id']


class PlayerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'put', 'delete']