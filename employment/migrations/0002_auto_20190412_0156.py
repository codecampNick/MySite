# Generated by Django 2.1 on 2019-04-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
