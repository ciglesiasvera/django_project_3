from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000)
        ]
    )

    def __str__(self):
        return self.title
