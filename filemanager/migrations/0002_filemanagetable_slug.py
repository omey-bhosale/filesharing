# Generated by Django 3.2 on 2021-04-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemanagetable',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=15),
        ),
    ]
