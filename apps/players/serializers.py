from rest_framework import serializers

from apps.players.models import PlayerModel


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = (
            'id',
            'name',
            'number',
            'salary',
            'position',
            'updated_at',
            'created_at',
        )

    def validate_salary(self, salary):
        if salary <= 0:
            raise serializers.ValidationError('Salary must be greater than 0')
        return salary

    def validate(self, attrs):
        salary = attrs.get('salary')
        number = attrs.get('number')
        if salary is not None and number is not None and salary == number:
            raise serializers.ValidationError('Salary cannot be equal to kit number')
        return attrs