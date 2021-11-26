from django.db import models


class HabitModel(models.Model):
    FREQUENCY_CHOICES = (
        ('month', '1ヶ月'),
        ('week', '1週間'),
        ('day', '1日'),
    )
    TIME_UNIT_CHOICES = (
        ('hour', '時間'),
        ('minutes', '分'),
    )
    GOOD_OR_BAD_CHOICES = (
        ('good', '良い習慣'),
        ('bad', '悪い習慣'),
        ('normal', '日常習慣'),
    )
    username = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    habit = models.CharField(
        max_length=100,
    )
    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        null=True,
        blank=True,
    )
    time_value = models.IntegerField(
        null=True,
        blank=True,
    )
    time_unit = models.CharField(
        max_length=10,
        choices=TIME_UNIT_CHOICES,
        null=True,
        blank=True,
    )
    good_or_bad = models.CharField(
        max_length=10,
        choices=GOOD_OR_BAD_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username + ' : ' + self.habit
