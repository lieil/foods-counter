# Generated by Django 4.2.7 on 2023-11-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('PC', 'Штука'), ('KG', 'Килограмм'), ('L', 'Литр')], default='PC', max_length=2),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
