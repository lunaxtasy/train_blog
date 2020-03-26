# tests/blog/views/test_topic_list.py

import pytest
from model_mommy import mommy
from blog.models import Post, Comment, Topic

pytestmark = pytest.mark.django_db

def test_topic_list_url_returns_200(client):
    """
    Checks that topics page url can be found
    """
    response = client.get('/topics/')
    assert response.status_code

def test_topic_list_published_only(client):
    """
    Checks that only topics from published posts is being used
    """
    topics = mommy.make('blog.Topic', name='topic')
    published = mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
    )
    draft = mommy.make(
        'blog.Post',
        status=Post.DRAFT,
    )

    response = client.get('/topics/')
    result = response.context.get('top_topics')

    assert list(result) == [topics]
