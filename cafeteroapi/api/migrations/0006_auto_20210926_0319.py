# Generated by Django 3.2.7 on 2021-09-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210926_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='contact',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='batch',
            name='contact_name',
            field=models.TextField(default=''),
        ),
    ]
