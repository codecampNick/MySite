# Generated by Django 2.1 on 2019-04-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='experience_level',
            field=models.FloatField(default=0.0),
        ),
    ]
