# Generated by Django 3.1.3 on 2021-01-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210129_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='cover',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
