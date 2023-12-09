from django.db import models

from musician.models import Musician

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=30, verbose_name='Album Name')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    released = models.DateField(verbose_name='Album Release Date')
    rating = models.DecimalField(
        decimal_places=2, max_digits=3, verbose_name='Rating')

    def __str__(self) -> str:
        return self.name + ' by ' + self.musician.firstName
