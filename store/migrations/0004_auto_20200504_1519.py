# Generated by Django 2.2.7 on 2020-05-04 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200504_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='addess',
            new_name='address',
        ),
    ]
