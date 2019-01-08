# Generated by Django 2.1.4 on 2019-01-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0006_site_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.CharField(blank=True, choices=[('Plant', 'Plant'), ('DataCenter', 'Data Center'), ('Yard', 'Yard'), ('DistributionCenter', 'Distribution Center'), ('HeadOffice', 'Head Office')], max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='country',
            field=models.CharField(blank=True, choices=[('CA', 'CANADA'), ('US', 'USA')], max_length=10),
        ),
    ]
