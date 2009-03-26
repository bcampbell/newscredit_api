import solango, re
from crawler.models import Article

class ArticleDocument(solango.SearchDocument):
  date = solango.fields.DateField()
  title = solango.fields.CharField(copy=True)
  content = solango.fields.TextField(copy=True)
  author = solango.fields.CharField(copy=True)
  tags = solango.fields.CharField(copy=True, multi_valued=True)
  
  class Media:
    template = 'solango/document.html'

  def transform_date(self, instance):
    if instance.updated:
      return instance.updated
    else:
      return instance.published
      
  def transform_content(self, instance):
    r = re.compile(r'<.*?>') # strip html tags
    if instance.entry_content:
      return r.sub('', instance.entry_content)
    else:
      return r.sub('', instance.entry_summary)

  def transform_title(self, instance):
    if instance.entry_title:
      return instance.entry_title
    else:
      return instance.__unicode__()
  
  def transform_author(self, instance):
    """docstring for transform_author"""
    if len(instance.names.all()):
      return instance.names.all()[0].__unicode__()
    else:
      return ''

  def transform_tags(self, instance):
    """transform tags for solr"""
    return instance.tags.split(',')
  
  def get_model(self):
    """get model"""
    return Article.objects.get(id=self.fields['id'].value)
solango.register(Article, ArticleDocument)
