# Generated by Django 4.0 on 2023-07-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_notifydatabase'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifydatabase',
            name='patname',
            field=models.CharField(default='karthik', max_length=30),
            preserve_default=False,
        ),
    ]
