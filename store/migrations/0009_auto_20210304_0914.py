# Generated by Django 3.0.5 on 2021-03-04 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_saveditems_prev_prod_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SavedItems',
            new_name='SavedItem',
        ),
    ]
