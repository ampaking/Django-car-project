# Generated by Django 3.2.4 on 2021-08-07 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contact_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 7, 6, 47, 38, 29828)),
        ),
    ]