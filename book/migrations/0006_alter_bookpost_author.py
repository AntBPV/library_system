# Generated by Django 5.1.1 on 2024-09-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_bookpost_author_bookpost_doc_alter_bookpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='author',
            field=models.CharField(default='', max_length=300),
        ),
    ]
