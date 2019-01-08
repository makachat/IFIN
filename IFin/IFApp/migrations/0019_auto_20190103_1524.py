# Generated by Django 2.1.4 on 2019-01-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFApp', '0018_contract_siteaffectation'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='typeOfExpense',
            field=models.CharField(choices=[('Capex', 'Capex'), ('Opex', 'Opex')], default='Opex', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='entity',
            field=models.CharField(choices=[('SJ-INC', 'Stella-Jones INC'), ('MCHI', 'MacFarland'), ('SJ-CORP', 'Stella-Jones Corporate')], max_length=10),
        ),
    ]