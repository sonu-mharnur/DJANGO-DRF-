# Generated by Django 4.1.6 on 2023-12-12 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTapp', '0003_categoty_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Categoty',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_title',
        ),
    ]
