from django.db import models

class ManasFims(models.Model):
    title = models.CharField(max_length=300)
    time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
