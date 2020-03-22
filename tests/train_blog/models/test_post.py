from model_mommy import mommy
from django.db.models import Count
import datetime as dt
import pytest

from blog.models import Post, Comment, Topic

pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_those_with_published_status():
    """
    From module notes, returns posts with published status only
    """
    published = mommy.make('blog.Post', status=Post.PUBLISHED)
    mommy.make('blog.Post', status=Post.DRAFT)

    expected = [published]
    result = list(Post.objects.published())

    assert result == expected

def test_publish_sets_status_to_published():
    """
    From module notes, sets post status to publish
    """
    post = mommy.make('blog.Post', status=Post.DRAFT)
    post.publish()

    assert post.status == Post.PUBLISHED

def test_get_authors_return_users_who_have_authored_posts(django_user_model):
    """
    From module notes, returns authors with posts only
    """
    author = mommy.make(django_user_model)
    mommy.make('blog.Post', author=author)
    mommy.make(django_user_model)

    assert list(Post.objects.get_authors()) == [author]

def test_get_authors_return_unique_users(django_user_model):
    """
    From module notes, returns unique authors with posts only
    """
    author = mommy.make(django_user_model)
    mommy.make('blog.Post', author=author, _quantity=3)

    assert list(Post.objects.get_authors()) == [author]

def test_get_topics_return_list_of_topics():
    """
    Returns list of topics
    """
    topics = mommy.make('blog.Topic', name='topic')
    mommy.make('blog.Post')

    assert list(Post.objects.get_topics()) == [topics]

def test_get_topics_count_topics():
    """
    Returns a count of how many posts for a topic
    """
    topics = mommy.make('blog.Topic', name='topic')
    mommy.make('blog.Post', _quantity=2)

    top_count = Post.objects.get_topics('topic_count')

    assert top_count == [topics.topic_count]

def test_post_list_only_returns_published_articles(client):
    published = mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
        title='Published post'
    )
    mommy.make(
        'blog.Post',
        status=Post.DRAFT,
        title='Draft post'
    )

    response = client.get('/posts/')
    #Get the posts object_list
    result = response.context.get('posts')

    assert list(result) == [published]

def test_get_absolute_url_post_published_date():
    """
    Checks date and slug in URL
    """
    post = mommy.make(
        'blog.Post',
        published=dt.datetime(2014, 12, 20, tzinfo=dt.timezone.utc),
        slug='model-instances',
    )

    assert post.get_absolute_url() == '/posts/2014/12/20/model-instances/'

def test_get_absolute_url_no_publish_date_slug():
    """
    Checks URL without date or slug
    """
    post = mommy.make(
        'blog.Post',
        published=None,
    )

    assert post.get_absolute_url() == f'/posts/{post.pk}/'
