# Generated by Django 4.1.7 on 2023-03-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_manager', '0005_assetportfolio_quantity_alter_assetportfolio_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetportfolio',
            name='quantity',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]
