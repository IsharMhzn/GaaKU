# Generated by Django 3.0.7 on 2020-08-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20200803_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
