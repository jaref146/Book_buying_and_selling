# Generated by Django 3.2.9 on 2021-12-02 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_auto_20211202_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_book',
            name='store_post_book_price',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='sale_book',
            name='store_post_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 19, 44, 12, 799763)),
        ),
    ]