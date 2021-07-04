# Generated by Django 3.2.4 on 2021-06-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=269)),
                ('last_name', models.CharField(max_length=269)),
                ('designation', models.CharField(max_length=269)),
                ('photo', models.ImageField(upload_to='photots/%Y/%m/%d')),
                ('facebook_link', models.CharField(max_length=270)),
                ('twitter_link', models.CharField(max_length=270)),
                ('istagram_link', models.CharField(max_length=270)),
                ('createed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]