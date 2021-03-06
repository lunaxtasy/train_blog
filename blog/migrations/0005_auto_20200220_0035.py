# Generated by Django 3.0.3 on 2020-02-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200220_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The time and date of actual publishing', unique_for_date='published'),
        ),
    ]
