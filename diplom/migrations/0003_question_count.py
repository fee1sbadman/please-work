# Generated by Django 2.2.1 on 2019-05-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0002_auto_20190523_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
