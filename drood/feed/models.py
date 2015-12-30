from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def create(cls, name, url):
        """
        Add a new feed
        """
        feed = False

        # prevent duplicate feeds from being added
        try:
            feed = cls.objects.get(url=url)
        except:
            pass

        if not feed:
            feed = cls.objects.create(name=name, url=url)

        return feed
