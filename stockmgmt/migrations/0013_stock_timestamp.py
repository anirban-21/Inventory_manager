# Generated by Django 3.1.1 on 2020-10-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0012_auto_20201001_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
