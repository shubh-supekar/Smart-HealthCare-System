# Generated by Django 2.1.2 on 2018-10-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.CharField(max_length=1000)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=1)),
                ('email_id', models.CharField(max_length=250)),
                ('mobile_no', models.BigIntegerField()),
                ('speciality', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('locality', models.CharField(max_length=250)),
                ('hospital', models.CharField(max_length=250)),
            ],
        ),
    ]
