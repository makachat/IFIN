# Generated by Django 2.1.4 on 2019-01-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0011_auto_20190103_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
