# Generated by Django 3.1 on 2020-09-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_testimony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='product',
            field=models.CharField(default='product', max_length=50),
        ),
    ]
