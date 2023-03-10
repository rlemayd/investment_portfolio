# Generated by Django 4.1.7 on 2023-03-04 21:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_manager', '0007_alter_assetportfolio_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='value_balance',
            field=models.DecimalField(decimal_places=2, default=1000000000, max_digits=20),
        ),
        migrations.CreateModel(
            name='PortfolioDailyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_manager.portfolio')),
            ],
        ),
    ]
