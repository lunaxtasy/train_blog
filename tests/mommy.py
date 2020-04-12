"""
mommy.py --> I would prefer to call it mummy.py

Allows testing with RichTextUploadingField enabled
"""

from model_mommy import mommy, random_gen
from ckeditor_uploader.fields import RichTextUploadingField

class CustomMommy(mommy.Mommy):
    """
    Extends basic Mommy with custom fields mapped
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Implements CKEditor uploading field generator
        self.type_mapping[RichTextUploadingField] = random_gen.gen_text
