# Generated by Django 3.1.4 on 2020-12-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20201231_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='修改日期'),
        ),
    ]