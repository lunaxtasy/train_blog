#blog/context_processors.py

"""
Returns context data for common items carried across all pages
"""

from . import models

def base_context(request):
    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')
    topics = models.Post.objects.published() \
        .get_topics()
    return {'authors': authors, 'topics': topics}
