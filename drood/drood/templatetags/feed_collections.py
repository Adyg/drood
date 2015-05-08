from django import template

from feed.models import Feed


register = template.Library()


def feed_collections(active_feed=False):
    """
    Display the sidebar feed collection
    """
    feeds = Feed.objects.all()

    return {
        'feeds': feeds,
        'active_feed': active_feed,
    }


register.inclusion_tag('drood/_feed_collections.html')(feed_collections)
