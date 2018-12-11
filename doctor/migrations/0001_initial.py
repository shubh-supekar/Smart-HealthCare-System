# Generated by Django 2.0.5 on 2018-12-11 13:06

from django.db import migrations, models
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('slug', models.SlugField(default='abc')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=40.5, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=doctor.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
