#tests\blog\views\test_topic_detail.py

import pytest

from model_mommy import mommy
from blog.models import Topic

pytestmark = pytest.mark.django_db

def test_topic_detail_view_access_by_slug(client):
    mommy.make('blog.Topic', slug='hello')

    response = client.get('/topics/hello/')
    assert response.status_code == 200

def test_topic_detail_slug_spelling(client):
    mommy.make('blog.Topic', slug='hello')
    mommy.make('blog.Topic', slug='he1lo')

    response = client.get('/topics/hello/')
    assert response.status_code ==200
