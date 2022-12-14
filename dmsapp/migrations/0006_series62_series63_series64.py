# Generated by Django 4.0.3 on 2022-09-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0005_alter_userip_aload_alter_userip_dia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='series62',
            fields=[
                ('skfNo', models.IntegerField(primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='series63',
            fields=[
                ('skfNo', models.IntegerField(primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='series64',
            fields=[
                ('skfNo', models.IntegerField(primary_key=True, serialize=False)),
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
