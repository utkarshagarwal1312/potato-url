from django.db import models


# Create your models here.
class Key(models.Model):
    val = models.CharField(max_length=10)
    is_used = models.BooleanField(default=False)
