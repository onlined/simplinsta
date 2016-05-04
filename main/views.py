import requests

from django.shortcuts import render
from django.conf import settings

from .models import Tag

def request_url(tag):
    return 'https://api.instagram.com/v1/tags/%s/media/recent?count=6&client_id=%s' % (tag, settings.INSTAGRAM_CLIENT_ID)

def show_tag(request, tag=settings.DEFAULT_TAG):
    recent_tags = Tag.objects.all()
    res = requests.get(request_url(tag))
    urls = [[],[]]
    try:
        data = res.json()
        for i,post in enumerate(data['data']):
            urls[i//3].append(post['images']['low_resolution']['url'])
    except:
        pass
    return render(request, 'main/show_tag.html', context={
        'tag': tag,
        'recent_tags': recent_tags,
        'urls': urls,
    })
    
def show_tag_prev(request):
    pass
    
def show_tag_next(request):
    pass
    
def find_tag(request):
    pass
