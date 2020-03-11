"""
test_views.py

Test program for checking views.py
"""
import pytest

@pytest.mark.django_db
def test_index_ok(client):
    """
    checks that HTTP response for the index view is 200
    """
    response = client.get('/')
    assert response.status_code == 200
