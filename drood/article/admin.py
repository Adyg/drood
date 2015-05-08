from django.contrib import admin

from .models import Article, ArticleMedia

admin.site.register(Article)
admin.site.register(ArticleMedia)
