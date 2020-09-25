# Generated by Django 3.1 on 2020-09-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='sub_category1',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
