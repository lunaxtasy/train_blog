# Generated by Django 3.0.3 on 2020-04-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_contest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='photo',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
