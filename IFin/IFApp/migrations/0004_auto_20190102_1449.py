# Generated by Django 2.1.4 on 2019-01-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0003_glaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glaccount',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]