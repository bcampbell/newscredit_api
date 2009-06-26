# vim:set ts=2 sts=2 sw=2 expandtab:
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
#from twitfave.locallib.decorators.json import json_callback
import urllib2
import html5lib
from locallibs.aump import hall, hatom
from models import Article,scrape_article_page

def json_object(request, queryset, object_id=None, slug=None, slug_field='slug'):
  """docstring for json_object"""
  model = queryset.model
  if object_id:
      queryset = queryset.filter(pk=object_id)
  elif slug and slug_field:
      queryset = queryset.filter(**{slug_field: slug})
  else:
      raise AttributeError, "Generic detail view must be called with either an object_id or a slug/slug_field."
  try:
      data = serializers.serialize('json', queryset)
  except ObjectDoesNotExist:
      raise Http404, "No %s found matching the query" % (model._meta.verbose_name)
  return HttpResponse(data, mimetype='application/json')



def render_article( art ):
  out = u"<pre>\n"

  out += u"bookmark: %s\n" %(art.bookmark)
  out += u"title: %s\n" %(art.entry_title)

  out = out + u"by:\n"

  for author in art.authors.all():
    out = out + "  " + unicode( author ) + "\n";

  out = out + u"</pre>\n";
  return out



def ben_test(request):
  if not 'HTTP_REFERER' in request.META:
    return HttpResponse( '' )

  url = request.META['HTTP_REFERER']

  # is article already in DB?
  art = None
  try:
    art = Article.objects.get( bookmark=url )
  except Article.DoesNotExist:
    arts = scrape_article_page( url )
    if len(arts) > 0:
      # Could be multiple articles on the page... ignore all but the first one
      art = arts[0]

  if art is not None:
    out = render_article( art )
  else:
    out = u"<pre>None</pre>\n";

  return HttpResponse(out)


