# Generated by Django 3.0.1 on 2020-01-20 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0002_journal_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='key_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 20, 16, 19, 32, 773696, tzinfo=utc), null=True, verbose_name='Key in'),
        ),
    ]
