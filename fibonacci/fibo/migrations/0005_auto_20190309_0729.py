# Generated by Django 2.2 on 2019-03-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibo', '0004_auto_20190308_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfibo',
            name='fibo',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
