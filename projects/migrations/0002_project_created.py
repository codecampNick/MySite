# Generated by Django 2.1 on 2019-04-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.BooleanField(default=False),
        ),
    ]
