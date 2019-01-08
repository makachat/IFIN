# Generated by Django 2.1.4 on 2019-01-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0002_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('glaccount', models.DecimalField(decimal_places=0, max_digits=8)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]