from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    """
    Rail Tales homepage first HTTP request attempt:

    return render(request, 'blog/home.html', {'message': 'Hello everyone!'})

    Now for second attempt below:
    """
    #Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    topical = models.Post.objects.get_topics()

    #Add context variable "latest_posts"
    context = {
        'topics' : topical,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
