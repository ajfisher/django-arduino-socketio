from django.db import models

class LightUser(models.Model):
    
    name = models.CharField(max_length=20)
    session = models.CharField(max_length=20)

    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name
