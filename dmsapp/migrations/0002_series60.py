# Generated by Django 4.0.3 on 2022-09-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='series60',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skfNo', models.IntegerField()),
                ('dia', models.IntegerField()),
                ('d1min', models.IntegerField()),
                ('dcap', models.IntegerField()),
                ('d2min', models.IntegerField()),
                ('bB', models.IntegerField()),
                ('rR', models.IntegerField()),
                ('rR1', models.IntegerField()),
                ('staticC', models.IntegerField()),
                ('dynamicC', models.IntegerField()),
                ('maxSpeed', models.IntegerField()),
            ],
        ),
    ]
