from io import BytesIO
import pytest

from PIL import Image
from blog.models import Contest

pytestmark = pytest.mark.django_db

def test_valid_form_submission(client, settings, tmpdir):
    """
    Checks to make sure that the image upload and form submission is successful
    """
    # Set media root to a pytest temporary dir
    settings.MEDIA_ROOT = tmpdir
    # Create an image in memory and save to a file buffer
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    file = BytesIO()
    image.save(file, 'png')
    file.name = 'pytest.png'
    file.seek(0)

    data = {
        'first_name': 'Becky',
        'last_name': 'Doran',
        'email': 'rebecca.doran1@gmail.com',
        'photo': file
    }
    response = client.post('/contest/', data)
    assert response.status_code == 302
    assert response.url == '/'

def test_invalid_submission(client):
    """
    Checks that form detects an improper submission
    """
    data = {'fizz': 'buzz'}
    response = client.post('/contest/', data)
    assert response.status_code != 302
    assert Contest.objects.exists() is False
