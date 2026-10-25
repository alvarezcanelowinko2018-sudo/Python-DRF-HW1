from django_filters import rest_framework as django_filters

from apps.players.models import PositionChoices, PlayerModel


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class PlayerFilter(django_filters.FilterSet):
    lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    range = django_filters.RangeFilter(field_name='number')
    salary_in = NumberInFilter(field_name='salary', lookup_expr='in')
    position = django_filters.ChoiceFilter(field_name='position', choices=PositionChoices.choices)
    order = django_filters.OrderingFilter(
        fields=(
            'id',
            'name',
            'salary',
            'number',
        )
    )

    class Meta:
        model = PlayerModel
        fields = ['salary', 'number', 'position']