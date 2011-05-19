from django.db import models

# Taula per guardar sa pagina base
class Pagina(models.Model):
    urlbase = models.URLField(verify_exists=True, max_length=500, unique=True)
    nom = models.CharField(max_length=500)

    def __unicode__(self):
        return self.urlbase

# Taula per guardar les noticies de cada pagina base
class Noticia(models.Model):
    titol = models.CharField(max_length=500)
    url = models.URLField(verify_exists=True, max_length=500, unique=True)
    pagina = models.ForeignKey('Pagina')

    def __unicode__(self):
        return self.titol
