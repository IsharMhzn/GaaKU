# Generated by Django 3.1 on 2020-09-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_timestamp'),
        ('Account', '0012_auto_20200922_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
