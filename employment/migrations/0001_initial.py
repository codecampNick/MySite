# Generated by Django 2.1 on 2019-04-12 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=100)),
                ('company_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Responsibilites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=255)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employment.Company')),
            ],
        ),
        migrations.AddField(
            model_name='accomplishments',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employment.Company'),
        ),
    ]
