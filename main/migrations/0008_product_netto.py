# Generated by Django 4.2.7 on 2023-11-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productgroup_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='netto',
            field=models.FloatField(default=0),
        ),
    ]
