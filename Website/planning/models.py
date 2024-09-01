from django.db import models


def is_valid_day(value):
    '''
    0 -> Monday
    1 -> Tuesday
    2 -> Wednesday
    3 -> Thursday
    4 -> Friday
    5 -> Saturday
    6 -> Sunday
    '''
    return 0 <= value <= 6


def is_valid_date(value):
    '''
    0 -> 00-01
    1 -> 01-02
    2 -> 02-03
    3 -> 03-04
    4 -> 04-05
    ...
    23 -> 23-00
    '''
    return 0 <= value <= 23


class Planning(models.Model):
    entry = models.CharField(default='', max_length=50)
    day = models.IntegerField(default=-1, validators=[is_valid_day])
    start = models.IntegerField(default=-1, validators=[is_valid_date])
    end = models.IntegerField(default=-1, validators=[is_valid_date])
    disc = models.CharField(default='', max_length=200)
