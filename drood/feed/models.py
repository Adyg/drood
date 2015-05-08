from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.name
