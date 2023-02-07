from django.db import models

# Create your models here.
class Image(models.Model):
    idx = models.IntegerField
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title
