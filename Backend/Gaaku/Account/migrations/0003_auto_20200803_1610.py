# Generated by Django 3.0.7 on 2020-08-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20200803_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.BigIntegerField(null=True),
        ),
    ]
