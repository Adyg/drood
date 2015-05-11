# -*- coding: utf-8 -*-
import feedparser
import hashlib
import datetime
from time import mktime

from django.core.management.base import NoArgsCommand
from django.utils.html import strip_tags
from bs4 import BeautifulSoup

from feed.models import Feed
from article.models import Article, ArticleMedia
from drood.utils import _remove_attrs


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        IGNORED_MEDIA_HOSTS = ['feedburner.com', ]
        feeds = Feed.objects.all()

        for feed in feeds:
            articles = feedparser.parse(feed.url)['entries']

            for article in articles:

                article_hash = hashlib.md5(
                    article.description.encode('utf-8', 'ignore'))
                article_hash_digest = article_hash.hexdigest()

                already_added = Article.objects.filter(
                    control_hash=article_hash_digest)

                #normalize, normalize, normalize
                extracted_raw_summary = ''
                extracted_media = ''
                extracted_media_type = None

                #try to find the largest piece of content
                if hasattr(article, 'content'):
                    extracted_raw_summary = article.content[0].value
                elif hasattr(article, 'summary'):
                    extracted_raw_summary = article.summary

                #try to find an image/embed:
                if hasattr(article, 'media_content'):
                    extracted_media = article.media_content[0]['url']
                    extracted_media_type = 'image'

                #BeautifulSoup kicks in, to remove all inline styles
                soup = BeautifulSoup(extracted_raw_summary)
                clean_soup = _remove_attrs(soup)
                extracted_raw_summary = '%s' % clean_soup
                #if we do not yet have a media element for this article,
                #attempt to retrieve one using BS4
                if not extracted_media:
                    first_image = clean_soup.find('img')
                    if first_image:
                        try:
                            extracted_media = first_image['src']
                            extracted_media_type = 'image'
                        except:
                            pass

                if not already_added:
                    added_article = Article(
                        title=article.title,
                        summary=strip_tags(extracted_raw_summary.decode('utf-8', 'ignore')),
                        raw_summary=extracted_raw_summary,
                        link=article.link,
                        control_hash=article_hash_digest,
                        feed_id=feed.id,
                    )

                    if hasattr(article, 'author') and article.author:
                        added_article.author = article.author

                    if hasattr(article, 'published'):
                        try:
                            added_article.publication_date = datetime.datetime.fromtimestamp(mktime(article.published_parsed))
                        except:
                            pass

                    added_article.save()

                    if extracted_media:
                        valid = True
                        for ignored_domain in IGNORED_MEDIA_HOSTS:
                            if ignored_domain in extracted_media:
                                valid = False
                        if valid:                                
                            added_media = ArticleMedia(
                                article=added_article,
                                src=extracted_media
                            )

                        added_media.save()
