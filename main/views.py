import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Tag
from .forms import TagForm

def request_url(tag, max_tag_id = ''):
    if max_tag_id != '':
        max_tag_id = '&max_tag_id=' + max_tag_id
    return 'https://api.instagram.com/v1/tags/%s/media/recent?count=6&client_id=%s%s' % (tag, settings.INSTAGRAM_CLIENT_ID, max_tag_id)

def show_tag(request, tag=settings.DEFAULT_TAG):
    recent_tags = Tag.objects.order_by('-time')[:20]
    res = requests.get(request_url(tag,request.session.pop('max_tag_id','') if request.resolver_match.url_name == 'show_tag_next' else ''))
    urls = [[],[]]
    try:
        data = res.json()
        request.session['max_tag_id'] = data['pagination']['next_max_tag_id']
        for i,post in enumerate(data['data']):
            urls[i//3].append(post['images']['low_resolution']['url'])
    except:
        pass
    if request.method == 'GET':
        form = TagForm()
    elif request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            try:
                obj = Tag.objects.get(name=form.cleaned_data['name'])
            except:
                obj = form.save(commit=False)
            obj.time = timezone.now()
            obj.save()
            return redirect(reverse('show_tag',args=[obj.name]))
    return render(request, 'main/show_tag.html', context={
        'tag': tag,
        'form': form,
        'recent_tags': recent_tags,
        'urls': urls,
    })
    
def show_tag_prev(request, tag):
    pass
