from django.db import models

# Create your models here.

class Pagina(models.Model):
    urlbase = models.URLField(verify_exists=True, max_length=500, unique=True)
    nom = models.CharField(max_length=500)

    def __unicode__(self):
        return self.urlbase

class Noticia(models.Model):
    titol = models.CharField(max_length=500)
    url = models.URLField(verify_exists=True, max_length=500, unique=True)
    pagina = models.ForeignKey('Pagina')

    def __unicode__(self):
        return self.titol
