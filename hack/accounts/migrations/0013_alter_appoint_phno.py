# Generated by Django 4.0 on 2023-07-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_treating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='phno',
            field=models.BigIntegerField(),
        ),
    ]
