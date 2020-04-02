from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
"""

"""

class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'

    def get_queryset(self):
        #Get base queryset
        queryset = super().get_queryset()

        #For 'pk' look-up, uses default queryset
        if 'pk' in self.kwargs:
            return queryset
        #Filters published date for everything else
        return queryset.published().filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicDetailView(DetailView):
    model = models.Topic
    context_object_name = 'top_topic'

    def get_context_data(self, **kwargs):
        topic_list = super(TopicDetailView, self).get_context_data(**kwargs)
        topic_list['options'] = models.Post.objects.filter(topics=self.get_object())
        return topic_list

    """def get_queryset(self):
        #Get base queryset
        queryset = super().get_queryset()

        #For 'pk' look-up, uses default queryset
        if 'pk' in self.kwargs:
            return queryset
        #Filters published date for everything else
        return queryset.published().filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )"""

class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        context.update({'latest_posts' : latest_posts})

        return context

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')[:10]

class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'top_topics'
    queryset = models.Topic.objects.all().order_by('name')

def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')

"""
Original code:

ContentMixin (superseded by context processor):

class ContextMixin:

    #Populates topic and authors variables

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = models.Post.objects.published()
            .get_authors()
            .order_by('first_name')
        context['topics'] = models.Post.objects.published()
            .get_topics()
        return context

get_context_data (superseded by ContentMixin)

    def get_context_data(self, **kwargs):
        #Get context from parent class
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published()
            .order_by('-published')[:3]

        authors = models.Post.objects.published()
            .get_authors()
            .order_by('first_name')

        topics = models.Post.objects.published()
            .get_topics()

        Class-based view example:
        #Defone "authors" context variable
        context['authors'] = models.Post.objects.published()
            .get_authors()
            .order_by('first_name')
        return context


        #Update context with context variables
        context.update({
            'authors': authors,
            'topics': topics,
            'latest_posts': latest_posts,
        })

        return context
        # render(request, 'blog/about.html')

class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        #Get context from parent class
        context = super().get_context_data(**kwargs)

        authors = models.Post.objects.published()
            .get_authors()
            .order_by('first_name')

        topics = models.Post.objects.published()
            .get_topics()

        Class-based view example:
        #Defone "authors" context variable
        context['authors'] = models.Post.objects.published()
            .get_authors()
            .order_by('first_name')
        return context

        return context

Original Home view

def home(request):

    Rail Tales homepage first HTTP request attempt:

    return render(request, 'blog/home.html', {'message': 'Hello everyone!'})

    Now for second attempt below:

    #Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    authors = models.Post.objects.get_authors()
    #Get list of topics
    topics = models.Post.objects.get_topics()

    #Add context variable "latest_posts"
    context = {
        'authors': authors,
        'topics' : topics,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
"""
