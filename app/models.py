from django.db import models
from django.utils import timezone

class clients(models.Model):
    user = models.CharField(max_length=200)
    entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.user
