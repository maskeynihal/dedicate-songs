# Generated by Django 3.0.5 on 2020-04-10 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_published',
            new_name='date_created',
        ),
    ]
