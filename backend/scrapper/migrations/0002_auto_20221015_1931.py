# Generated by Django 2.2.13 on 2022-10-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptodata',
            name='current_top_10',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cryptodata',
            name='price',
            field=models.FloatField(),
        ),
    ]
