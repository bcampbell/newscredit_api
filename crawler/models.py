# vim:set ts=2 sts=2 sw=2 expandtab:
from django.db import models
from django.contrib import admin, databrowse
from locallibs.aump import hall, hatom
from tagging.fields import TagField
from tagging.models import Tag, TaggedItem
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from urlparse import urlparse
#from BeautifulSoup import BeautifulSoup
import pprint, urllib2, re, os, time, simplejson
import html5lib

#browse tags

# Create your models here.
class CrawlSite(models.Model):
  """site from which we are crawling"""
  url = models.URLField("Site URL", unique=True)
  name = models.TextField("Site Name", null=True, blank=True)
  def __unicode__(self):
    """string rep"""
    return self.url
  def save(self):
    """overridden save"""
    super(CrawlSite, self).save()
    if len(self.feed_pages.all()) < 1:
      feedpage = self.feed_pages.model()
      feedpage.url = self.url
      self.feed_pages.add(feedpage)
  def crawl(self):
    #if we have no feed pages, add the actual url of the site itself
    if len(self.feed_pages.all()) < 1:
      feedpage = self.feed_pages.model()
      feedpage.url = self.url
      self.feed_pages.add(feedpage)
      feedpage.fetch()
      return True
    else:
      results=[]
      for page in self.feed_pages.all():
        results.append(page.fetch())
      return True

class FeedPageManager(models.Manager):
  """manager for feed pages"""
  def get_due_pages(self):
    """get pages due for refresh"""
    return self.exclude(refresh_at__gt=datetime.now())

class FeedPage(models.Model):
  """pages which are either atom feeds or hatom pages"""
  url = models.URLField("Feed URL", db_index=True)
  crawl_site = models.ForeignKey(CrawlSite, related_name='feed_pages')
  updated_at = models.DateTimeField(null=True, blank=True)
  refresh_minutes = models.IntegerField(help_text="How many minutes to wait before refreshing this page", default=120)
  refresh_at = models.DateTimeField(null=True, blank=True)
  objects = FeedPageManager()
  crawled = [] # what pages have been crawled in this instance
  def __unicode__(self):
    """string rep"""
    return self.url
  def fetch(self, url=None, follow_next=False):
    """fetch feed and parse it"""
    if not url:
      url = self.url
    print url
    if url in self.crawled:
      return False # Already crawled
    self.crawled.append(url)
    self.updated_at = datetime.now()
    self.refresh_at = datetime.now() + timedelta(minutes=self.refresh_minutes)
    self.save()
    html = urllib2.urlopen(url).read()
    parser = hatom.MicroformatHAtom()
    htmlparser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("dom"))
    dom = htmlparser.parse(html)
    parser.Feed(dom)
    results = [result for result in parser.Iterate()]          
    # create articles and/or revision from results
    for result in results:
      if result.get('bookmark'):
        if re.match('http://', result.get('bookmark')):
          bookmark = result.get('bookmark')
        elif re.match('/', result.get('bookmark')):
          bookmark = 'http://' + urlparse(url).netloc + result.get('bookmark')
        else:
          bookmark = url + result.get('bookmark')
      else:
        bookmark = url
      if bookmark != url and bookmark not in self.crawled:
        try:
          self.fetch(url=bookmark) # fetch the actual version, not the summarised one
        except Exception, e:
          pass
      else:
        article, created = Article.objects.get_or_create(bookmark=bookmark)
        article.from_hatom_parsed(result)
        article.save()
    if follow_next and len(results) > 0:
      # follow next links to find more articles and spider entire sites -
      # do this even if they're outside the hfeed element, for the moment (we may want to change this)
      # clear some stuff we don't need anymore
      del results, parser, html
      # find next links
      for element in dom.getElementsByTagName('a'):
        if element.getAttribute('rel').lower() == 'next':
          try:
            time.sleep(3) # let's not go nuts here
            next = element.getAttribute('href')
            if not re.match('http://', next):
              if re.match('/', next):
                next = 'http://' + urlparse(url).netloc + next
              else:
                next = url + next
            self.fetch(url=next, follow_next=True)            
          except Exception, e:
            pass
    return True

class Article(models.Model):
  """article"""
  bookmark = models.URLField("Article permalink", unique=True)
  entry_title = models.TextField("Title", null=True, blank=True)
  entry_content = models.TextField("Content", null=True, blank=True)
  entry_summary = models.TextField("Summary", null=True, blank=True)
  updated = models.DateTimeField("Last Updated", null=True, blank=True, db_index=True)
  published = models.DateTimeField("First Published", null=True, blank=True, db_index=True)
  feedpages = models.ManyToManyField(FeedPage, through='FeedPageArticle')
  tags = TagField()
  tag_models = generic.GenericRelation(TaggedItem)
  def __unicode__(self):
    """string rep"""
    if self.entry_title:
      return self.entry_title
    else:
      return self.bookmark
  
  def get_absolute_url(self):
    """get url"""
    return self.bookmark
  
  def analysis_text(self):
    """provide text for analysis"""
    return self.entry_title + ' ' + self.entry_content
  
  def analyze(self):
    """add semantic entities"""
    from entify.models import analyze as entify_analyze
    results = entify_analyze(self)
    return results
    
  def from_hatom_parsed(self, result):
    """from a hatom parsed item"""
    self.entry_title = result.get('entry-title', '')
    self.entry_content = result.get('entry-content', '')
    self.entry_summary = result.get('entry-summary', '')
    if result.has_key('tag'):
      self.tags = reduce(lambda x, y: x + ',' + y, [tag.get('name') for tag in result.get('tag')]).lower()
    if result.get('author') and len(result.get('author')) > 0:
      for parsedauthor in result.get('author'):
        try:
          if parsedauthor.get('url'):
            author, created = Author.objects.get_or_create(url=parsedauthor.get('url'))
            author.link_to_article_from_hcard(self,parsedauthor)
            author.save()
          else:
            name, created = Name.objects.get_or_create(fn=parsedauthor.get('fn'))
            name.articles.add(self)
            name.save()          
        except Exception, e:
          pass # fail bad authors silently - (be conservative in what you send, and liberal in what you accept)
    try:
      self.published = datetime.strptime(result.get('published'), "%Y-%m-%dT%H:%M:%SZ")
    except Exception, e:
      self.published = datetime.now()
    try:
      self.updated = datetime.strptime(result.get('updated'), "%Y-%m-%dT%H:%M:%SZ")
    except Exception, e:
      # TODO : some better logic here, that checks if the article has been updated
      self.updated = datetime.now()
    return True
  
  def as_json(self):
    """json representation"""
    show = {
      'bookmark' : self.bookmark,
      'entry-title' : self.entry_title,
      'entry-summary' : self.entry_summary,
      'entry-content' : self.entry_content,
      'updated' : self.updated.ctime(),
      'published' : self.published.ctime(),
      'tags' : self.tags,
    }
    return(simplejson.dumps(show))

class ArticleEntity(models.Model):
  """relationship between Articles and Entities"""
  article = models.ForeignKey(Article)
  content_type = models.ForeignKey(ContentType)
  entity_id = models.PositiveIntegerField()
  entity = generic.GenericForeignKey('content_type', 'entity_id')

class FeedPageArticle(models.Model):
  """relationship between Article and FeedPage"""
  feedpage = models.ForeignKey(FeedPage)
  article = models.ForeignKey(Article)
  def __unicode__(self):
    """string rep"""
    return "%s : %s" % (self.feedpage, self.article)

class Author(models.Model):
  """article author"""
  url = models.URLField("Author page", unique=True)
  articles = models.ManyToManyField(Article, related_name='authors', through='WorkedOn')
  def __unicode__(self):
    """string rep"""
    return self.url
  def link_to_article_from_hcard(self, article, hcard):
    """from a hcard parsed item"""
    worked_on, created = WorkedOn.objects.get_or_create(author=self, article=article)
    worked_on.role = hcard.get('role', 'author') #default to author if no role provided
    worked_on.save()
    name, created = Name.objects.get_or_create(fn=hcard.get('fn'))
    name.articles.add(article)
    name.save()
    author_name, created = AuthorName.objects.get_or_create(name=name, author=self)
    author_name.author = self
    author_name.name = name
    author_name.articles.add(article)
    author_name.save()

class Name(models.Model):
  """names for people"""
  fn = models.TextField("formatted name")
  authors = models.ManyToManyField(Author, related_name='names', through='AuthorName')
  articles = models.ManyToManyField(Article, related_name='names')
  def __unicode__(self):
    """string rep"""
    if self.fn:
      return self.fn
    else:
      return 'author id ' + self.id.__str__()
  
class AuthorName(models.Model):
  """author url to name relationship"""
  author = models.ForeignKey(Author, db_index=True, blank=True, null=True, related_name='authornames')
  name = models.ForeignKey(Name, db_index=True, blank=True, null=True, related_name='authornames')
  # articles and count links so we can keep a count of the popular names for a user to create canonical
  articles = models.ManyToManyField(Article, blank=True, null=True)
  def __unicode__(self):
    """string rep"""
    return "%s" % (self.name)

class WorkedOn(models.Model):
  """relationship between articles and authors"""
  author = models.ForeignKey(Author, db_index=True)
  article = models.ForeignKey(Article, db_index=True)
  role = models.CharField(null=True, blank=True, db_index=True, max_length=255)
  class Meta:
    verbose_name = 'worked on (article <-> author)'
    verbose_name_plural = 'worked on (article <-> author)'
  def __unicode__(self):
    """string rep"""
    return "%s : %s" % (self.author, self.article)

class Principles(models.Model):
  """principles"""
  url = models.URLField(unique=True)
  articles = models.ManyToManyField(Article, related_name='principles')
  class Meta:
    verbose_name_plural = 'Principles'
  def __unicode__(self):
    """string rep"""
    return self.url
  
class Revision(models.Model):
  """revision of article"""
  article = models.ForeignKey("Article")
  source = models.URLField("Revision source URL")
  entry_title = models.TextField("Title")
  entry_content = models.TextField("Content", null=True, blank=True)
  entry_summary = models.TextField("Summary")




def scrape_article_page( url ):
  """ scrape a page for a single article. Returns list of Article objects or None """

  # TODO: get rid of this, refactor FeedPage.fetch instead

  articles = []

  html = urllib2.urlopen(url).read()
  parser = hatom.MicroformatHAtom()
  htmlparser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("dom"))
  dom = htmlparser.parse(html)
  parser.Feed(dom)
  results = [result for result in parser.Iterate()]
  # create articles and/or revision from results
  for result in results:
    if result.get('bookmark'):
      if re.match('http://', result.get('bookmark')):
        bookmark = result.get('bookmark')
      elif re.match('/', result.get('bookmark')):
        bookmark = 'http://' + urlparse(url).netloc + result.get('bookmark')
      else:
        bookmark = url + result.get('bookmark')
    else:
      bookmark = url
    article, created = Article.objects.get_or_create(bookmark=bookmark)
    article.from_hatom_parsed(result)
    article.save()
    articles.append( article )

  return articles



try:
  databrowse.site.register(Tag)
  admin.site.register(CrawlSite)
  databrowse.site.register(CrawlSite)
  admin.site.register(FeedPage)
  databrowse.site.register(FeedPage)
  admin.site.register(Article)
  databrowse.site.register(Article)
  admin.site.register(Author)
  databrowse.site.register(Author)
  admin.site.register(Name)
  databrowse.site.register(Name)
  admin.site.register(Principles)
  databrowse.site.register(Principles)
  admin.site.register(Revision)
except Exception, e:
  pass
