from django.db import models


# Create your models here.
from keygen.models import Key


class KeyUrlMap(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    url = models.TextField()
    is_active = models.BooleanField(default=True)
