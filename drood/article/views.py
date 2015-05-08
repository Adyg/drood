from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

from article.models import Article
from feed.models import Feed


def list(request, feed_id=False):
    articles = None
    feed = None

    if feed_id:
        feed = get_object_or_404(Feed, pk=feed_id)
        articles = Article.objects.filter(feed=feed)

    if not articles:
        articles = Article.objects.all()

    paginator = Paginator(articles.order_by('-publication_date'), 20)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    print feed
    return render(request, 'list.html', {
        'articles': articles,
        'page': page,
        'paginator': paginator,
        'feed': feed,
    })
