# Generated by Django 5.1.1 on 2024-09-12 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_bookpost_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('doc', models.FileField(blank=True, null=True, upload_to='docs/')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(default='', max_length=300)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Normal'), (1, 'Reserved'), (2, 'Saved')], default=0)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
