# Generated by Django 4.1.6 on 2023-12-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RESTapp', '0004_rename_categoty_book_category_remove_book_book_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='Categoty',
        ),
        migrations.AddField(
            model_name='book',
            name='book_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
