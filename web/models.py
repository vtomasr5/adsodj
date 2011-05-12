from django.db import models

# Create your models here.

class Paginas(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)

    def __unicode__(self):
        return self.title

