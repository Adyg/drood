from django.db import models
from django.utils import timezone

from feed.models import Feed


class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=240, blank=False, null=False)
    author = models.CharField(max_length=240, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    raw_summary = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    control_hash = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    def thumbnail(self):
        media = ArticleMedia.objects.filter(article=self)

        if media:
            return media[0]

        return False


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article)
    embed_code = models.TextField(blank=True, null=True)
    src = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.article.title
