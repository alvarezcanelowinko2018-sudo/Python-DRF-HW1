from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel


class PositionChoices(models.TextChoices):
    GOALKEEPER = 'Goalkeeper'
    DEFENDER = 'Defender'
    MIDFIELDER = 'Midfielder'
    FORWARD = 'Forward'


class PlayerModel(BaseModel):
    class Meta:
        db_table = 'players'

    name = models.CharField(
        max_length=20,
        validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)]
    )
    number = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(99)])
    salary = models.FloatField()
    position = models.CharField(max_length=100, choices=PositionChoices.choices)