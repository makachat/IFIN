# Generated by Django 2.1.4 on 2019-01-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0015_contract_noticeperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='comment',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
