# Generated by Django 2.1 on 2019-04-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(default='Need Short Description', max_length=255),
        ),
    ]
