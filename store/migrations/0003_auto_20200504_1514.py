# Generated by Django 2.2.7 on 2020-05-04 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200504_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='nmae',
            new_name='name',
        ),
    ]
