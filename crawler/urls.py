from django.conf.urls.defaults import *
from django.views.generic.list_detail import *
from crawler.models import Article
from crawler.views import *

article_json = {
  'queryset' : Article.objects.all(),
  'template_name' : 'object_json.html',
}

urlpatterns = patterns('',
  (r'^(?P<object_id>.*).json$', object_detail, dict(article_json), "article-json"),
  (r'^bentest$', "crawler.views.ben_test" ),
)
