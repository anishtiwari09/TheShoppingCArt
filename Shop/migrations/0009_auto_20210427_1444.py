# Generated by Django 3.2 on 2021-04-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20210427_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderid',
            new_name='order_id',
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock_qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('Electronics', (('Washing Machine', 'Washing Machine'), ('Refrigerators', 'Refrigerators'), ('Mixer Grinder & Juicer', 'Mixer Grinder & Juicer'), ('Others', 'Others')))], max_length=100),
        ),
    ]