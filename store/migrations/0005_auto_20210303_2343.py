# Generated by Django 3.1.7 on 2021-03-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210303_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedItems',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.CharField(max_length=100)),
                ('item_status', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_saved',
            field=models.BooleanField(default=False),
        ),
    ]
