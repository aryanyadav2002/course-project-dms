# Generated by Django 4.0.3 on 2022-09-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0006_series62_series63_series64'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eqbload',
            fields=[
                ('faco', models.IntegerField(primary_key=True, serialize=False)),
                ('e', models.IntegerField()),
                ('lx', models.IntegerField()),
                ('ly', models.IntegerField()),
                ('gx', models.IntegerField()),
                ('gy', models.IntegerField()),
            ],
        ),
    ]
