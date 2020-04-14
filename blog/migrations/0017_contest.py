# Generated by Django 3.0.3 on 2020-04-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200412_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.TextField()),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted'],
            },
        ),
    ]
