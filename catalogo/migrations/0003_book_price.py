# Generated by Django 3.2.4 on 2021-07-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20210627_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
