# Generated by Django 4.0.3 on 2022-09-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rpm', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rload', models.DecimalField(decimal_places=2, max_digits=8)),
                ('aload', models.DecimalField(decimal_places=2, max_digits=8)),
                ('lfactor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('elife', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
