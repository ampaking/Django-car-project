# Generated by Django 3.2.4 on 2021-07-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='year'),
        ),
    ]
