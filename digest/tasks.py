from djnago.db import transaction
from celery.task import task
from .models import Resource
import feedparser
import dateutil.parser

@task
def update_rss():
    for rec in Resource.objects.all():
        try:
            data = feedparser.parse(rec.link)
            print ('INFORMATION!!! INFORMATION!!!', data.feed['updated'])
            print  iso_to_date(data.feed['updated'])
            #with transaction.commit_on_success():
            for item in data.entries:
                print item.title #link
                #entry = Resource(title=item.title)
                #entry.save()
        except Exception as e:
            print ('sync failed: %s' % e)

def iso_to_date(date_feed):
    if not date_feed:
        return None
    return dateutil.parser.parse(date_feed)
