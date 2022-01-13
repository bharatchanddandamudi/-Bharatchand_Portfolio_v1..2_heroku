# Generated by Django 4.0 on 2021-12-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/jobs/')),
                ('title', models.CharField(max_length=200, null=True)),
                ('summary', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/projects/')),
                ('title', models.CharField(max_length=200, null=True)),
                ('summary', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]