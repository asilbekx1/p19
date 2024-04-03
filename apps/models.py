from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to='Friendship/%Y/%m')
