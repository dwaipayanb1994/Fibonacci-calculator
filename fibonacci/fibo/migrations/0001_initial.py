# Generated by Django 2.2 on 2019-03-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFibo',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('fibo', models.BigIntegerField()),
            ],
        ),
    ]
