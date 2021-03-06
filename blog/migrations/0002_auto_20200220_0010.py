# Generated by Django 3.0.3 on 2020-02-20 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.Post'),
        ),
    ]
