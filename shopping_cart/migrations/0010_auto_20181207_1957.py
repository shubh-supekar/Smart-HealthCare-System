# Generated by Django 2.0.5 on 2018-12-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0009_auto_20181207_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='patient_name',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_phno',
            field=models.IntegerField(null=True),
        ),
    ]