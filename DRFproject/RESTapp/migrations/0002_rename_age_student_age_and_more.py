# Generated by Django 4.1.6 on 2023-12-11 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fatger_name',
            new_name='Father_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
    ]
