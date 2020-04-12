import pytest

from blog.models import Contact

pytestmark = pytest.mark.django_db

def test_post_contact_form_redirect(client):
    """
    Checks that successful data entry returns to main homepage
    """
    data = {
        'first_name': 'Becky',
        'last_name': 'Doran',
        'email': 'rebecca.doran1@gmail.com',
        'message': 'Test message'
    }
    response = client.post('/contact/', data)
    assert response.status_code == 302
    assert response.url == '/' #main homepage

def test_post_contact_form_saves_data(client):
    """
    Checks that form is actually saving entered data
    """
    data = {
        'first_name': 'Becky',
        'last_name': 'Doran',
        'email': 'rebecca.doran1@gmail.com',
        'message': 'Test message'
    }
    client.post('/contact/', data)

    #One object in database only!
    obj = Contact.objects.get()
    assert obj.first_name == data['first_name']
    assert obj.last_name == data['last_name']
    assert obj.email == data['email']
    assert obj.message == data['message']

def test_invalid_submission(client):
    """
    Checks that form detects an improper submission
    """
    data = {'fizz': 'buzz'}
    response = client.post('/contact/', data)
    assert response.status_code != 302
    assert Contact.objects.exists() is False
