# Generated by Django 2.1 on 2019-02-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirects', '0002_auto_20190220_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redirect',
            old_name='url',
            new_name='target',
        ),
    ]
