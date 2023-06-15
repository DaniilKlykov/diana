from django.db import models


class Risunki(models.Model):
    class Meta:
        db_table = 'risunki'

    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, null=True)
    canvas = models.CharField(max_length=20)
    paints = models.CharField(max_length=30)
    size = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}, {self.author}'
