# Generated by Django 2.1.4 on 2019-01-03 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0017_auto_20190103_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='siteAffectation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='IFApp.Site'),
        ),
    ]
