# Generated by Django 3.0.5 on 2021-03-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_saveditems_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveditems',
            name='prev_prod_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]