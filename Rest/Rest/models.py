from django.db import models


class personDetails(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    github=models.URLField()


