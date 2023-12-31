# Generated by Django 4.0 on 2023-07-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('phno', models.BigIntegerField()),
            ],
        ),
    ]
