# Generated by Django 5.2.1 on 2025-05-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
