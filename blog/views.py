from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from . import forms, models

# Create your views here.

class PostDetailView(DetailView):
    """
    Allows getting access to post details from the database
    """
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
    """
    Allows getting access to topic details from the database
    """
    model = models.Topic
    context_object_name = 'top_topic'

    #get access to the topic data with the M2M key
    def get_object(self, queryset=None):
        obj = super(TopicDetailView, self).get_object(queryset=queryset)
        return obj

class ContactFormView(CreateView):
    """
    Creates a form for entering in contact information to submit
    """
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        """
        Contact form validation
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)

class ContestFormView(CreateView):
    """
    Creates a form for entering in contest information and uploading an image
    to submit
    """
    form_class = forms.PhotoForm
    template_name = 'blog/contest_form.html'
    model = models.Contest
    success_url = reverse_lazy('home')

    """
    Entry form validation
    """
    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for entering! Good Luck!'
        )
        return super().form_valid(form)

class HomeView(TemplateView):
    """
    Provides templates, querysets and context for the main Homepage template
    """
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        context.update({'latest_posts' : latest_posts})

        return context

class AboutView(TemplateView):
    """
    Provides templates for the About page
    """
    template_name = 'blog/about.html'

class PostListView(ListView):
    """
    Provides context and querysets for the PostList
    """
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')[:10]

class TopicListView(ListView):
    """
    Provides context and querysets for the TopicList
    """
    model = models.Topic
    context_object_name = 'top_topics'
    queryset = models.Topic.objects.all().order_by('name')

def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')
