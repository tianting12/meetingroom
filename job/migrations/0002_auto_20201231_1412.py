# Generated by Django 3.1.4 on 2020-12-31 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
