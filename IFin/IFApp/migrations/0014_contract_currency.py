# Generated by Django 2.1.4 on 2019-01-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0013_auto_20190103_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='currency',
            field=models.CharField(choices=[('CAD', 'CAD'), ('USD', 'USD')], default='CAD', max_length=10),
            preserve_default=False,
        ),
    ]
