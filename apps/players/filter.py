from django_filters import rest_framework as django_filters

from apps.players.models import PlayerModel


class PlayerFilter(django_filters.FilterSet):
    class Meta:
        model = PlayerModel
        fields = {
            'salary': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'number': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'name': [
                'exact',
                'contains',
                'icontains',
                'startswith',
                'istartswith',
                'endswith',
                'iendswith',
            ],
            'position': ['exact'],
        }